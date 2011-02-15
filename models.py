from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from nodomainers.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    #avatar = Column(String(50), unique=False)

    def __init__(self, username, avatar=None):
        self.username = username
        #self.avatar = avatar

    def __repr__(self):
        return str(self.username)

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    message = Column(String(140), unique=False)
    date = Column(DateTime, unique=False)
   
    def __init__(self, user, message, date):
        self.user = user
        self.message = message
        self.date = date  

    def __repr__(self):
        return '<User %r> <Message: %r>' % (str(self.username), str(self.message))

