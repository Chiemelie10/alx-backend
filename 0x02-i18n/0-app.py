#!/usr/bin/env python3
"""This module defines functions that run a flask application."""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


def index() -> str:
    """The index page."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
