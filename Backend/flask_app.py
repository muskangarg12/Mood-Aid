from flask import Flask, render_template, request, url_for, Markup
import os
import pandas as pd
import numpy as np
import json
from random import randrange

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# load quotes in memory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# declare global variable
quotes = None

@app.before_request
# first function
# loading the quotes and getting the sentiment score
def prepare_sentiment_quote_stash() :
    global quotes

    # load the quotes data
    quotes = pd.read_csv(os.path.join(BASE_DIR,'quotes.csv'))

    sid = SentimentIntensityAnalyzer()

    all_compounds = []
    for sentence in quotes['quote'] :
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss) :
            if (k == 'compound') :
                all_compounds.append(ss[k])

    # add sentiment to the data
    quotes['sentiment_score'] = all_compounds

    # create ladder index
    quotes = quotes.sort_values('sentiment_score')
    quotes['index'] = [ix for ix in range(0, len(quotes))]


# second function
# getting a quote according to sentiments
def gimme_a_quote(direction = None, current_index = None, max_index_value = 0) :
    rand_index = randrange(max_index_value)
    darker = None
    brighter = None

    # new session visit
    if current_index is None :
        brighter = rand_index

    if direction == 'brighter' :
        brighter = current_index
    else :
        darker = current_index

    if darker is not None :
        current_index = rand_index

        try :
            current_index = int(darker)
        except ValueError:
            # somebody is gaming the system
            current_index = rand_index

        if current_index > 0 :
            # try for a lesser value than current one
            rand_index = randrange(0, current_index)
            print('darker')
        else :
            # already at lowest point so assign a new random index
            rand_index = rand_index

    elif brighter is not None :

        try :
            current_index = int(brighter)
        except ValueError:
            # somebody is gaming the system
            current_index = rand_index

        if current_index < max_index_value - 1 :
            # try for a lesser value than current one
            rand_index = randrange(current_index, max_index_value)
            print('brighter')
        else :
            # already at highest point so assign a new random index
            rand_index = rand_index

    else :
        # grab a random value
        random_index = rand_index

    return (rand_index)


@app.route('/')
def quote_me():
    quote_stash_tmp = quotes.copy()
    max_index_value = np.max(quote_stash_tmp['index'].values)
    rand_index_value = randrange(max_index_value)

    darker = request.args.get("darker")
    brighter = request.args.get("brighter")

    if darker is not None :

        try :
            current_index = int(darker)
        except ValueError:
            # somebody is gaming the system
            current_index = rand_index

        new_index = gimme_a_quote(direction = 'darker', current_index = current_index, max_index_value = max_index_value)

    elif brighter is not None :

        try :
            current_index = int(brighter)
        except ValueError:
            # somebody is gaming the system
            current_index = rand_index

        new_index = gimme_a_quote(direction = 'brighter', current_index = current_index, max_index_value = max_index_value)

    else :
        # grab a random value
        new_index = randrange(max_index_value)

    random_quote = quote_stash_tmp.iloc[new_index]

    # get a rando integer between 0 and max_index_value
    quote = random_quote['quote']
    author = random_quote['author']
    current_id = random_quote['index']

    return json.dumps({
        "quote" : quote,
        "author" : author,
        "current_id" : int(current_id)});

if __name__=='__main__':
    app.run(debug=True)


