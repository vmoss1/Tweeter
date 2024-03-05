# !!START
from flask import Flask , render_template , redirect , url_for
from .config import Config
from app.tweets import tweets
from random import randint , random
from app.forms.form import CreateTweet
from datetime import date

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    tweet = randint(0 , len(tweets) -1)
    return render_template("index.html" , tweet=tweet)

@app.route('/feed')
def feed():
    return render_template("feed.html" ,  tweets=tweets)

@app.route("/new" , methods=["GET","POST"])
def new():
    form = CreateTweet()

    if form.validate_on_submit():
        author = form.author.data
        tweet = form.tweet.data
        tweet_id = len(tweets) + 1
        tweet_date = date.today()
        likes = randint(10000, 600000) 

        new_tweet = {'id': tweet_id, 'author': author, 'tweet': tweet, 'date': tweet_date, 'likes': likes}
        tweets.append(new_tweet) 

        return redirect(url_for('feed')) 
    else:
        # If there are errors, render the form again with error messages
        return render_template('new_tweets.html', form=form)


# !!END
