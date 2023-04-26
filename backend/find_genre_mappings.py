import pandas as pd

# finding unique game genres
games_df = pd.read_csv('cleaned_video_game_sales_and_ratings.csv')
games_unique_genres = games_df['Genre'].unique()

# finding unique movie genres
movies_df = pd.read_csv('cleaned_movies.csv')
movies_df['genre_list'] = movies_df['genres'].str.split('|')
movies_df_exploded = movies_df.explode('genre_list')
movies_unique_genres = movies_df_exploded['genre_list'].unique()

print('Unique video game genres')
print('------------------')
print(games_unique_genres)
print('Unique movie genres')
print('------------------')
print(movies_unique_genres)