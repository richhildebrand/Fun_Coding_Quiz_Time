def find_rotation_point(list_of_words):
    rotation_point = None
    steps_to_find = 0

    first_word = list_of_words[0]
    min_index = -1
    max_index = len(list_of_words)
    while min_index+1 < max_index:
        steps_to_find += 1
        difference = max_index - min_index
        mid_point = min_index + (difference // 2)
        print('min:' + str(min_index) + '   max:' + str(max_index) + '   mid:' + str(mid_point))

        word = list_of_words[mid_point]
        if word < first_word: 
            max_index = mid_point
            rotation_point = mid_point
        elif word > first_word: min_index = mid_point
        elif word == first_word: return rotation_point, steps_to_find

    if rotation_point == None: rotation_point = 0
    return rotation_point, steps_to_find

def first_word_is_first_alphabetically(word_one, word_two):
    return word_one < word_two

    
