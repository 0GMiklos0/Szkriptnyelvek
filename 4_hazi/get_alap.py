#!/usr/env/bin python3
import shutil
import os
import sys

TEXT = """
---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
q) quit"""

def main():
    F_TEXT = TEXT.strip() + '\n'
    s = input(F_TEXT)
    if len(sys.argv) > 2:
        if os.path.isfile("alap.py"):
            print("Mar letezik a fajl",file = sys.stderr)
        elif s == '1':
            shutil.copy("alap.py",'')
        elif s == '2':
            shutil
        elif s == 'q':
            return 0


if __name__ == "__main__":
    main()