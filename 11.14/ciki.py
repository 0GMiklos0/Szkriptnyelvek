#!/usr/bin/env python3

import requests
import time
import random

URL = "https://divany.hu/offline/2016/03/19/meno_vagy_ciki_a_gyarilag_koszos_cipo/"
ITERATION = 10

def main():
    for i in range(ITERATION):
        r = requests.get(URL)
        html = r.text
        print('.', end='', flush = True)
        time.sleep(random.randint(1,10))
    print('\n')
    
if __name__ == "__main__":
    main()