import pandas as pd

movies = pd.read_csv('./datasets/movies.csv')
ratings = pd.read_csv('modified_ratings.csv')

# pivot the ratings dataframe
user_item_matrix = ratings.pivot_table(index='userId', columns='title', values='rating')

# fill missing values with a blank
user_item_matrix = user_item_matrix.fillna('')

# reindex the columns with all movie titles
user_item_matrix = user_item_matrix.reindex(columns=movies['title'])
user_item_matrix.to_csv('movie_user_item.csv')
