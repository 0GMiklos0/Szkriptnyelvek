#!/usr/bin/env python3
import json
import urllib.request 

def main():
    url = "http://www.reddit.com/r/earthporn/.json"
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    json_data = json.loads(html)
    children = json_data['data']['children']
    for child in children:
        url = child['data']['url']
        print(url)

if __name__ == "__main__":
    main()