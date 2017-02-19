#/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect, request, render_template, g
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
    return render_template('layout.html', data={"lang": language})


if __name__ == '__main__':
    app.run(debug=False)
