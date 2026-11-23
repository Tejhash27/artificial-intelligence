# Basic Recommendation System using Collaborative Filtering

# User ratings for different movies
ratings = {
    "User1": {
        "MovieA": 5,
        "MovieB": 4,
        "MovieC": 0,
        "MovieD": 0
    },

    "User2": {
        "MovieA": 5,
        "MovieB": 4,
        "MovieC": 4,
        "MovieD": 5
    },

    "User3": {
        "MovieA": 1,
        "MovieB": 2,
        "MovieC": 5,
        "MovieD": 4
    }
}

# Select the target user
target_user = "User1"

# Calculate similarity using common ratings
def similarity(user1, user2):
    common = []

    for movie in ratings[user1]:
        if ratings[user1][movie] > 0 and ratings[user2][movie] > 0:
            common.append(movie)

    if len(common) == 0:
        return 0

    difference = 0

    for movie in common:
        difference += abs(
            ratings[user1][movie] - ratings[user2][movie]
        )

    return 1 / (1 + difference / len(common))


# Find the most similar user
best_user = None
best_score = -1

for user in ratings:
    if user != target_user:
        score = similarity(target_user, user)

        if score > best_score:
            best_score = score
            best_user = user

# Recommend movies not watched by target user
recommendations = []

for movie in ratings[best_user]:
    if ratings[target_user][movie] == 0:
        recommendations.append(movie)

# Display results
print("COLLABORATIVE FILTERING")
print("-----------------------------")
print("Target User:", target_user)
print("Most Similar User:", best_user)
print("Similarity Score:", round(best_score, 2))

print("\nRecommended Movies:")

for movie in recommendations:
    print(movie)

print("-----------------------------")
print("Recommendation Completed Successfully!")
