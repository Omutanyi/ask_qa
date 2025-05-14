import streamlit as st
from search.web_search import search_web
from search.youtube_search import search_youtube
from extract.web_scraper import extract_text_from_url
from extract.video_transcripts import get_transcript
from llm.answer_with_citations import ask_with_citations

def run_app():
    st.set_page_config(page_title="Ask the Web + YouTube", layout="wide")
    st.title("🔍 Ask the Web + YouTube")

    source_type = st.sidebar.radio("Sources", ["Both", "Include Web", "Include YouTube"], index=0)
    show_debug = st.sidebar.checkbox("Show Debug Panel", value=False)

    question = st.text_input("Ask a question:")
    if st.button("Ask") and question:
        results = []
        sources = []

        if source_type in ["Both", "Include Web"]:
            web_results = search_web(question)
            for result in web_results:
                print (result) 
                content = extract_text_from_url(result)
                sources.append({"content": content})
                results.append({**result, "content": content})

        if source_type in ["Both", "Include YouTube"]:
            yt_results = search_youtube(question)
            for result in yt_results:
                transcript, _ = get_transcript(result["video_id"])
                sources.append({"content": transcript})
                results.append({**result, "content": transcript})

        if not sources:
            st.warning("No sources found.")
            return

        answer = ask_with_citations(question, sources)
        st.markdown("### 📘 Answer")
        st.markdown(answer)

        with st.expander("📚 Sources"):
            for i, result in enumerate(results):
                st.markdown(f"[{i+1}] [{result['title']}]({result['url']})")

        if show_debug:
            with st.expander("🛠️ Debug JSON"):
                st.json(results)
