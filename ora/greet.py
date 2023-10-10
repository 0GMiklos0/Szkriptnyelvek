#!/usr/bin/env python3
def hello(name, repeat=1):
    [print(f"Hello {name}") for i in range(repeat)]
def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}!")
def main():
    greet("Miki", "Bonjour")
    greet("Miki", "Hola")
    greet("Miki", "Nigga")
    greet("Miki")
    hello("Miki",2)

if __name__ =="__main__":
    main()