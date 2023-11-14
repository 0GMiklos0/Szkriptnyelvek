#!/usr/bin/env python3

from pygyak import get_page

url = "https://www.python.org"

def main():
    print(get_page(url))
    
if __name__ == "__main__":
    main()