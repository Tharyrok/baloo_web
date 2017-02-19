#/usr/bin/env python2
# -*- coding: utf-8 -*-

## Memo : ./gotty --address=127.0.0.1 --port=4242 --credential demo:test -w --reconnect screen -x -R -S main

from flask import Flask, redirect, request, render_template, g, jsonify
from flask_babel import Babel, gettext



app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return getattr(g, 'lang')

@app.route('/')
def language_detection():
    return redirect('/%s' % request.accept_languages.best_match(['fr', 'en', 'nl']))

@app.route('/<language>')
def lang_home(language):
    setattr(g, 'lang', language)
    return render_template('home.html', data={"lang": language})

@app.route('/status')
def get_status():
    return jsonify('True')

@app.route('/create')
def post_create():
    return jsonify('True')

@app.route('/remove')
def get_remove():
    return jsonify('True')

if __name__ == '__main__':
    app.run(debug=False)
