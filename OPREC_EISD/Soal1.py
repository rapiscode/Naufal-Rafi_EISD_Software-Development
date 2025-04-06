ratings_list = [
    [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0], 
    [5, 4, 2.5, 5, 3.6, 1.1, 3.6, 4, 4.2, 1.5]
]

for ratings in ratings_list:
    min_rating = min(ratings)
    max_rating = max(ratings)
    avg_rating = sum(ratings) / len(ratings)

    def clean(n):
        return int(n) if n.is_integer() else round(n, 1)

    min_rating = clean(min_rating)
    max_rating = clean(max_rating)
    avg_rating = clean(avg_rating)

    print([min_rating, max_rating, avg_rating])
