import random
import random

class SecondOrderMarkovChain:
    def __init__(self):
        # Empty dictionary to store Markov chain
        # Key: tuple of two previous words
        # Value: dictionary where key is next word and value is frequency
        self.chain = {}

    def add_text(self, text):
        words = text.split()
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

    def generate_text(self, length=10):
        # Select a random state (pair of two previous words) from the chain
        current_state = random.choice(list(self.chain.keys()))
        # Initialize list to store generated text, add the two previous words
        generated_text = list(current_state)

        for _ in range(length):
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

        return ' '.join(generated_text)

# Example usage:
# input_text = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
input_text = "I like dogs and you like dogs. I like cats but you hate cats."
markov = SecondOrderMarkovChain()
markov.add_text(input_text)

generated_text = markov.generate_text(length=20)
print(generated_text)