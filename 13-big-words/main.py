def steps_to_rotation_point(ascDictionary):
    return 0

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