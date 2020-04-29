from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_articles, get_sources


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = get_articles('category=general')
    health = get_articles('category=health')
    technology = get_articles('category=technology')
    title = 'Home - Welcome to The best  Online News Website Online'
    return render_template('index.html', title=title, general=general, technology=technology, health=health)


@main.route('/articles/<int:id>')
def articles(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    cnn_news = get_articles('cnn')
    bbc_news = get_articles('bbc-news')

    return render_template('articles.html', title=title, articles=articles)


@main.route('/sources/<id>')
@main.route('/sources')
def sources(id=None):
    title = 'Sources - All'
    sources = get_sources()
    articles_from_source = get_articles(f'sources={id}')
    
    
    if id:
        return render_template('sources.html', title=f'Headlines | {id}',articles=articles_from_source,id = id)
    else:
        return render_template('sources.html', title=title,sources=sources)
