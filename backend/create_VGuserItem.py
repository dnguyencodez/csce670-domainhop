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
        shift = random.randint(350, 400)
        num_ratings = num_users - shift
    elif num_ratings > 2000 and num_ratings < 4000:
        shift = random.randint(400, 475)
        num_ratings = num_users - shift
    elif num_ratings > 1000 and num_ratings < 2000:
        shift = random.randint(475, 525)
        num_ratings = num_users - shift
    elif num_ratings >= num_users and num_ratings <= 1000:
        shift = random.randint(525, 570)
        num_ratings = num_users - shift
    elif num_ratings < num_users and num_ratings > 200:
        shift = random.randint(50, 100)
        num_ratings = shift
    elif num_ratings < num_users and num_ratings > 20:
        shift = random.randint(10, 50)
        num_ratings = shift
    else:
        shift = random.randint(1, 8)
        num_ratings = shift

    # print(num_ratings)
    users = np.random.choice(num_users, size=num_ratings, replace=False)
    ratings = np.random.normal(mean_rating, 1, size=num_ratings)
    # Clip the ratings to the range of 0 to 10
    ratings = np.clip(ratings, 0, 10)
    for user, rating in zip(users, ratings):
        rating_rounded = rating / 2
        if rating_rounded % 1 < 0.45:
            rating_rounded = int(rating_rounded)
        elif rating_rounded % 1 > 0.55:
            rating_rounded = int(rating_rounded) + 1
        elif rating_rounded % 1 > 0.45 and rating_rounded % 1 < 0.55:
            rating_rounded = round(rating_rounded * 2) / 2
        else:
            rating_rounded = 0
        matrix[user, game_index] = rating_rounded
        user_counts[user] += 1
    if np.max(user_counts) >= 300:
        break

# convert the matrix to a dataframe
game_names = df['Name'].unique()
matrix_df = pd.DataFrame(matrix, columns=game_names)
matrix_df.index += 1 
matrix_df.insert(0, 'users', range(1, 672))

matrix_df.to_csv('vg_user_item.csv', index=False)
