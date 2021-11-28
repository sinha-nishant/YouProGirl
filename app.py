from os import environ
from flask import Flask, render_template
from pymongo import MongoClient

import db

connection = MongoClient(f"mongodb+srv://python:{environ.get('PASSWORD')}@youprogirl.b8uyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")['you-pro-girl']

app = Flask(__name__)

@app.route('/')
def you_pro_girl():
    return render_template('index.html')

@app.route('/courses')
@app.route('/courses/<string:course_id>')
def courses(course_id=None):
    if course_id:
        return render_template('course.html', course_info = db.get_course(connection, course_id=course_id))
    else:
        return render_template('courses.html', course_list = db.get_courses(connection))

@app.route('/shop')
def shop():
    return render_template('shop.html', products = db.get_products(connection))

@app.route('/about-us')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    from newsapi import NewsApiClient

    newsapi = NewsApiClient(api_key=environ.get('NEWS-KEY'))

    response = newsapi.get_everything(qintitle="(women OR female OR woman) (business OR leader OR successful OR powerful) -sex -guinea -unsafe",
                                           sort_by='popularity',
                                           page_size=18)

    return render_template('news.html', news=response)

if __name__ == '__main__':
    app.run()
