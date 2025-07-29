import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.set_page_config(page_title="AI Webscraper", layout="wide")
st.title("🔎 AI-Powered Website Content Scraper")

url = st.text_input("Enter URL to scrape:", placeholder="https://example.com")

if st.button("Scrape Now") and url:
    try:
        html = scrape_website(url)
        body = extract_body_content(html)
        clean_text = clean_body_content(body)
        parts = split_dom_content(clean_text)

        st.success("✅ Scraping successful!")
        for i, part in enumerate(parts):
            with st.expander(f"📄 Page Section {i+1}"):
                st.code(part)
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
