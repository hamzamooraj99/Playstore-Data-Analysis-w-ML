import pandas as pd

def change_2(value):
    if(value == 2):
        value = 1
    else:
        return

def refine(csv_file, new_csv_file):
    dataset = pd.read_csv(csv_file)
    main_data = dataset.iloc[:, [0, 1, 4, 11, 8, 5, 17, 20]]
    rating_data = dataset.iloc[:, 22:27]
    extra_data = dataset.iloc[:, 27:90]
    
    dataset = pd.concat([main_data, rating_data, extra_data], axis=1, join='inner')

    dataset.to_csv(new_csv_file, index=False)

if __name__ == "__main__":
    refine('./Datasets/Playstore_Popular_Apps_US.csv', './Datasets/Apps_Refined_US.csv')
    refine('./Datasets/PlayStore_Popular_Apps_PK.csv', './Datasets/Apps_Refined_PK.csv')