import pandas as pd
import requests

# preprocess video games
games = pd.read_csv('./datasets/Video_Game_Sales_as_of_Jan_2017.csv')
print(games['Year_of_Release'].value_counts())
# drop rows with missing User_score values
# games = games.dropna(subset=['User_Score'])

# # drop unnecessary columns
# games = games.drop(['Platform', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Count', 'Rating'], axis=1)
# games = games.iloc[:20]
# print(games.info())

# # Set the access token and client ID as variables
# access_token = 'v5amu75qdq7jfl4sramd9xs2l8w9fp'
# client_id = 'lp388twgy0wkc9ffle68laajiwiogy'
# # Set the endpoint and query parameters for the API request
# url = 'https://api.igdb.com/v4/games'
# # Set the headers for the API request, including the access token and client ID
# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Client-ID': client_id,
#     'Accept': 'application/json'
# }
# print(games.shape[0])
# val = [0]

# def getDescription(name: str):
#     query = f'fields summary, storyline; search "{name}";'

#     # Make the API request and get the response data
#     response = requests.post(url, headers=headers, data=query)
#     game_data = response.json()
#     val[0] += 1
#     text = ""
#     if not game_data or not game_data[0]: return text
#     if "summary" in game_data[0]: text += game_data[0]["summary"] + " "
#     if "storyline" in game_data[0]: text += game_data[0]["storyline"]
#     if val[0] % 100 == 0: print(val, text)
#     return text
    
# games["description"] = games.apply(lambda row: getDescription(row['Name']), axis=1)

# games.to_csv('cleaned_video_games.csv', index=False)


# # preprocess movies
# # movies = pd.read_csv('./datasets/movies.csv')
# # ratings = pd.read_csv('./datasets/ratings.csv')

# # # find each movieId's avg rating
# # avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()

# # # combine the movies.csv and ratings.csv files, excluding the timestamp columns (bc movies.csv has genres and ratings.csv has ratings, userId, and timestamp)
# # merged_data = pd.merge(movies, avg_ratings, on='movieId', how='inner')
# # merged_data = merged_data.drop(['movieId', 'rating'], axis=1)
# # merged_data.to_csv('cleaned_movies.csv', index=False)