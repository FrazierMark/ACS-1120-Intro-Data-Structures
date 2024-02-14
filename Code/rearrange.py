import random

quote_from_user = input("Enter a quote: ")

quote_array = quote_from_user.split(" ")
random.shuffle(quote_array)
new_quote = " ".join(quote_array)
print(new_quote)