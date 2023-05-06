import numpy as np
import pandas as pd
from sklearn.decomposition import NMF

# load the video game and movie user-item matrices
vg_data = pd.read_csv('vg_user_item.csv')
movie_data = pd.read_csv('movie_user_item.csv')

merged_data = pd.merge(vg_data, movie_data, on='users')

# aggregate the user-item matrices by summing the two matrices
aggregated_matrix = np.zeros((len(vg_data), len(vg_data.columns) + len(movie_data.columns)-1))
aggregated_matrix[:,:len(vg_data.columns)] = vg_data.values
aggregated_matrix[:,len(vg_data.columns):] = movie_data.iloc[:,1:].values

# replace NaN values with zeros
aggregated_matrix = np.nan_to_num(aggregated_matrix)

# use matrix factorization (NMF) to provide recommendations
nmf_model = NMF(n_components=10, init='random', random_state=0)
W = nmf_model.fit_transform(aggregated_matrix)
H = nmf_model.components_

# video game and movie titles
vg_titles = list(vg_data.columns)[1:]
movie_titles = list(movie_data.columns)[1:]

# give the top 8 recs 
def recommend(userId=1):
    user_recommendations = np.dot(W[userId], H)
    user_vg_recommendations = user_recommendations[:len(vg_titles)]
    user_movie_recommendations = user_recommendations[len(vg_titles):]
    vg_top_indices = np.argsort(user_vg_recommendations)[::-1][:8]
    movie_top_indices = np.argsort(user_movie_recommendations)[::-1][:8]
    vg_top_recommendations = [vg_titles[idx] for idx in vg_top_indices]
    movie_top_recommendations = [movie_titles[idx] for idx in movie_top_indices]
    return vg_top_recommendations, movie_top_recommendations

# vg, movies = recommend(5)
# print(vg)
# print(movies)
