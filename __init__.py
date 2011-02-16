# all the imports
from flask import Flask
app = Flask(__name__)
app.secret_key = 'development_key'
from nodomainers.database import db_session
from nodomainers import views


@app.after_request
def shutdown_session(response):
    db_session.remove()
    return response
