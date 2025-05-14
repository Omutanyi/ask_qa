from llm.answer_with_citations import format_sources

def test_format_sources():
    sources = [{"content": "Source one"}, {"content": "Source two"}]
    formatted = format_sources(sources)
    assert "[1] Source one" in formatted
    assert "[2] Source two" in formatted
