import random
import re

class SecondOrderMarkovChain:
    def __init__(self, source_text):
        # Empty dictionary to store Markov chain
        # Key: tuple of two previous words
        # Value: dictionary where key is next word and value is frequency
        self.source_text = self.compile_source_text(source_text)
        self.chain = {}
        
    def compile_source_text(self, source_text):
      with open(str(source_text)) as file:
        
      # Define a regex pattern to remove punctuation (except apostrophe)
        pattern = re.compile(r'[^\w\'_]')
        text = file.read()
        
        all_words_without_punctuations = re.sub(pattern, ' ', text)
        all_words = all_words_without_punctuations.lower().split()
      return all_words

    def add_text(self):
        words = self.source_text
        for i in range(len(words) - 2):  # Iterate until the second last word
            # Access the current word, next word, and the word after next
            current_word = words[i]
            next_word = words[i + 1]
            next_next_word = words[i + 2]

            # Create a tuple of two previous words
            current_state = (current_word, next_word)

            # If the current state is not in the chain, add it
            if current_state not in self.chain:
                self.chain[current_state] = {}

            # If the next word is not in the current state's dictionary, add it
            if next_next_word not in self.chain[current_state]:
                self.chain[current_state][next_next_word] = 0

            # Increment the frequency of the next next word
            self.chain[current_state][next_next_word] += 1

    def generate_text(self, maxLength=15):
        # Build Markov Chain
        self.add_text()
        # Select a random state (pair of two previous words) from the chain
        current_state = random.choice(list(self.chain.keys()))
        # Initialize list to store generated text, add the two previous words
        generated_text = list(current_state)

        for _ in range(maxLength):
            # If the current state is in the chain
            if current_state in self.chain:
                # Get the dictionary of next words and their frequencies for the current state
                next_words = self.chain[current_state]
                # Choose a random next word based on the frequencies
                next_word = random.choices(list(next_words.keys()), weights=list(next_words.values()))[0]
                # Add the next word to the generated text
                generated_text.append(next_word)
                # Update the current state by shifting the previous words and adding the next word
                current_state = (current_state[1], next_word)
            else:
                break
        
        generated_text = [word.capitalize() if i == 0 else word for i, word in enumerate(generated_text)]

        return ' '.join(generated_text)+'.'
