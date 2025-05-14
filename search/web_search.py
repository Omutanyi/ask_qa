import os
import requests
from serpapi import GoogleSearch
from dotenv import load_dotenv
load_dotenv() 

def search_web(query, max_results=5):
    api_key = os.getenv("SERPAPI_KEY")
    params = {
    "q": query,
    "api_key": api_key,
    "num": max_results
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    cleaned_results = []
    for i, item in enumerate(results.get("organic_results", [])[:max_results]):
        cleaned_results.append({
            "id": f"web_{i+1}",
            "title": item.get("title"),
            "url": item.get("link"),
        })
    return cleaned_results
