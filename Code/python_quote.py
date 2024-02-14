import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!",
          "The purpose of our lives is to be happy.",
          "Life is what happens when you're busy making other plans.",
          "Get busy living or get busy dying.",
          "You only live once, but if you do it right, once is enough.",
          "Many of life's failures are people who did not realize how close they were to success when they gave up.",
          "If you want to live a happy life, tie it to a goal, not to people or things.",
          "Never let the fear of striking out keep you from playing the game.",
          "Money and success don't change people; they merely amplify what is already there.")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)