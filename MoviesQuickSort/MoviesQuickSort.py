def quick_sort(movies):
    if len(movies) <= 1:
        return movies

    pivot = movies[len(movies) // 2]

    left = [m for m in movies if m[1] > pivot[1]]
    middle = [m for m in movies if m[1] == pivot[1]]
    right = [m for m in movies if m[1] < pivot[1]]

    return quick_sort(left) + middle + quick_sort(right)


movies = [
    ("Inception", 8.8),
    ("Interstellar", 8.6),
    ("Titanic", 7.9),
    ("Avatar", 7.8),
    ("The Dark Knight", 9.0)
]

sorted_movies = quick_sort(movies)

print("--- Top Rated Movies First ---")

for title, rating in sorted_movies:
    print(title, ":", rating)
