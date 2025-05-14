from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = ""
        entries = []
        for entry in transcript:
            entries.append({
                "start": entry["start"],
                "text": entry["text"]
            })
            full_text += f"[{entry['start']:.0f}] {entry['text']}\n"
        return full_text, entries
    except Exception as e:
        return f"[Error fetching transcript: {e}]", []
