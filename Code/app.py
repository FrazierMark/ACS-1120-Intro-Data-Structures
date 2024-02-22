"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov_chain2 import SecondOrderMarkovChain

app = Flask(__name__)

markov_chain = SecondOrderMarkovChain("./data/corpus.txt")
max_length = 11

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    new_text = markov_chain.generate_text(max_length)
    return render_template("index.html", sentence=new_text)


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