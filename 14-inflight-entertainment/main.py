def two_movies_sum_length(flight_length, movie_lengths):
    number_of_movies = len(movie_lengths)

    for length_index in range(0, number_of_movies):
        length = movie_lengths[length_index]
        for next_length_index in range(length_index+1, number_of_movies):
            next_length = movie_lengths[next_length_index]
            if (length + next_length) == flight_length: return True

    return False