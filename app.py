from flask import Flask

app = Flask(__name__)


@app.route('/')
def you_pro_girl():
    return 'You, Pro Girl!'


if __name__ == '__main__':
    app.run()
