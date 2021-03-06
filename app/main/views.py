from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_articles,search_articles
# from .forms import ReviewForm
# from ..models import Review


# Views
@main.route('/')
def index():


    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to the News Website'

    #Getting Science Sources
    science_sources = get_source('science')

    #Getting Business Sources
    business_sources = get_source('business')

    #Getting Entertainment Sources
    entertainment_sources = get_source('entertainment')

    #Getting General Sources
    general_sources = get_source('general')

    #Getting Health Sources
    health_sources = get_source('health')

    #Getting Sports Sources
    sports_sources = get_source('sports')

    #Getting Technology Sources
    technology_sources = get_source('technology')

    search_article = request.args.get('article_query')

    # if search_article:
    #     return redirect(url_for('search',query=search_article))
    # else:
    return render_template('index.html', title = title, science = science_sources, business = business_sources, entertainment = entertainment_sources, sports = sports_sources, health = health_sources, general = general_sources, technology = technology_sources)


@main.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the source and its articles.
    '''
    all_articles = get_articles(id)
    title = f'Welcome to the News Website -- {id.upper()}'
    id_up = id.upper()

    return render_template('source.html', article = all_articles, title = title, id_up = id_up)


@main.route('/search/')
def search_main():
    '''
    View root page function that returns the search page and the form.
    '''
    title = 'Welcome to the News Website -- Search'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search',query=search_article))
        return render_template('search.html', title = title)
    else:
        return render_template('search.html', title = title)


@main.route('/search/<query>')
def search(query):
    '''
    View function to display the search results
    '''
    query_list = query.split(" ")
    query_format = "+".join(query_list)
    searched_articles =search_article(query_format)
    title = f'Search results for "{query}"'
    return render_template('search.html',article = searched_articles,query=query)    