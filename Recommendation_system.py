import numpy as np

# Define the user-item matrix
user_item_matrix = np.array([
    [5, 3, 0, 0, 0],
    [0, 4, 5, 0, 0],
    [0, 7, 0, 2, 4],
    [2, 0, 0, 1, 0],
    [0, 0, 0, 0, 4]
])

# Define the number of latent factors
num_factors = 2

# Perform SVD on the user-item matrix
U, sigma, Vt = np.linalg.svd(user_item_matrix)

# Reduce the dimensionality of the user and item matrices
U_reduced = U[:, :num_factors]
Vt_reduced = Vt[:num_factors, :]

# Define a function to get the top-N recommended items for a user
def get_recommendations(user_id, num_recommendations):
    # Get the user's latent factors
    user_factors = U_reduced[user_id, :]
    
    # Calculate the dot product of the user's latent factors and the item latent factors
    scores = np.dot(user_factors, Vt_reduced)
    
    # Get the top-N recommended items
    recommended_items = np.argsort(-scores)[:num_recommendations]
    
    return recommended_items

# Test the recommendation system
user_id = 0
num_recommendations = 3
recommended_items = get_recommendations(user_id, num_recommendations)
print("Recommended items for user", user_id, ":", recommended_items)