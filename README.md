# AI Chat Log Summarizer

**AI Chat Log Summarizer** is a Python-based tool that reads `.txt` chat logs between a user and an AI, analyzes the conversation, and generates a clear summary. It includes message statistics and keyword insights using basic Natural Language Processing (NLP).

---

## 🚀 Features

- ✅ Parses chat logs in the format:
  ```
  User: Hello
  AI: Hi! How can I help?
  ```
- Separates messages by speaker (User / AI)
- Counts messages from User vs AI
- Extracts the top 5 most used words (excluding stopwords)
- Generates a natural-language summary
- (Optional) Can be extended to use TF-IDF for better keyword relevance


## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/chat_summarizer.git
cd chat_summarizer
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
env\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK stopwords (one-time only)

```bash
python setup_nltk.py
```

---

## How to Run

Make sure your chat file (like `chat.txt`) is formatted properly.

Then run:

```bash
python chat_log_summarizer.py --file chat.txt
```

---

## Example Output

```
Summary:
- The conversation had 8 exchanges.
- Most common keywords: python, use, data, ai, language.
```

---

## License

MIT License. Free to use and modify.

---
