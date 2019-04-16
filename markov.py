"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as opened_file:
        return opened_file.read()
    

text_string = open_and_read_file("green-eggs.txt")

def make_chains(text_string):
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

    for i in range(len(text_list) - 1):

        key_tuple = (text_list[i], text_list[i + 1])

        if i == len(text_list) - 2:
            pass
        else:
            chains[key_tuple] = chains.get(key_tuple, [])
            chains[key_tuple].append(text_list[i + 2])


    return chains

# print(make_chains(text_string))


def make_text(chains):
    """Return text from chains."""

    # randomly choose a key_tuple from dict

    # randomly pick a word in the list of key_tuple
    words = []

    keys_list = [key for key in chains.keys()]
    word_pair = choice(keys_list)
    words.extend([word_pair[0], word_pair[1]])

    while True:
        try:
            random_word = choice(chains[word_pair])
            words.append(random_word)
            word_pair = (word_pair[1], random_word)

        except KeyError:
            break


    return " ".join(words)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
