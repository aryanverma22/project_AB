import random
import datetime
import os
from flask import Flask, request, jsonify, make_response
from Books.service.pic_search import get_book_pic

def get_all_books(db, Books):
    '''
        Returns all the Books in the users table.
        :param db:
        :param Books:
        :return:
        '''

    # db.create_all()
    # db.commit()

    data = Books.query.all()

    out=[]
    # print(data)
    i=0
    for x in data:
        i+=1

        temp={'id': x.id,
              'name': x.name,
              'author': x.author,
              'genre': x.genre,
              'picture': x.picture,
              'completed':x.completed}
        out.append(temp)
    random.shuffle(out)
    final= out
    return make_response(final,201)



def create(db, Books, inp):
    '''
    Creates a new entry in the Books database by taking Json input('name,'author','genre','completed') from the API and returns the status message
    :param db:
    :param Books:
    :return:
    '''
    # data= request.json
    # inp= Input(**data)
    print(inp.name)
    # name1= data["name"]
    # email1= data["email"]

    present = Books.query.filter_by(name= inp.name).first()
    print(present)
    name = inp.name
    author = inp.author
    pic_link= get_book_pic(name,author)[0]
    # if inp.completed == 0:
    #     inp.completed= False
    # else:
    #     inp.completed= True
    new = Books(name=inp.name, genre=inp.genre, author= inp.author, completed= inp.completed, picture= pic_link)
    # if present is not None:

    db.add(new)
    db.commit()
    final={'data': f" ('ID: {new.id}', 'name: {new.name}', 'author': {new.author}', 'genre': {new.genre}','pic':{new.picture})",
           'message': "Books successfully added"}
    return make_response(final,201)
    # else:
    #     final = { 'data': f" ('ID: {new.id}', 'name: {new.name}', 'author': {new.author}', 'genre': {new.genre}')",
    #              'message': "Books already present"}
    #     return make_response(final,404)

def update(db, Books, inp, data):
    '''
    Updates the users corresponding to the 'user_id', 'change_in', 'new_data' being provided as a Json input.
    :param db:
    :param Books:
    :return:
    '''
    print(data)
    # data= request.json
    # inp=Input(**data)
    # user_id= data["user_id"]
    # col_to_change= data["change_in"]
    # new= data["new_data"]
    present = Books.query.filter_by(id=inp.id).first()
    if not present:
        return make_response({'Data': data,"message":"Books not present"},404)
    else:
        if present.completed== True:
            present.completed= False
            db.commit()
        else:
            present.completed = True
            db.commit()
        return make_response({'Message':"Updated"}, 201)




def delete(db,User,inp,data):
    '''
    Deletes the record corresponding to the 'user_id' being taken as a Json input.
    :param db:
    :param User:
    :return:
    '''
    # data=request.json
    # inp= Input(**data)
    # uid= data["user_id"]
    print(inp.user_id)
    present = User.query.filter_by(id=inp.user_id).first()
    if not present:
        return make_response({'Data': data, 'message':"User_id not valid"}, 404)
    else:
        db.delete(present)
        db.commit()

        final={'data': f" ('ID: {present.id}', 'name: {present.name}', 'email_id: {present.email_id}', 'Avatar:{present.avatar}')",
               'message':"Books deleted successfully" }
        return make_response(final,201)





    # change= data.get("new_name")
    # # print(id, email)
    # if email:
    #     present = Books.query.filter_by(email_id=email).first()
    #     if not present:
    #         return make_response("Books not present",202)
    #     else: