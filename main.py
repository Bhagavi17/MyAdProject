import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🕷️ AI-Powered Web Scraper")

url = st.text_input("Enter a website URL", "https://www.wikipedia.org")

if st.button("Scrape Website"):
    try:
        html = scrape_website(url)
        st.success("✅ Website scraped successfully!")

        raw_body = extract_body_content(html)
        cleaned_text = clean_body_content(raw_body)
        chunks = split_dom_content(cleaned_text)

        st.subheader("📄 Cleaned Page Content")
        for i, chunk in enumerate(chunks):
            st.text_area(f"Chunk {i + 1}", chunk, height=200)

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
