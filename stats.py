import pandas as pd

def main(csv_file):
    df = pd.read_csv(csv_file)

    contentRating = df['contentRating'].nunique()
    genre = df['genre'].nunique()

    print("Content Rating:", contentRating, " unique values")
    print("Genre:", genre, " unique values")

if __name__ == '__main__':
    print("----- US -----")
    main('./Datasets/Final_App_Popularity_US.csv')

    print("----- PK -----")
    main('./Datasets/Final_App_Popularity_PK.csv')
