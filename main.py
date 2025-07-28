import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.set_page_config(page_title="AI Webscraper", layout="wide")

st.title("🕷️ AI Webscraper")
url = st.text_input("Enter URL to scrape:")

if url:
    try:
        st.write("Scraping the website...")
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)
        chunks = split_dom_content(cleaned_content)

        st.success("Scraping completed successfully!")
        st.subheader("Scraped Content")
        for i, chunk in enumerate(chunks):
            st.markdown(f"### Chunk {i+1}")
            st.text_area("", chunk, height=200)

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
