import random
import string
import re

# Function takes a text/file argument
# and create a word_count dictionary

def histogram(file_name):
  with open(file_name, mode='r') as file:
      all_words = file.read().replace('\n', ' ')

  # Define a regex pattern to remove punctuation (except apostrophe)
  pattern = re.compile(r'[^\w\']')

  # Remove punctuation from the text
  all_words_without_punctuations = re.sub(pattern, ' ', all_words)
  words_list = all_words_without_punctuations.lower().split()
  histogram = {}
  for word in words_list:
      histogram[word] = histogram.get(word, 0) + 1
  return histogram


# Function takes a histogram and 
# returns the total count of unique words in the histogram
def unique_words(histogram):
  unique_words_count = 0
  for count in histogram.values():
    if count == 1:
      unique_words_count += 1
  print(unique_words_count)
  return unique_words_count

# Function takes a string and a histogram and 
# returns the amount of times the word is used
def frequency(word, histogram):
  if word.lower() in histogram.keys():
    print(histogram[word])
    return histogram[word]
  print(f"{word} does not appear in the text file.")


# Testing
# new_histogram = histogram('source_text.txt')
# unique_words(new_histogram)
# frequency('too,', new_histogram)


# return_random_word(new_histogram)