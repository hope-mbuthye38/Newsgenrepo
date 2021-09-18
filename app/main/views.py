from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_News, get_sources,search_News
from ..models import News, Review

#...
@main.route('/')
def index():
    '''
    view route function
    '''
    sourcegen = get_sources('sources')
    print(sourcegen)

    return render_template('index.html',sourcegen = sourcegen)
    


