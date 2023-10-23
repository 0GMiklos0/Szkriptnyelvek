
def main():
    with open("7_hazi/string1.py", "r") as f:
        x = f.read().splitlines()
        x = [s for s in x if not s.strip().startswith("#")]
        f.close()
    with open("7_hazi/string1_clean.py", "w") as w:
        for s in x:
            print(s,file=w)


if __name__ == "__main__":
    main()