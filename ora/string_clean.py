INPUT = "string_1.py"

def main():
    with open(INPUT, "r") as f:
        sorok = f.read().splitlines()
        print(sorok)
        takarito = [l for l in sorok if l.startswith()!="#"]
        print(takarito)
        
if __name__ == "__main__":
    main()