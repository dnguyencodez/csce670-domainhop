import pandas as pd
import requests
from collections import defaultdict


# preprocess movies
movies = pd.read_csv('./datasets/movies.csv')
ratings = pd.read_csv('./datasets/ratings.csv')
tags = pd.read_csv('./datasets/tags.csv')

# find each movieId's avg rating
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()

# combine the movies.csv and ratings.csv files, excluding the timestamp columns (bc movies.csv has genres and ratings.csv has ratings, userId, and timestamp)
merged_data = pd.merge(movies, avg_ratings, on='movieId', how='inner')

movieIDs = merged_data["movieId"].tolist()

description = {idx:"" for idx in movieIDs}

for index, row in tags.iterrows():
    if row["movieId"] in description:
        description[row["movieId"]] += str(row["tag"]) + " "

merged_data["description"] = merged_data["movieId"].apply(lambda x : description[x])
 
merged_data.to_csv('cleaned_movies.csv', index=False)

