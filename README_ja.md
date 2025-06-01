# ニュース要約翻訳ツール

このプロジェクトは、Yahoo! Japan から最新の国際ニュース記事を取得し、その内容を Google Cloud Translation API を用いて日本語から英語に翻訳し、さらに Google Cloud Natural Language API を使って重要なキーワードを抽出・要約します。結果は JSON ファイルとして保存するか、コンソールに出力することができます。

---

## ⚡ 特徴

* [Yahoo! Japan](https://news.yahoo.co.jp/topics/world) から最新の国際ニューストピックをスクレイピング
* 各ニュース記事の本文を抽出
* Google Cloud Translation API による日本語から英語への翻訳
* Google Cloud Natural Language API による主要キーワードの抽出と要約
* `--output` オプションによって JSON ファイルまたはコンソール出力を選択可能

---

## 📂 プロジェクト構成

```
.
├── summaries.json (任意)
├── scripts/
│   ├── main.py
│   ├── news_scraper.py
│   ├── summarizer.py
│   └── translator.py
```

---

## ⚙ 必要環境

* Python 3.8以上
* `google-cloud-translate`
* `google-cloud-language`
* `beautifulsoup4`
* `requests`

依存パッケージのインストール：

```bash
pip install -r requirements.txt
```

Google Cloud の認証情報の設定：

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
```

---

## 🔧 使い方

```bash
python scripts/main.py --output json      # summaries.json に保存
python scripts/main.py --output console   # コンソールに出力
```

処理の流れ：

1. 最新のニュースタイトルとURLを取得
2. 各記事の本文を抽出
3. 英語へ翻訳
4. 重要キーワードで要約
5. `--output` オプションに応じて結果を出力

---

## 📗 出力例 (JSON)

```json
[
  {
    "title": "ある日本語ニュースタイトル",
    "original": "元の文章...",
    "translated": "The original article translated to English...",
    "summary": "Keywords: Prime Minister, Japan, Trade, Policy"
  }
]
```

---

## ✉ 補足

* Yahoo! Japan の記事構造が変更された場合、スクレイピング部分の修正が必要になる可能性があります。
* `news_scraper.py` および `translator.py` を編集することで、ニュースソースや翻訳対象言語の変更が可能です。
* `--output` フラグで出力形式を柔軟に選択可能です。

---

## 🚀 ライセンス

[MIT ライセンス](./LICENSE)

---

## ✍️ 作者

\[ty70](./tomoakiyokoo98@gmail.com)
