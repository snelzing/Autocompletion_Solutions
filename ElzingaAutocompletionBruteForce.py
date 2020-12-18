'''

The Brute Force method for solving the Autocompletion problem

'''

input = "Aa"

EXAMPLE_DICTIONARY = ['Aardvark', "A", "aarmory", "antler", "zoology", "orca", "orcas"]


def is_prefixed_by(prefix, dictionary):
    # processing the input
    lower_input = prefix.lower()
    lower_input_length = len(lower_input)

    sliced_word_list = []
    possible_completions = []

    # go through the dictionary
    for i in dictionary:
        lowercase_it = i.lower()
        lower_input_list = list(input.lower())

        word_slice = slice(lower_input_length)
        sliced_word_list = list(lowercase_it[word_slice])
        if sliced_word_list == lower_input_list:
            possible_completions.append(i)

    return possible_completions


print(f"here are are the autocomplete options for '{input}'")
print(is_prefixed_by(input, EXAMPLE_DICTIONARY))
