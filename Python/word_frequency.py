from collections import Counter
import string

def word_frequency(filename):
    # open and read the content of the file
    with open(filename, 'r') as file:
        text = file.read()

    # convert text to lowercase to make it case-insensitive
    text = text.lower()

    # remove punctuation using translate and string.punctuation
    text.translate(str.maketrans('', '', string.punctuation))

    #  split the text into words
    words = text.split()

    # count the frequency of each word
    word_counts = Counter(words)

    return word_counts

# prompt user to input filename
filename = input("Please enter filename: ")

# print the word frequency dictionary
print(word_frequency(filename))