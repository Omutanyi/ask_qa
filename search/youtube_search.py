import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv() 

def search_youtube(query, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    results = []
    for i, item in enumerate(response["items"]):
        results.append({
            "id": f"yt_{i+1}",
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "url": f"https://youtube.com/watch?v={item['id']['videoId']}"
        })
    return results
