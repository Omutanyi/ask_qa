# Ask the Web + YouTube

A Streamlit app that answers your questions using both public websites and YouTube videos.

## 🚀 Quickstart

```bash
git clone https://github.com/your/repo.git
cd ask-qa
cp .env.example .env  # Add your API keys
docker build -t ask-qa .
docker run -p 8501:8501 ask-qa


🏗 Architecture
search/: Web and YouTube search

extract/: Content extraction

llm/: LLM answers with citations

ui/: Streamlit interface

tests/: Pytest unit tests

🤖 Prompt Logic
Citations [1]... are inserted where LLMs find direct support. Keeps answers traceable.

⚠️ Known Limitations
Only top 5 pages / 3 videos

Citations rely on LLM compliance

Basic transcript summarization


ask-qa/
├── app.py
├── search/
│   ├── web_search.py
│   ├── youtube_search.py
│   └── __init__.py
├── extract/
│   ├── web_scraper.py
│   ├── video_transcripts.py
│   └── __init__.py
├── llm/
│   └── answer_with_citations.py
├── ui/
│   └── streamlit_ui.py
├── tests/
│   ├── test_transcripts.py
│   └── test_citations.py
├── .env.example
├── requirements.txt
├── Dockerfile
├── README.md
└── utils.py
