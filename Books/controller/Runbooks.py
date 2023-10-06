import pandas as pd
from Books.Input.Model.model import Input
from Books.Input.service.services import take_input,take_input_get , convert_input
from Books.Model.model import Books
from Books.service.services import create,update,delete,get_all_books
from flask_cors import cross_origin
from Repo.Connection import db



# Load the Excel file
# df = pd.read_excel(r"C:\Users\Thanos\PycharmProjects\project_AB\Book 4.xlsx")
#
# # Iterate through each row
# for index, row in df.iterrows():
#     if index>0:
#         break
#     print(index)
#     new= Input
#     new.name=row['Name']
#     new.author = row['Author']
#     new.genre = row['Genre']
#     new.completed = row['completed']
#     # create(db, Books, new)
#     print(new)
#
#
#     # print(f"Row {index + 1}:")
#     # print(f"Name: {row['Name']}")
#     # print(f"Author: {row['Author']}")
#     # print(f"Genre: {row['Genre']}")
#     # print(f"Completed: {row['completed']}")
#     print("\n")





def routes(app,db):
    # db = SQLAlchemy(app)
    @app.route('/', methods=['GET'])
    @cross_origin('http://localhost:3000/')
    def get_users():
        return get_all_books(db, Books)

    @app.route('/', methods=['Post'])
    @cross_origin('http://localhost:3000/')
    def create1():
        inp,raw= convert_input(take_input)

        return create(db,Books,inp)
    #
    @app.route('/', methods=['Put'])
    @cross_origin('http://localhost:3000/')
    def update_1():
        inp,raw= convert_input(take_input)
        return update(db,Books,inp,raw)

    #
    # @app.route('/', methods=['Delete'])
    # def delete1():
    #     inp,raw= convert_input(take_input)
    #     return delete(db,Books,inp,raw)

