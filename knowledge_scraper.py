import os
import requests
import json
from bs4 import BeautifulSoup
from transformers import pipeline

# AI model for processing web content
summarizer = pipeline("summarization")

def scrape_website(url):
    """Scrapes web content and extracts key information."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        return summarizer(text, max_length=150, min_length=30, do_sample=False)
    return None

def update_knowledge_base():
    """Fetches knowledge from key AI sources and updates the AI system."""
    urls = [
        "https://arxiv.org/list/cs.AI/recent",
        "https://blog.openai.com",
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
