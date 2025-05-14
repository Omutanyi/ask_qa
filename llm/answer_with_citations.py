import os
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() 

class GeminiClient:
    def __init__(self):
        secret_key = os.getenv("Gemini_API_KEY")
        genai.configure(api_key=secret_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    def format_sources(self, sources: List[Dict]) -> str:
        return "\n\n".join([f"[{i+1}] {src['content']}" for i, src in enumerate(sources)])
    
    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating response: {str(e)}"

def ask_with_citations(question: str, sources: List[Dict]) -> str:
    """Ask a question with source citations using Gemini's free tier."""
    client = GeminiClient()
    context = client.format_sources(sources)
    
    prompt = f"""You are a helpful assistant. Answer the user's question using only the sources below.
    Always cite the sources with [1], [2], etc. when using information from them.

    Question: {question}

    Sources:
    {context}

    Answer (with citations where applicable):"""
    
    return client.generate_response(prompt)
