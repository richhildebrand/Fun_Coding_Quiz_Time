def two_movies_sum_length(flight_length, movie_lenghts):
    movie_times_available = set()

    for movie_length in movie_lenghts:
        difference = flight_length - movie_length
        if difference in movie_times_available: return True
        movie_times_available.add(movie_length)

    return False
