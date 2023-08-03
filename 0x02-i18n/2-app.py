#!/usr/bin/env python3
"""This module defines functions that run a flask application."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """This class lists the available Languages in the app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """This function gets locale from request object."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """The index page."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
