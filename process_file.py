# def find_occurences_count(text = input("enter text to look up ")):                        #counts the occurences of text in a file
#     my_lines = []
#     with open(input("input file name to open "), 'r') as file_variable:
#         for my_line in file_variable:
#             my_lines.append(my_line.rstrip('\n'))

#     x = (sum(text in s for s in my_lines))
#     print(x)

# find_occurences_count()

def list_of_items_desired(text = input("enter text to look up ")):                      #finds the index of portions of a string in a file
    my_lines = []
    with open(input("Enter file name to open "), 'r') as file_variable:
        for my_line in file_variable:
            my_lines.append(my_line.rstrip('\n'))

    list_of_indexes = ([i for i, s in enumerate(my_lines) if text in s])
    print(list_of_indexes)

    list_of_items = []
    for i in list_of_indexes:
        list_of_items.append(my_lines[i])
    print(list_of_items)

    list_without_text = ([s.replace('X-DSPAM-Confidence:', '') for s in list_of_items])
    # print(list_without_text)

    list_of_float = list(map(float, list_without_text))
    # print(list_of_float)

    total = 0
    for i in list_of_float:
        total += i
    print("X-DSPAM-Confidence: ", total/len(list_of_float))

list_of_items_desired()