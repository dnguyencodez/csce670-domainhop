import pandas as pd
import numpy as np
from sklearn.decomposition import NMF

# Define the genre mapping dictionary
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

vg_df = pd.read_csv('cleaned_video_games.csv', index_col=0)
m_df = pd.read_csv('cleaned_movies.csv', index_col=0)

# variable to rate only 70% of items for each user (i'm randomly generating ratings)
pct_rated = 0.7

# intial user-item matrices
vg_ratings = np.zeros((5000, len(vg_df)))
m_ratings = np.zeros((5000, len(m_df)))
# print(vg_ratings)

# generate random ratings for random items
for i in range(5000):
    vg_cols = np.random.choice(vg_df.index, size=int(len(vg_df) * pct_rated), replace=False)
    m_cols = np.random.choice(m_df.index, size=int(len(m_df) * pct_rated), replace=False)
    for col in vg_cols:
        vg_ratings[i][vg_df.index.get_loc(col)] = np.random.randint(1, 6)
    for col in m_cols:
        m_ratings[i][m_df.index.get_loc(col)] = np.random.randint(1, 6)

# update genre mappings
for index, row in m_df.iterrows():
    genres = row['Genre'].split('|')
    mapped_genres = set()
    for genre in genres:
        if genre in genre_mapping:
            mapped_genres.update(genre_mapping[genre])
            # print(mapped_genres)
    for genre in mapped_genres:
        m_df.at[index, genre] = 1

m_df.drop(columns=['Genre'], inplace=True)

# finalize user-item matrices
vg_matrix = pd.DataFrame(vg_ratings, columns=vg_df['Title'], dtype=np.float64)
# print(vg_matrix)
m_matrix = m_df.drop(columns=['Title']).astype(np.float64)
m_matrix.columns = m_df['Title']

# make the aggregated matrix
combined_matrix = pd.concat([vg_matrix, m_matrix], axis=1)

# matrix factorization using NMF
model = NMF(n_components=50, init='random', random_state=0)
W = model.fit_transform(combined_matrix)
H = model.components_

# give the recommendations
vg_pref = pd.DataFrame(W[:, :len(vg_df)], index=combined_matrix.index)
vg_recommendations = pd.DataFrame(np.dot(vg_pref.loc[5000], H[len(vg_df):, :]), index=m_matrix.columns, columns=['Score'])
vg_recommendations.sort_values('Score', ascending=False, inplace=True)
top_vg_recommendations = vg_recommendations.head(10)

