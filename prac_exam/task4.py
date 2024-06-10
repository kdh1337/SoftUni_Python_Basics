import sys

number_movies = int(input())
highest_rating = 0
lowest_rating = sys.maxsize
total_ratings = 0

for i in range (1, number_movies + 1):
    movie_name = input()
    movie_rating = float(input())
    total_ratings += movie_rating
    if movie_rating > highest_rating:
        highest_rated_movie = movie_name
        highest_rating = movie_rating
    if movie_rating < lowest_rating:
        lowest_rated_movie = movie_name
        lowest_rating = movie_rating

avg_rating = total_ratings / number_movies

print(f'{highest_rated_movie} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {avg_rating:.1f}')