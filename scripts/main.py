import argparse
import json
from scripts.news_scraper import fetch_news
from scripts.translator import translate_to_english
from scripts.summarizer import summarize_text


def main(output_mode):
    articles = fetch_news()
    print("Number of articles fetched:", len(articles))
    print("Article titles:", [a["title"] for a in articles])
    summaries = []

    for article in articles:
        translated = translate_to_english(article['content'])
        summary = summarize_text(translated)
        summaries.append({
            "title": article['title'],
            "original": article['content'],
            "translated": translated,
            "summary": summary
        })

    if output_mode == 'json':
        with open("summaries.json", "w", encoding="utf-8") as f:
            json.dump(summaries, f, ensure_ascii=False, indent=2)
        print("Output saved to summaries.json")
    elif output_mode == 'console':
        for summary in summaries:
            print("\n---\n")
            print(f"Title: {summary['title']}")
            print(f"Original: {summary['original'][:100]}...")
            print(f"Translated: {summary['translated'][:100]}...")
            print(f"Summary: {summary['summary']}")
    else:
        print("Invalid output mode. Use 'json' or 'console'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch, translate, and summarize Yahoo! Japan news articles.")
    parser.add_argument('--output', choices=['json', 'console'], default='json', help='Output destination')
    args = parser.parse_args()

    main(args.output)
