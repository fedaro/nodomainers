from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from nodomainers.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    avatarurl = Column(String(200), unique=False)

    def __init__(self, username, avatarurl=None):
        self.username = username
        self.avatarurl = avatarurl

    def __repr__(self):
        return str(self.username)

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    message = Column(String(140), unique=False)
    date = Column(DateTime, unique=False)
    tweet_id = Column(Integer, unique=True)
   
    def __init__(self, user, message, date, tweet_id):
        self.user = user
        self.message = message
        self.date = date
        self.tweet_id = tweet_id 

    def __repr__(self):
        return '<User %r> <Message: %r>' % (str(self.user.username), str(self.message))

