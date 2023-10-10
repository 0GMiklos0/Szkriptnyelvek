#!/usr/bin/env python3
import sys

def main():
    print("hello",end = '')
    print("world")
    print("hello", "world", sep = '')
    print("hello", "world", file = sys.stderr)
    sys.stdout.write("he") # csak string lehet
    sys.stdout.write("he")
    
if __name__ == "__main__":
    main()