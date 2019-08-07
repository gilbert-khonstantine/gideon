# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from googlesearch import search
from bs4 import BeautifulSoup
import gensim
from nltk.tokenize import word_tokenize,sent_tokenize
import requests
import PyPDF2
import html2text
from readability.readability import Document
from tqdm import tqdm
import re
import time
import bleach
# ---- example index page ----
def welcome():
    form=FORM('URL to be checked:',
              INPUT(_name='URL', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))

    if form.accepts(request, session):
        response.flash = 'Please wait for 1-2 minutes while we process your request.'
        session.url = request.vars['URL']
        del request.vars['URL']
        redirect(URL('result'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form = form) 

def result():
    news = crawler(session.url)
    temp = fake_news_detect(session.url)
    score = temp[1]
    corr_news = temp[2]
    if temp[0]==0:
        conc = 'Possibly Fake News'
    else: conc = 'Possibly Not Fake News'
    form_1 = FORM(INPUT(_type='submit',_value="Return to Main Page"))
    if form_1.accepts(request, session):
        redirect(URL('welcome'))
    return dict(news = news,conc=conc,score = score,corr_news=corr_news,form=form)

def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
