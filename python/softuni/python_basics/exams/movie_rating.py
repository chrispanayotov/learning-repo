import sys
n_movies = int(input())

max_movie = None
max_rating = -sys.maxsize-1
min_movie = None
min_rating = sys.maxsize
avg_rating = 0

for i in range(n_movies):
    movie = input()
    rating = float(input())

    if rating > max_rating:
        max_movie = movie
        max_rating = rating
    if rating < min_rating:
        min_movie = movie
        min_rating = rating

    avg_rating += rating

print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating / n_movies:.1f}")