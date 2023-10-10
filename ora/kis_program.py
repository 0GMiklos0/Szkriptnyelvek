def get_movie_info():
    return ('Totall Recall', 1990, 7.5)

def main():
    t = get_movie_info()
    title,year,score = t
    print(title, year, score)
    
if __name__ == "__main__":
    main()