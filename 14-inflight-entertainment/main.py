def two_movies_sum_length(flight_length, movie_lengths):
    movie_times_available = set()

    for length in movie_lengths:
        matching_value = flight_length - length
        if matching_value in movie_times_available: return True
        else: movie_times_available.add(length)

    return False