from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(url):
    options = Options()
    options.add_argument('--headless')          # Run Chrome in headless mode
    options.add_argument('--no-sandbox')        # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

    # ✅ Update path to your chromedriver if it's placed locally
    driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)

    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body):
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    cleaned = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
