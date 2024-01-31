import random

dictionary = open("/usr/share/dict/words", "r")
dictionary_list = dictionary.readlines()
dictionary.close()

random_words = []
number_of_words = int(input("How many words would you like? "))

def random_word():
  for i in range(number_of_words):
    random_word = random.choice(dictionary_list).strip()
    random_words.append(random_word)
  
  random_words_string = " ".join(random_words)
  return random_words_string

print(random_word())