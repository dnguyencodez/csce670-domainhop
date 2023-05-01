import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
# nltk.download('averaged_perceptron_tagger')
# load video game and movie data
vg_df = pd.read_csv('cleaned_video_games.csv').dropna(subset=['description'])
m_df = pd.read_csv('cleaned_movies.csv').dropna(subset=['description'])
# print(vg_df.shape, m_df.shape)
def tokenize(text):
    tokens = word_tokenize(text.lower())
    # Remove punctuation and numbers
    table = str.maketrans('', '', string.punctuation + string.digits)
    tokens = [token.translate(table) for token in tokens]
    # Remove words that are only 1 or 2 characters long
    tokens = [token for token in tokens if len(token) > 2]
    return tokens

# Create a lemmatizer function
def lemmatize(token):
    lemma = WordNetLemmatizer().lemmatize(token, get_wordnet_pos(token))
    return lemma

# Define a function to get the WordNet part of speech (POS) tag for a given token
def get_wordnet_pos(token):
    # Map POS tag to first character used by WordNetLemmatizer
    tag = nltk.pos_tag([token])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN) # default to NOUN if tag is not found

# Apply the tokenizer and lemmatizer functions to the description columns in the dataframes
# vg_df['description'] = vg_df['description'].apply(lambda x: ' '.join([lemmatize(token) for token in tokenize(x)]))
# m_df['description'] = m_df['description'].apply(lambda x: ' '.join([lemmatize(token) for token in tokenize(x)]))

# create a combined dataframe with only the relevant columns
combined_df = pd.concat([vg_df[['Name', 'description']], m_df[['title', 'description']]])

# create a TfidfVectorizer and fit_transform the description column of the combined dataframe
vectorizer = TfidfVectorizer()
desc_matrix = vectorizer.fit_transform(combined_df['description'])

# calculate the cosine similarity matrix
cos_sim_matrix = cosine_similarity(desc_matrix)

# define a function to recommend video games for a given movie
def recommend_video_games_for_movie(movie_title, k=10):
    # get the index of the movie in the m_df dataframe
    movie_index = m_df.index[m_df['title'] == movie_title][0]
    # get the top k similar video games to the movie
    similar_video_games_indices = cos_sim_matrix[movie_index].argsort()[::-1]
    similar_video_games_indices = similar_video_games_indices[similar_video_games_indices < vg_df.shape[0]]
    # similar_video_games_indices = similar_video_games_indices[:k]
    # return the names of the similar video games
    similar_video_games = list(set(vg_df.iloc[similar_video_games_indices]['Name'].tolist()))[:k]
    print(len(similar_video_games))
    return similar_video_games

# define a function to recommend movies for a given video game
def recommend_movies_for_video_game(vg_name, k=10):
    # get the index of the video game in the vg_df dataframe
    vg_index = vg_df.index[vg_df['Name'] == vg_name][0]
    # get the top k similar movies to the video game
    similar_movies_indices = cos_sim_matrix[vg_index].argsort()[::-1]
    similar_movies_indices = similar_movies_indices[similar_movies_indices < m_df.shape[0]]
    # similar_movies_indices = similar_movies_indices[:k]
    # return the titles of the similar movies
    # similar_movies = list(set(vg_df.iloc[similar_video_games_indices]['Name'].tolist()))[:k]
    similar_movies = list(set(m_df.iloc[similar_movies_indices]['title'].tolist()))[:k]
    return similar_movies


# print(recommend_video_games_for_movie("Alice in Wonderland (2010)"))
# print(recommend_movies_for_video_game("NBA Jam"))