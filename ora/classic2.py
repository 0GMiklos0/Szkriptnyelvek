#!/usr/bin/env python3
class Hello:
    def create_name(self, name):
        self.name = name
    # nem kell elejen deklaralni az atTRIBUTUMOt
    def display_name(self):
        return self.name
    
    def greet(self):
        print(f"Hello {self.name}")

def main():
    h = Hello
    # print(h.name) -- hiba
    h.create_name("mmmmmmmm")
    print(h.name)
    print(h.display_name())
    h.greet()
    
if __name__ == "__main__":
    main()