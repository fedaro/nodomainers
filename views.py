from nodomainers import app
from nodomainers.models import User, Tweet
#from nodomainers.database import db_session
from flask import render_template

@app.route('/')
def show_entries():
    tweets = Tweet.query.all()
    return render_template('show_entries.html', entries=tweets)

