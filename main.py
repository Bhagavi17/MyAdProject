import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.set_page_config(page_title="AI Web Scraper", layout="wide")

st.title("🔍 AI Website Content Scraper")
st.markdown("Enter a website URL below to scrape and extract its main content.")

# Input form
url = st.text_input("🌐 Enter URL", placeholder="https://example.com")

if st.button("Scrape"):
    if not url:
        st.error("Please enter a URL.")
    else:
        try:
            with st.spinner("Scraping website..."):
                html = scrape_website(url)
                body = extract_body_content(html)
                cleaned = clean_body_content(body)
                split_parts = split_dom_content(cleaned)

            st.success("✅ Scraping complete!")
            st.subheader("📄 Extracted Content:")
            for i, part in enumerate(split_parts):
                st.text_area(f"Part {i + 1}", part, height=300)

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
