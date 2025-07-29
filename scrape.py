import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ Path to local ChromeDriver
    service = Service(executable_path=os.path.abspath("chromedriver.exe"))  # Ensure chromedriver.exe is in the same folder
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    return str(soup.body) if soup.body else ""

def clean_body_content(body):
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    cleaned = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
