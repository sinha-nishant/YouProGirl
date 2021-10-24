from os import environ
from flask import Flask, render_template
from pymongo import MongoClient

import db

connection = MongoClient(f"mongodb+srv://python:{environ.get('PASSWORD')}@youprogirl.b8uyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")['you-pro-girl']

app = Flask(__name__)

@app.route('/')
def you_pro_girl():
    return render_template('index.html', courses = db.get_courses(connection))

if __name__ == '__main__':
    app.run()
