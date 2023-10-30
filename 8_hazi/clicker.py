import mouse

def main():
    while not (mouse.is_pressed("left")):
        continue
    [mouse.click('left') for i in range(2023)]

if __name__ == "__main__":
    main()