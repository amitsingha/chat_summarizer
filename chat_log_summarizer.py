import os
import re
from collections import Counter, defaultdict
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

STOPWORDS = set(stopwords.words('english'))

def parse_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    user_msgs, ai_msgs = [], []
    all_text = []

    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            msg = line[5:].strip()
            user_msgs.append(msg)
            all_text.append(msg)
        elif line.startswith("AI:"):
            msg = line[3:].strip()
            ai_msgs.append(msg)
            all_text.append(msg)

    return user_msgs, ai_msgs, all_text

def messages_statistics(user_msgs, ai_msgs):
    return {
        'total': len(user_msgs) + len(ai_msgs),
        'user': len(user_msgs),
        'ai': len(ai_msgs)
    }

def keywords_analysis(texts, method='simple', top_n=5):

    words = re.findall(r'\b\w+\b', ' '.join(texts).lower())
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    freq = Counter(words)
    return [word for word, _ in freq.most_common(top_n)]

def generate_summary(message_counts, keywords):
    return f"""Summary:
- This conversation had {message_counts['total']} exchanges.
- Most common keywords: {', '.join(keywords)}"""

def summarize_file(file_path, method='simple'):
    user_msgs, ai_msgs, all_text = parse_chat_log(file_path) # 2.1 :: Chat Log Parsing
    message_counts = messages_statistics(user_msgs, ai_msgs) # 2.2 :: Message Statistics
    keywords = keywords_analysis(all_text, method=method) # 2.3 :: Keyword Analysis
    summary = generate_summary(message_counts, keywords)
    print(summary)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="AI Chat Log Summarizer")
    parser.add_argument('--file', type=str, help='Path to a single chat log file')

    args = parser.parse_args()
    summarize_file(args.file)
