#!/usr/bin/env python3
import utils_mod as um

def main():
    print([um.duplaz(i) for i in range(10)])

if __name__ == "__main__":
    print(um.__name__)
    main()