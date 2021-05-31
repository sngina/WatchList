from flask import render_template # takes the template file as its own first argument
from app import app


#Views
@app.route('/')
def index():
    '''
    View root page function thats returns the index page and its data
    '''
    title ='Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html' , title = title)
@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)