#!/usr/bin/env python3
class Proba:
    static_value = 12345 # osztalyvaltozo
    def hello(self):
        print("hello")

def main():
    print(Proba.static_value)
    p = Proba()
    p.hello()

if __name__ == "__main__":
    main()