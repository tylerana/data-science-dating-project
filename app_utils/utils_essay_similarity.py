import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import ast
warnings.filterwarnings('ignore')

def score_profiles(user_embedding, final_df, num_of_matches):
    similarity_results = []
    user_embedding = np.array(user_embedding)
    
    try:
        dtype = final_df['bert_embeddings'].dtype
        if dtype == 'object':
            final_df['bert_embeddings'] = final_df['bert_embeddings'].apply(ast.literal_eval)
    except Exception as e:
        print("Error converting embeddings:", e)
        
    for index, row in final_df.iterrows():
        
        match_embedding = np.array(row["bert_embeddings"])     

        cos_similarity = cosine_similarity(user_embedding.reshape(1, -1), match_embedding.reshape(1, -1))  # compute cosine similarity
        similarity = float(cos_similarity[0][0])

        similarity_results.append((index, similarity))
        
    top_matches = sorted(similarity_results, key=lambda x: x[1], reverse=True)[:num_of_matches]
    
    top_indices = [idx for idx, _ in top_matches]
    top_scores = [score for _, score in top_matches]
    top_profiles = final_df.loc[top_indices].copy()
    top_profiles["similarity_score"] = top_scores
        
    return top_profiles