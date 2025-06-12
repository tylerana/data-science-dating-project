# matching based on essays
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import gower 

def get_essay_matches(user_index, df, top_n):
  similarity_results = []

  user = df.iloc[user_index][-1]
  user_embedding = np.array(user)

  for i, x in enumerate(range(len(df))):
    if x != user_index:
      user_B = df.iloc[x][-1]
      match_embedding = np.array(user_B)         # get the second user's embedding

      cos_similarity = cosine_similarity(user_embedding.reshape(1, -1), match_embedding.reshape(1, -1))  # compute cosine similarity
      similarity = float(cos_similarity[0][0])

      similarity_results.append((df.index[x], similarity))
  top_matches = sorted(similarity_results, key=lambda x: x[1], reverse=True)[:top_n]
  return top_matches


# matching based on lifestyle
def get_lifestyle_matches(user_index, df, top_n):
  # creating a list to return the matches
  lifestyle_matches = []

  # getting users lifestyle choices
  user = df.iloc[[user_index]]

  # dropping to prevent user from matching with self
  df = df.drop(index=user_index)
  df["original_index"] = df.index
  df = df.reset_index(drop=True)

  # re-aligning columns
  user = user[df.drop(columns="original_index").columns]

  user_distance = gower.gower_matrix(user, df.drop(columns="original_index"))
  similarity = 1 - user_distance

  for i in range(len(df)):
    score = float(similarity[0][i])
    user_id = df["original_index"][i]
    lifestyle_matches.append((user_id, score))

  top_matches = sorted(lifestyle_matches, key=lambda x: x[1], reverse=True)[:top_n]

  return top_matches

# blended score
def get_matches(user_index, df, df_gowers, essay_weight, lifestyle_weight, filtered_user_indices):

  blended_score = []

  # get essay matching score
  essay_matches = get_essay_matches(user_index, df)  # gives us the (user_id, essay score)

  # get lifestyle matching score
  lifestyle_matches = get_lifestyle_matches(user_index, df_gowers)   # gives us the (user_id, lifestyle score)

  #essay table
  essay_dict = dict(essay_matches)
  lifestyle_dict = dict(lifestyle_matches)

  # getting keys
  keys = filtered_user_indices

  for user_index in keys:
    essay = essay_dict.get(user_index, 0.0)
    lifestyle = lifestyle_dict.get(user_index, 0.0)
    final = (essay * essay_weight) + (lifestyle * lifestyle_weight)
    blended_score.append((user_index, final))

  top_matches = sorted(blended_score, key=lambda x: x[1], reverse=True)
  return top_matches

def filter_user_profiles(df, preferred_min_age, preferred_max_age, preferred_locations, preferred_orientations):
    filtered_df = df[
        (df["age"] >= preferred_min_age) &
        (df["age"] <= preferred_max_age) &
        (df["location"].isin(preferred_locations)) &
        (df["orientation"].isin(preferred_orientations))
    ]
    return filtered_df
