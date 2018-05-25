#!/usr/bin/env python3

import os
import sys
import yaml

from flask import Flask, request, render_template

app = Flask(__name__)
version = ""

@app.route('/')
def terminal_home():

    with open('user.yml', 'r') as user:
        user_info = yaml.load(user)

    return render_template('home.html', user=user_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
