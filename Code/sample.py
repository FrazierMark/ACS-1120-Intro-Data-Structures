from histogram import histogram
import random

# Function takes a histogram
# and returns a random word from the histogram dictionary
# words with a higher occurrence, will more likely be selected
def return_random_word(histogram):
  weighted_words = []
  for word, count in histogram.items():
      weighted_words.extend([word] * count)
  random_word = random.choice(weighted_words)
  print(random_word)
  return random_word

# Testing
new_histogram = histogram('source_text.txt')

return_random_word(new_histogram)