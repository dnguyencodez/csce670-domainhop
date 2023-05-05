import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# load video game and movie data
vg_df = pd.read_csv('cleaned_video_games.csv').dropna(subset=['description'])
m_df = pd.read_csv('cleaned_movies.csv').dropna(subset=['description'])

# load ratings data
vg_ratings_df = pd.read_csv('vg_user_item.csv')
m_ratings_df = pd.read_csv('movie_user_item.csv')
# print(vg_ratings_df.columns)
# print(m_ratings_df.columns)

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
# vg_df['description'] = vg_df['description'].apply(lambda x: ' '.join([lemmatize(token) for token in word_tokenize(x.lower()) if token not in string.punctuation]))
# m_df['description'] = m_df['description'].apply(lambda x: ' '.join([lemmatize(token) for token in word_tokenize(x.lower()) if token not in string.punctuation]))

# create a combined dataframe with only the relevant columns
combined_df = pd.concat([vg_df[['Name', 'description']], m_df[['title', 'description']]])

# create a TfidfVectorizer and fit_transform the description column of the combined dataframe
vectorizer = TfidfVectorizer()
desc_matrix = vectorizer.fit_transform(combined_df['description'])

# create a ratings matrix with users as rows and video games and movies as columns
ratings = pd.concat([vg_ratings_df, m_ratings_df], axis=1)

# normalize the ratings
mean_rating = ratings.mean(axis=1)
ratings = ratings.sub(mean_rating, axis=0)
ratings = ratings.fillna(0)

# calculate the cosine similarity matrix using both description and ratings
desc_cos_sim_matrix = cosine_similarity(desc_matrix)
ratings_cos_sim_matrix = cosine_similarity(ratings)

def recommend_video_games_for_movie(movie_title, user_id, k=10):
    user_ratings = vg_ratings_df[vg_ratings_df['users'] == user_id]
    # get the index of the movie in the m_df dataframe
    movie_index = m_df.index[m_df['title'] == movie_title][0]
    # get the top k similar video games to the movie
    similar_video_games_indices = desc_cos_sim_matrix[movie_index].argsort()[::-1]
    similar_video_games_indices = similar_video_games_indices[similar_video_games_indices < vg_df.shape[0]]
    
    # # filter out the video games the user has already rated
    # rated_video_games = list(user_ratings[user_ratings.columns.intersection(vg_df['Name'])].dropna(axis=1).columns)
    # similar_video_games_indices = [i for i in similar_video_games_indices if vg_df.iloc[i]['Name'] not in rated_video_games]
    
    # get the top k similar video games that the user has not rated
    similar_video_games = list(set(vg_df.iloc[similar_video_games_indices]['Name'].tolist()))[:k]
    return similar_video_games


# define a function to recommend movies for a given video game
def recommend_movies_for_video_game(vg_name, user_id, k=10):
    user_ratings = m_ratings_df[m_ratings_df['users'] == user_id]
    # get the index of the video game in the m_df dataframe
    vg_index = vg_df.index[vg_df['Name'] == vg_name][0]
    # get the top k similar movies to the movie
    similar_movies_indices = desc_cos_sim_matrix[vg_index].argsort()[::-1]
    similar_movies_indices = similar_movies_indices[similar_movies_indices < m_df.shape[0]]
    
    # # filter out the movies the user has already rated
    # rated_movies = list(user_ratings[user_ratings.columns.intersection(m_df['title'])].dropna(axis=1).columns)
    # similar_movies_indices = [i for i in similar_movies_indices if m_df.iloc[i]['title'] not in rated_movies]
    
    # get the top k similar movies that the user has not rated
    similar_movies = list(set(m_df.iloc[similar_movies_indices]['title'].tolist()))[:k]
    return similar_movies


# print(recommend_movies_for_video_game("NBA Jam", 1))
# print(recommend_video_games_for_movie("Happy Gilmore (1996)", 1))