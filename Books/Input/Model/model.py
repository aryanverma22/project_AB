from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Time, Boolean

class Input(BaseModel):
    id=""
    name= ""
    author= ""
    genre= ""
    completed: bool
    change_in= ""
    new_data=""







