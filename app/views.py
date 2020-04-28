from flask import render_template,request,redirect,url_for
from app import app
from .request import get_articles,get_sources


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_sources('bbc_news')
    title = 'Home - Welcome to The best  Online News Website Online'
    return render_template('index.html', title=title,gen = general_news)




@app.route('/articles/<int:id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    cnn_news = get_articles('cnn')
    bbc_news = get_articles('bbc-news') 

    return render_template('articles.html',title = title,articles = articles)