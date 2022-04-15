#import library yang dibutuhkan
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#lakukan pembacaan dataset
movie_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.basics.tsv', sep='\t') #untuk menyimpan title_basics.tsv
rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='\t') #untuk menyimpan title.ratings.tsv
