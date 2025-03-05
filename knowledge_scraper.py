import os
import requests
import json
import time
from bs4 import BeautifulSoup
from transformers import pipeline

summarizer = pipeline("summarization")

def scrape_website(url, retries=3, delay=5):
    """Attempt to scrape a website, retrying if needed."""
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join([p.text for p in soup.find_all('p')])
            return summarizer(text, max_length=150, min_length=30, do_sample=False)
        except requests.exceptions.RequestException as e:
            print(f"⚠️  Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
    print(f"❌ Failed to retrieve {url} after {retries} attempts.")
    return None

def update_knowledge_base():
    urls = [
        "https://arxiv.org/list/cs.AI/recent",
        "https://www.browse.ai/docs/api/v2#tag/robots/operation/getRobots",  # Might be outdated, replace if necessary
        "https://www.deeplearning.ai/the-batch/"
    ]

    knowledge = {}
    for url in urls:
        summary = scrape_website(url)
        if summary:
            knowledge[url] = summary

    with open(os.path.join(os.getcwd(), "knowledge", "knowledge_base.json"), "w") as f:
        json.dump(knowledge, f, indent=4)

    print("✅ Knowledge base updated.")

if __name__ == "__main__":
    update_knowledge_base()
