"""

The Prefix Map method for solving the Autocompletion problem


"""

EXAMPLE_LIST = ["Aardvark","A", "aarmory", "antler", "zoology", "orca", "orcas"]
fill_dictionary = {}

prefix = "aar"


def make_list(word):

        prefix_list = []
        ze_list = list(word)
        new_addition = ""
        for y in ze_list:
            counter = 0
            if prefix_list == []:
                new_addition = y
                prefix_list.append(new_addition)
                continue
            if not prefix_list == []:
                new_addition = prefix_list[counter-1] + y
                prefix_list.append(new_addition)
                counter = counter + 1
            
        return prefix_list

word_dict_of_dict = {}
for word in EXAMPLE_LIST:
    word = word.lower()
    word_dict = make_list(word)
    word_dict_of_dict[word] = word_dict

            
for extracted_dict in word_dict_of_dict:
    for z in word_dict_of_dict[extracted_dict]:
        if prefix == z:
            print(extracted_dict)

