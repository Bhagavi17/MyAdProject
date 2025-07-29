import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.set_page_config(page_title="AI Webscraper", layout="wide")
st.title("🌐 AI Website Scraper")
st.write("Enter a website URL to scrape its content:")

url = st.text_input("Website URL", placeholder="https://example.com")

if url and st.button("Scrape Website"):
    try:
        raw_html = scrape_website(url)
        body = extract_body_content(raw_html)
        cleaned = clean_body_content(body)
        parts = split_dom_content(cleaned)

        st.success("✅ Website scraped successfully!")
        for i, part in enumerate(parts):
            with st.expander(f"📄 Content Block {i+1}", expanded=(i == 0)):
                st.text(part)

    except Exception as e:
        st.error(f"❌ Error: {e}")
