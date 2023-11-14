import urllib.request as uri

def get_page(url: str) -> str:
    response = uri.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    return html