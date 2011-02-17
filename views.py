# -*- coding: utf-8 -*-
from nodomainers import app
from nodomainers.models import User, Tweet
from flask import render_template


app.config['MSG_PER_PAGE'] = 5


@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>')
def show_entries(page):
    #tweets = Tweet.query.all()
    #return render_template('show_entries.html', entries=tweets)
    pagination = Tweet.query \
                 .order_by(Tweet.date.desc())\
                 .paginate(page, app.config['MSG_PER_PAGE'])
    return render_template('show_entries.html', pagination=pagination)


@app.route('/message/<int:id>')
def show_message(id):
    message = Tweet.query.get_or_404(id)
    return render_template('show_message.html', entry=message)
