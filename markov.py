"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as opened_file:
        return opened_file.read()
    
text_string = open_and_read_file("the_cat.txt")

def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    #call open_file and split and save in new variable
    # loop through list using index so we can get pairs instead single word
    # keep track of each word and every word that follows
    # store those in a string
    # 

    chains = {}
    text_list = text_string.split()

    for i in range(len(text_list) - n):

        # key_tuple = (text_list[i], text_list[i + 1])
        key_tuple = tuple([text_list[j] for j in range(i, i+n)])

        chains[key_tuple] = chains.get(key_tuple, [])
        chains[key_tuple].append(text_list[i + n])


    return chains

# print(make_chains(text_string, 3))


def make_text(chains, n):
    """Return text from chains."""

    # randomly choose a key_tuple from dict

    # randomly pick a word in the list of key_tuple
    words = []

    keys_list = [key for key in chains.keys() if key[0][0].isupper()]
    word_group = choice(keys_list)
    list_group = list(word_group)
    words.extend(list_group)
    punct = ['.', '?', '!']

    # print(word_group)
    # print(words)

    while len(words) <= 50:
            random_word = choice(chains[word_group])
            words.append(random_word)
            if random_word[-1] in punct: 
                break                

            else:
                list_group = list_group[(-n+1)::]
                list_group.append(random_word)          
                word_group = tuple(list_group)



    return " ".join(words)



input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains, 4)

print(random_text)
