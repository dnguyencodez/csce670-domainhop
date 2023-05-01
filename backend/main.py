from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import recommender2

app = Flask(__name__)
CORS(app)

# return the user's favorite movies and games
@app.route('/favorites', methods=['POST'])
def getUserInfo():
    # read json file
    f = open('userInfo.json')
    data = json.load(f)
    response = data["1"]

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
        recList = recommender2.recommend_video_games_for_movie(title)
    else:
        title = request.json["movie"]
        print(title)
        recList = recommender2.recommend_movies_for_video_game(title)

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