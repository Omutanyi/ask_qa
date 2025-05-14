from extract.video_transcripts import get_transcript

def test_get_transcript_valid():
    text, entries = get_transcript("dQw4w9WgXcQ") 
    assert isinstance(text, str)
    assert isinstance(entries, list)
