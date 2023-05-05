import pandas as pd
import numpy as np
import random

df = pd.read_csv('cleaned_video_games.csv')

# dictionary to store the mapping from game name to index
game_to_index = {game: i for i, game in enumerate(df['Name'].unique())}

# df = df[df['Number_of_Ratings'] >= 10]

# sort the dataframe by mean rating in descending order
df = df.sort_values(by='Mean_Rating', ascending=False)

# Create an empty user-item matrix
num_users = 671
num_games = len(game_to_index)
matrix = np.zeros((num_users, num_games))

# iterate over the rows of the dataframe and fill in the matrix
user_counts = np.zeros(num_users)
for i, row in df.iterrows():
    game_index = game_to_index[row['Name']]
    mean_rating = row['Mean_Rating']
    num_ratings = int(row['Number_of_Ratings'])
    if num_ratings > 4000:
        shift = random.randint(10, 40)
        num_ratings = num_users - shift
    elif num_ratings > 2000 and num_ratings < 4000:
        shift = random.randint(40, 70)
        num_ratings = num_users - shift
    elif num_ratings > 1000 and num_ratings < 2000:
        shift = random.randint(70, 120)
        num_ratings = num_users - shift
    elif num_ratings >= num_users and num_ratings < 1000:
        shift = random.randint(120, 160)
        num_ratings = num_users - shift
    elif num_ratings < num_users and num_ratings > 200:
        num_ratings -= 100
    elif num_ratings < num_users and num_ratings > 20:
        num_ratings -= 18

    users = np.random.choice(num_users, size=num_ratings, replace=False)
    ratings = np.random.normal(mean_rating, 1, size=num_ratings)
    for user, rating in zip(users, ratings):
        matrix[user, game_index] = rating
        user_counts[user] += 1
    if np.max(user_counts) >= 170:
        break

# convert the matrix to a dataframe
game_names = df['Name'].unique()
matrix_df = pd.DataFrame(matrix, columns=game_names)
matrix_df.index += 1 
matrix_df.insert(0, 'users', range(1, 672))

matrix_df.to_csv('vg_user_item.csv', index=False)
