import doctest

eng_alphabet = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26
}

dictionary_of_nums = {}

# adding to dictionary
def add_to_dic(word):
    num_of_word = ""
    for i in range(len(word)):
        num_of_word = num_of_word + str(eng_alphabet[word[i]])

    if num_of_word in dictionary_of_nums:
        dictionary_of_nums[num_of_word] = dictionary_of_nums[num_of_word] + [word]
    else:
        dictionary_of_nums[num_of_word] = [word]
    #print(dictionary_of_nums)


def give_outputs_of(input_num_str):
    '''
    # testisg 1 word 'BYE'
    >>> add_to_dic('BYE')
    >>> give_outputs_of('2255')
    ['BYE']

    # testing 2 words 'BYE' and 'VEE' (with same number)
    >>> add_to_dic('VEE')
    >>> give_outputs_of('2255')
    ['BYE', 'VEE']

    # resetting and testing the exact words of original example
    >>> dictionary_of_nums = {}
    >>> add_to_dic('BOOK')
    >>> add_to_dic('CITY')
    >>> add_to_dic('FLOWER')
    >>> add_to_dic('GHFYT')
    >>> add_to_dic('BOOAA')
    >>> add_to_dic('BOOKS')
    >>> give_outputs_of('2151511')
    ['BOOK', 'BOOAA']
    '''

    if input_num_str in dictionary_of_nums:
        return dictionary_of_nums[input_num_str]
    else:
        return []

doctest.testmod(verbose=True)
