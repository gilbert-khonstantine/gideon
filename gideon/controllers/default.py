# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def welcome():
    print(request.vars)
    if request.vars['URL'] and request.vars['query']:
        response.flash = 'please fill only one row'
    if request.vars['URL'] and not request.vars['query']:
        session.url = request.vars['URL']
        redirect(URL('result'))
    if request.vars['query'] and not request.vars['URL']:
        session.query = request.vars['query']
        redirect(URL('result_qry'))
    if not request.vars['URL'] and not request.vars['query']:
        response.flash = 'please fill the form'
    
    return dict() 

def result():
    news = crawler(session.url)
    temp = fake_news_detect(session.url)
    ctr = 0
    try:
        wordcloud_generator(news['body'])
        err_wc = ''
    except:
        ctr = 1
        err_wc='Word Cloud Can Not be Visualized'
    score = temp[1]
    corr_news = temp[2]
    if temp[0]==0:
        conc = 'Possibly Fake News'
    else: conc = 'Possibly Not Fake News'
    corr_news=list(set(corr_news))
    return dict(news = news,conc=conc,score = score,corr_news=corr_news,err_wc=err_wc,ctr=ctr)

def result_qry():
    news = session.query
    temp = fake_news_detector_keyword(session.query)
    score = temp[1]
    corr_news = temp[2]
    if temp[0]==0:
        conc = 'Possibly Fake News'
    else: conc = 'Possibly Not Fake News'
    corr_news=list(set(corr_news))
    return dict(news = news,conc=conc,score = score,corr_news=corr_news)

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
