from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import recommender
import pandas as pd

app = Flask(__name__)
CORS(app)

# return the user's favorite movies and games
@app.route('/favorites', methods=['POST'])
def getUserInfo():
    # read in the csv files
    vg_ratings_df = pd.read_csv('vg_ratings.csv')
    movie_ratings_df = pd.read_csv('movie_ratings.csv')

    # extract the first 10 movies and video games that the user has rated
    user_id = 1  # replace with the ID of the desired user
    n_items = 5

    user_vg_ratings = vg_ratings_df.loc[vg_ratings_df['users'] == user_id].iloc[:, 1:]
    user_vg_ratings = user_vg_ratings.loc[:, (user_vg_ratings != 0).any(axis=0)].iloc[:, :n_items]
    vg_names = user_vg_ratings.columns.tolist()

    user_movie_ratings = movie_ratings_df.loc[movie_ratings_df['users'] == user_id].iloc[:, 1:]
    user_movie_ratings = user_movie_ratings.loc[:, (user_movie_ratings != 0).any(axis=0)].iloc[:, :n_items]
    movie_titles = user_movie_ratings.columns.tolist()
    response = {"games": vg_names, "movies": movie_titles}

    return jsonify(response), 200

# return game recommendations for a given movie
@app.route('/recommend', methods=['POST'])
def recommend():
    # if not isinstance(movie, str) or not movie:
    #     return False
    title = ""
    isGame = request.json["isGame"]
    recList = []
    if isGame:
        title = request.json["game"]
        print(title)
        recList = recommender.recommend_video_games_for_movie(title, 832)
    else:
        title = request.json["movie"]
        print(title)
        recList = recommender.recommend_movies_for_video_game(title, 832)

    response = {"recs": recList}
    
    return jsonify(response), 200

# # return movie recommendations for a given game
# @app.route('/recommendMovies', methods=['POST'])
# def recommendMovies():
#     # if not isinstance(movie, str) or not movie:
#     #     return False
#     game = request.json["game"]
#     print(game)
#     recList = recommender2.recommend_movies_for_video_game(game)
#     response = {"recs": recList}
    
#     return jsonify(response), 200


if __name__ == '__main__':
   port = 5000
   app.run(host='0.0.0.0', port=port, debug=True )