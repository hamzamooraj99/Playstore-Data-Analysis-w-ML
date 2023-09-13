import pandas as pd

def main(popularity_csv, general_csv, new_file):
    popularity_dataset = pd.read_csv(popularity_csv)
    feature_dataset = pd.read_csv(general_csv)

    main_features = feature_dataset.iloc[:, 4:8]
    extra_features = feature_dataset.iloc[:, 13:]

    data = {
        'title' : feature_dataset['title'],
        'score' : feature_dataset['score'],
        'ratings' : feature_dataset['ratings'],
        'installs' : feature_dataset['maxInstalls'],
        'popularity_index' : popularity_dataset['popularity_index'],
    }

    df = pd.DataFrame(data)

    dataset = pd.concat([df, main_features, extra_features], axis=1, join='inner')

    dataset.to_csv(new_file, index=False)

if __name__ == '__main__':
    main('./Datasets/App_Popularity_US.csv', './Datasets/Apps_Refined_US.csv', './Datasets/Final_App_Popularity_US.csv')
    main('./Datasets/App_Popularity_PK.csv', './Datasets/Apps_Refined_PK.csv', './Datasets/Final_App_Popularity_PK.csv')