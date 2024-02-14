"""Main script, uses other modules to generate sentences."""
from flask import Flask
from sample import return_random_word
from histogram import histogram

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
new_histogram = histogram('source_text.txt')

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    
    random_word = return_random_word(new_histogram)
    return f"<p>RANDOM WORD: {random_word}</p>"


# if __name__ == "__main__":
#     """To run the Flask server, execute `python app.py` in your terminal.
#        To learn more about Flask's DEBUG mode, visit
#        https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
#     app.run(debug=True)


# if __name__ == '__main__':
#     app.config['ENV'] = 'development'
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)