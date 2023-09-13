import pandas as pd

def remove_duplicate(csv_file, new_file):
    dataset = pd.read_csv(csv_file)
    dataset[dataset.duplicated(['title'])]
    dataset = dataset.drop_duplicates(subset='title', keep='first')
    dataset.to_csv(new_file, index=False)

if __name__ == "__main__":
    remove_duplicate('./Datasets/Playstore_Popular_Apps_US.csv', './Datasets/Playstore_Popular_Apps_US.csv')
    remove_duplicate('./Datasets/PlayStore_Popular_Apps_PK.csv', './Datasets/PlayStore_Popular_Apps_PK.csv')