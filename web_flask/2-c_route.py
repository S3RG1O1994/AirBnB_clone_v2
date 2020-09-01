#!/usr/bin/python3
from flask import Flask
'''This function is for edit html'''

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''This return string in the page'''
    return 'HBNB'


@app.route('/hbnb')
def index_hbnb():
    '''This return string in the page'''
    return 'Hello HBNB!'


@app.route('/c/<text>')
def index_c(text):
    '''This is return string pass in text'''
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run()
