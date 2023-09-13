import pandas as pd
import numpy as np
import math
import statistics as stats

def gini(n1, n2, n3, n4, n5):
  arr = [n1, n2, n3, n4, n5]
  arr = np.array(arr)
  total = 0
  for i, xi in enumerate(arr[:-1], 1):
    total += np.sum(np.abs(xi - arr[i:]))
  return total / (len(arr)**2 * np.mean(arr))

#Function f is for installations
def f(installs):
    return(math.log10(installs))

#Function g is for user engagement(# of ratings vs # of installations)
def g(ratings, installs):
    return(
        math.log10(ratings) / math.log10(installs) 
    )

#Function h is for score adjustment
def h(ratings, score, gini):
   a = math.log10(ratings)
   b = score - 3
   return(a * b * gini)

def popularity_index(f, g, h):
    f_weight, g_weight, h_weight = 0.7, 0.2, 0.1
    return(
        (f_weight * f) + (g_weight * g) + (h_weight * h)
    )

def main(csv_file, new_file):
   
  dataset = pd.read_csv(csv_file)

  data = {
    'title' : dataset['title'],
    'score' : dataset['score'],
    'ratings' : dataset['ratings'],
    'installs' : dataset['maxInstalls']
  }

  df = pd.DataFrame(data)

  df['gini_coeff'] = dataset.apply(lambda row : gini(
    row['n_stars_1'],
    row['n_stars_2'],
    row['n_stars_3'],
    row['n_stars_4'],
    row['n_stars_5']
  ), axis=1)

  df['popularity_index'] = df.apply(lambda row : popularity_index(
    f(row['installs']),
    g(row['ratings'] , row['installs']),
    h(row['ratings'] , row['score'] , row['gini_coeff'])
  ), axis=1)

  df.to_csv(new_file, index=False)

if __name__ == '__main__':
   main('./Datasets/Apps_Refined_US.csv', './Datasets/App_Popularity_US.csv')
   main('./Datasets/Apps_Refined_PK.csv', './Datasets/App_Popularity_PK.csv')