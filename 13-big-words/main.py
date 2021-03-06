def first_word_is_first_alphabetically(first_word, second_word):
    first_word_letter_count = len(first_word)
    second_word_letter_count = len(second_word)

    index = 0
    while index < first_word_letter_count \
      and index < second_word_letter_count:

        if first_word[index] == second_word[index]: 
            index += 1
            continue

        return first_word[index] < second_word[index]

    return first_word_letter_count < second_word_letter_count


def find_rotation_point(ascWords):
    first_word = ascWords[0]
    min_index = 0
    max_index = len(ascWords) - 1

    step_count = 0
    mid_point = None
    while min_index < max_index:
        step_count += 1
        difference = max_index - min_index
        mid_point = (difference // 2) + min_index
        print('min_index:' + str(min_index) + '   mid_point:' + str(mid_point), '   max_index:' + str(max_index))

        word = ascWords[mid_point]
        if first_word_is_first_alphabetically(first_word, word):
            min_index = mid_point
        elif first_word_is_first_alphabetically(word, first_word):
            max_index = mid_point

        if min_index + 1 == max_index: 
            if first_word_is_first_alphabetically(first_word, ascWords[max_index]):
                return (0, step_count)
            else:
                return (max_index, step_count)

    return (mid_point, step_count)