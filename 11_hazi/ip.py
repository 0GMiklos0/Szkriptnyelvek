from urllib.request import Request, urlopen

def keressip(s : list[str]) -> str:
    for i in s :
        j = i.lower()
        if "\"ip\"" in j:
            return j
        


def main():
    
    req = Request(url='https://reallyfreegeoip.org/json/', headers={'User-Agent': 'Mozilla/5.0'})
    raw = urlopen(req).read()
    html = raw.decode("utf-8")
    s = html.split(",")
    ip = keressip(s)
    ip = ip.replace("{","").replace("}","").replace("\"","")
    ip = ip[3:]
    print("Az Ön IP címe:", ip)
    
if __name__ == "__main__":
    main()