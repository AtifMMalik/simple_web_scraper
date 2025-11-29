import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# --- load helpers ---
def load_list_from_file(path, key):
    with open(path, "r") as f:
        return set(json.load(f).get(key, []))

crawl_queue = load_list_from_file("./data/data.json", "crawl_queue")
processed_urls = load_list_from_file("./data/data.json", "URLs")  # adjust key if your file uses a different name

# --- page processor: takes html + base and adds normalized links to crawl_queue ---
def process_page(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all("a")
    for a in anchors:
        href = a.get("href")
        if not href:
            continue
        href = href.strip()

        # skip anchors, javascript, mailto, etc.
        if href.startswith("#") or href.lower().startswith(("javascript:", "mailto:")):
            continue

        # resolve relative URLs to absolute
        full = urljoin(base_url, href)
        # avoid re-adding already processed or already queued
        if full not in processed_urls:
            crawl_queue.add(full)

# --- main loop (fixed logic & counters) ---
limit = int(input("Enter the iteration limit: "))   # convert to int
limit_count = 0

while crawl_queue and limit_count < limit:
    url = crawl_queue.pop()

    # avoid reprocessing
    if url in processed_urls:
        print("Skipping...")
        print(url)
        print("------------------------------------------------")
        continue

    print("Processing...   [" , limit_count ,"]")
    print(url)
    print("------------------------------------------------")


    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        # skip bad URLs (network errors, invalid schema, 4xx/5xx, etc.)
        print(f"skip {url}: {e}")
        processed_urls.add(url)
        limit_count += 1
        continue

    process_page(html, url)
    processed_urls.add(url)
    limit_count += 1

# --- save back to JSON ---
out = {
    "crawl_queue": list(crawl_queue),
    "URLs": list(processed_urls)
}
with open("./data/data.json", "w") as f:
    json.dump(out, f, indent=4)
