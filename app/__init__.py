# !!START
from flask import Flask , render_template , redirect , url_for #importing from Flask
from .config import Config #importing from the config file
from app.tweets import tweets #importing the tweets file which contains a list of dictionaries
from random import randint # importing random
import random
from app.forms.form import CreateTweet #importing the form file from the forms
from datetime import date #importing datetime for the create a new tweet

app = Flask(__name__) # app to flask to be the dunder name auto assigns name of the file

app.config.from_object(Config) # used in Flask to load configuration settings from a Python object.
 
@app.route('/') #creating a route 
def index():
    tweet = tweets[int(random.random() * len(tweets))] #randomly picking each tweet on DOM reload
    return render_template("index.html" , tweet=tweet) # use render template to use templates created

@app.route('/feed')
def feed():
    return render_template("feed.html" ,  tweets=tweets)

@app.route("/new" , methods=["GET","POST"]) #using methods for dual purpose
def new():
    form = CreateTweet() #invoking the create tweet form assigning to form 

    if form.validate_on_submit(): # if the form has passed validation this will create a new tweet
        author = form.author.data
        tweet = form.tweet.data
        tweet_id = len(tweets) + 1
        tweet_date = date.today()
        likes = randint(10000, 600000) 

        new_tweet = {'id': tweet_id, 'author': author, 'tweet': tweet, 'date': tweet_date, 'likes': likes}
        tweets.append(new_tweet)  # appending the new tweet to the current tweets list

        return redirect(url_for('feed')) #is url for needed to redirect to a new page
    else:
        # If there are errors, render the form again with error messages
        return render_template('new_tweets.html', form=form)


# !!END
