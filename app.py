#!/usr/bin/env python
"""
Simple Flask web application.
"""

from flask import Flask, request, render_template

APP = Flask(__name__, template_folder='templates')


@APP.route('/')
def home():
    '''
    Rendering Home Page
    '''
    return render_template('index.html')


@APP.route('/hello', methods=['POST'])
def hello():
    '''
    For rendering results on HTML GUI
    '''
    inputs = list(request.form.values())
    result = f"Hello There {inputs[0]}"
    return render_template('index.html', hello_text=result)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)
