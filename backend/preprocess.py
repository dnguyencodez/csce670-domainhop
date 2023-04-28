import pandas as pd

# preprocess video games
games = pd.read_csv('./datasets/Video_Game_Sales_as_of_Jan_2017.csv')

# drop rows with missing User_score values
# games = games.dropna(subset=['User_Score'])

# drop unnecessary columns
games = games.drop(['User_Score', 'Platform', 'Year_of_Release', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Count', 'Rating'], axis=1)
games.to_csv('cleaned_video_games.csv', index=False)


# preprocess movies
movies = pd.read_csv('./datasets/movies.csv')
ratings = pd.read_csv('./datasets/ratings.csv')

# find each movieId's avg rating
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()

# combine the movies.csv and ratings.csv files, excluding the timestamp columns (bc movies.csv has genres and ratings.csv has ratings, userId, and timestamp)
merged_data = pd.merge(movies, avg_ratings, on='movieId', how='inner')
merged_data = merged_data.drop(['movieId', 'rating'], axis=1)
merged_data.to_csv('cleaned_movies.csv', index=False)