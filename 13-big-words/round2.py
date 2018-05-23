def find_rotation_point(list_of_words):
    mid_point = None
    steps_to_find = 0

    first_word = list_of_words[0]
    min_index = -1
    max_index = len(list_of_words)
    while min_index+1 < max_index:
        steps_to_find += 1
        difference = max_index - min_index
        mid_point = min_index + (difference // 2)

        word = list_of_words[mid_point]
        if word < first_word: max_index = mid_point
        if word > first_word: max_index = mid_point

    return mid_point, steps_to_find

    
