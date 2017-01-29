from flask import render_template, session, redirect, url_for
from . import main


@main.route('/')
def home():
    """Render website's home page."""
    return 'hey motherfucker' #render_template('about.html')
