
import urllib.request as uri
import os

def main():
    url = "https://www.python.org/"
    response = uri.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    print(html[:100])
    
def image():
    url = "https://i.ytimg.com/vi/NU5O-LqDFa4/sddefault.jpg"
    uri.urlretrieve(url)
    cmd = f"wget {url} -O lebruhjames.png"
    print(cmd)
    os.system(cmd)
    
if __name__ == "__main__":
    main()
image()