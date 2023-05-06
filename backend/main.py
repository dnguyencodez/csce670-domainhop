from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import recommender
import pandas as pd
import mergePreferences

app = Flask(__name__)
CORS(app)

# return the user's favorite movies and games
@app.route('/favorites', methods=['POST'])
def getUserInfo():
    user = int(request.json["user"])
    print(user)
    vg_names, movie_titles = mergePreferences.recommend(user)

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
    user = int(request.json["user"])
    if isGame:
        title = request.json["game"]
        print(title)
        recList = recommender.recommend_video_games_for_movie(title, user)
    else:
        title = request.json["movie"]
        print(title)
        recList = recommender.recommend_movies_for_video_game(title, user)

    response = {"recs": recList}
    
    return jsonify(response), 200


if __name__ == '__main__':
   port = 5000
   app.run(host='0.0.0.0', port=port, debug=True )