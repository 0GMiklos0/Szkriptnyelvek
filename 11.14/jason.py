import json

def main():
    f = open("11.14/person.json", "r")
    d = json.load(f)
    print(d["age"])
if __name__ == "__main__":
    main()