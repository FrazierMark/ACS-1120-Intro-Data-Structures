import random

class MarkovChain:
    def __init__(self):
      # Empty dictionary to store markov chain
      # Key == word
      # Value == list of words that follow the key-word
      self.chain = {}

    def add_text(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            # Access the current word and next word
            current_word = words[i]
            next_word = words[i + 1]
            # If the current word is not in the chain, add it
            if current_word not in self.chain:
                # Add the current word to the chain, set value to empty list
                self.chain[current_word] = []
            # Append the next word to the list of words that follow the current word
            self.chain[current_word].append(next_word)
        print(self.chain)

    def generate_text(self, length=100):
        # Select random word from the chain
        current_word = random.choice(list(self.chain.keys()))
        # initialize list to store generated text, add the first(random) word
        generated_text = [current_word]
        for _ in range(length):
            # check if the current word is in the chain (it's possible after updating current word,
            # it may not be in the chain, because it is likley a value in the chain, not a key)
            if current_word in self.chain:
                # randomly selects the next word from the array of self.chain[current_word] 
                next_word = random.choice(self.chain[current_word])
                # add the next word to the generated text
                generated_text.append(next_word)
                # update the current word to the next word
                current_word = next_word
            else:
                break
        return ' '.join(generated_text)


# Example usage:
input_text = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
markov = MarkovChain()
markov.add_text(input_text)

generated_text = markov.generate_text(length=20)
print(generated_text)