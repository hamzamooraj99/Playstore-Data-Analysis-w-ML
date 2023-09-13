Run in the following order:
    1) duplicate.py
        ~ Finds and removes all duplicates from original file (Playstore_Popular_Apps_...)
        ~ Saves it into itself

    2) dataset_refiner.py
        ~ Removes all the irrelevant information in the original dataset (Playstore_Popular_Apps_...)
        ~ Creates a new csv file (Apps_Refined_...)

    3) popularity_index.py
        ~ Calculates the popularity index using values from the refined dataset (Apps_Refined_...)
        ~ Scales the popularity_index from a range of 0-40 to the range 0-5
        ~ Creates a new csv file (App_Popularity_...)

    4) compilation.py
        ~ Combines the values used to calculate popularity_index (incl. popularity_index) and all features/characteristics of apps
        ~ Creates a new csv_file (Final_App_Popularity_...)