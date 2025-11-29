# 🕸️ Mini Web Crawler
[![My Skills](https://skillicons.dev/icons?i=python,json)](https://skillicons.dev)

A lightweight Python-powered web crawler that discovers links, expands a crawl queue, and stores processed URLs — using **BeautifulSoup**, **Requests**, and **JSON**.

---
---

## 🚀 Features
- 🔗 Extracts **all valid links** from webpages  
- 🧭 Normalizes & resolves relative URLs  
- 🗂️ Maintains **crawl queue + processed sets**  
- 🛑 Skips anchors, `mailto:`, and `javascript:` links  
- 💾 Saves progress to `data/data.json`  
- 🧰 Minimal deps: `requests`, `beautifulsoup4`

---
---

## 📦 Project Structure
### /data
└──> data.json <span style="opacity:0.5;"># stores crawl_queue + processed URLs</span>

### /src
└──> scraper.py <span style="opacity:0.5;"># main crawler script</span>

README.md

---
---

## ▶️ Quick Start
1. Install dependencies:

bash
```bash
pip install requests beautifulsoup4
pip install requests
```
2. Run:

bash
```bash
python scraper.py
```
3. Enter iteration limit when prompted:

```
Enter the iteration limit: 50
```

---
---

## 🧠 Workflow
1. Load crawl_queue and processed_urls from data/data.json.
2. Pop a URL from the queue.
3. Fetch page with a User-Agent header.
4. Extract \<a href="..."> links with BeautifulSoup.
5. Normalize, filter, and add new links to the queue.
6. Add the processed link to the URLs list.
7. Save updated crawl_queue and URLs back to JSON.

---
---

## 📁 Data Format
 json
```json
{
    "crawl_queue": [
        "https://example.com/1",
        "https://example.com/2",
        "https://example.com/3"
        
    ],
    "URLs": [
        "https://example.com/a",
        "https://example.com/b",
        "https://example.com/c",
        "https://example.com/d"
    ]
}
```

---
---
> [!Note]
> - Practice crawler — not a production search indexer.
> - Don’t hammer sites; respect robots.txt and site terms.
> - Ignore/avoid committing large data/ files to git.

---
---

## 💡 Future Enhancements
- [ ] 🗄️ Flexible storage support (SQL, NoSQL, JSON, CSV, Excel)
- [ ] 🔧 Custom processor callbacks for personalised HTML handling
- [ ] ⏱️ Rate limiting
- [ ] 🌐 Domain filtering
- [ ] 📥 HTML caching
- [ ] 🔍 Basic search index

