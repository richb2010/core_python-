"""Restaurant rating lister."""


from concurrent.futures import process


def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_text = open('score.text')

    score = {}

    for line in scores_text:
        line = line.rstrip()
        restaurant, score = line.split(":")
        score[restaurant] = int(score)

    return score


def add_restaurant(scores):
    """Add a restaurant and rating."""

    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Restaurant name>")
    rating = int(input("Rating> "))

    scores[restaurant] = rating 


def print_sorted_scores(scores):
    """Print restaurant and ratings, sorted. """

    for restaurant, rating in sorted(scores.items()):
          print(f"{restaurant} is rated at {rating}.")


# read existing scores in from file 
scores = process_scores()

# allow user to add a restaurant/rating pair
add_restaurant(scores)

# print an alphabetical list of all rated restaurant and their ratings 
print_sorted_scores(scores)
  



