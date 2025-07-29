from bs4 import BeautifulSoup

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body):
    soup = BeautifulSoup(body, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    cleaned = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
