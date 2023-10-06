import datetime
import os
from sqlalchemy import Column, Integer, String, Time, Boolean
from Repo.Connection import Base

# Base= declarative_base()

class Books(Base):
    __tablename__='Books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(50), unique=True)
    name = Column(String(100))
    genre = Column(String)
    author= Column(String)
    picture= Column(String)
    completed= Column(Boolean)



    # def __repr__(self):
    #
    #     # output= "{'ID': ,'Name': {self.name},'email': {self.email_id}}"
    #     # return output
    #     return f" ('ID: {self.id}', 'name: {self.name}', 'email_id: {self.email_id}')"
