# News Summary Translator

This project fetches the latest world news articles from Yahoo! Japan, translates their content from Japanese to English using Google Cloud Translate API, and summarizes the key entities using Google Cloud Natural Language API. The results can be saved as a JSON file or printed to the console.

---

## ⚡ Features

* Scrapes latest world news topics from [Yahoo! Japan](https://news.yahoo.co.jp/topics/world)
* Extracts article content from each news article URL
* Translates content from Japanese to English using Google Cloud Translation API
* Extracts key entities for summarization using Google Cloud Natural Language API
* Supports output to JSON file or standard output (console) using `--output` option

---

## 📂 Project Structure

```
.
├── summaries.json (optional)
├── scripts/
│   ├── main.py
│   ├── news_scraper.py
│   ├── summarizer.py
│   └── translator.py
```

---

## ⚙ Requirements

* Python 3.8+
* `google-cloud-translate`
* `google-cloud-language`
* `beautifulsoup4`
* `requests`

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up Google Cloud credentials:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
```

---

## 🔧 Usage

```bash
python scripts/main.py --output json      # Saves summaries to summaries.json
python scripts/main.py --output console   # Prints summaries to standard output
```

It will:

1. Fetch recent article titles and URLs
2. Extract their content
3. Translate to English
4. Summarize key entities
5. Output results based on `--output` selection

---

## 📗 Output Example (JSON)

```json
[
  {
    "title": "Some Japanese News Title",
    "original": "元の文章...",
    "translated": "The original article translated to English...",
    "summary": "Keywords: Prime Minister, Japan, Trade, Policy"
  }
]
```

---

## ✉ Notes

* Yahoo! Japan articles may require adjustments due to layout changes.
* You can switch sources or languages by modifying `news_scraper.py` and `translator.py`.
* The `--output` flag helps choose between file output and terminal display.

---

## 🚀 License

[MIT License](./LICENSE)

---

## ✍️ Author

\[ty70]
