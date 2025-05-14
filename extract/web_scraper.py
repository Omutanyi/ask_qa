import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n'.join(p.get_text() for p in paragraphs)
        return text.strip()
    except Exception as e:
        return f"[Error extracting text from {url}: {e}]"
