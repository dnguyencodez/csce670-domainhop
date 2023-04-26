import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# genre mapping from uniqueGenres.txt
genre_mapping = {
    'Adventure': ['Adventure', 'Role-Playing'],
    'Animation': ['Platform', 'Adventure'],
    'Children': ['Platform'],
    'Comedy': ['Misc'],
    'Fantasy': ['Adventure', 'Role-Playing'],
    'Romance': ['Simulation'],
    'Drama': ['Action', 'Adventure', 'Strategy', 'Role-Playing'],
    'Action': ['Action', 'Shooter'],
    'Crime': ['Action', 'Strategy'],
    'Thriller': ['Action', 'Shooter'],
    'Horror': ['Horror'],
    'Mystery': ['Puzzle'],
    'Sci-Fi': ['Action', 'Shooter', 'Simulation'],
    'Documentary': ['Simulation'],
    'IMAX': ['Misc'],
    'War': ['Strategy'],
    'Musical': ['Music', 'Misc'],
    'Western': ['Adventure', 'Shooter', 'Fighting', 'Misc'],
    'Film-Noir': ['Misc'],
    '(no genres listed)': ['Misc']
}

movies = pd.read_csv('cleaned_movies.csv')
games = pd.read_csv('cleaned_video_games.csv')

# print(movies.columns)
# print('----------------')
# print(games.columns)

# make a column in movies using the mapped genres
movies['MappedGenre'] = movies['Genre'].apply(lambda x: next((k for k, v in genre_mapping.items() if any(g in v for g in x.split('|'))), '(no genres listed)'))

# make a column in games using the mapped genres
games['MappedGenre'] = games['Genre'].apply(lambda x: next((k for k, v in genre_mapping.items() if x in v), '(no genres listed)'))

# merge movies and games using the mapped genres
merged_data = pd.merge(movies, games, on='MappedGenre', how='outer')

# print(merged_data.columns)

# combine genres and ratings into one column (similar to aggregate matrix from here https://recsys.acm.org/wp-content/uploads/2014/10/recsys2014-tutorial-cross_domain.pdf)
features = ['MappedGenre', 'rating_x', 'rating_y']
merged_data['combined_features'] = merged_data[features].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

# extract features (ratings and genres)
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(merged_data['combined_features'])

# compute the similarity
item_similarities = cosine_similarity(feature_matrix)

def get_top_similar_items(item_id, item_similarities, N=5):
    all_items = list(merged_data.index)
    # get similarity scores for the specified item
    item_scores = list(enumerate(item_similarities[item_id]))
    item_scores = sorted(item_scores, key=lambda x: x[1], reverse=True)
    top_items = [i for i, s in item_scores[1:N+1]]
    return merged_data.iloc[top_items]

# testing with the first movie --> code runs forever tho!
print(get_top_similar_items(0, item_similarities, N=10))
