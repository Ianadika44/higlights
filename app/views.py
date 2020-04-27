from flask import render_template
from app import app
from .request import get_articles,get_source


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    General_news = get_source('sources')
    title = 'Home - Welcome to The best  Online News Website Online'
    return render_template('index.html', title=title,news = General_news)




@app.route('/articles/<int:id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    cnn_news = get_articles('cnn')
    bbc_news = get_articles('bbc-news') 

    return render_template('articles.html',title = title,articles = articles)
