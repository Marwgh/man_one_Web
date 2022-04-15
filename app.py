from bottle import run , get , post , view ,static_file 
import uuid
import g





#################################################################
import tweet_delete                                       #DELETE

import signup_post                                        #POST
import login_post                                         #POST
import create_post                                        #POST

import tweet_put                                          #PUT


import users_get                                          #GET
import login_get                                          #GET
import logout_get                                         #GET
import logingout_get                                      #GET
import signup_get                                         #GET
import tweet_get                                          #GET
#################################################################

@get("/")
@view("home.html")
def _():
  return dict(tweets=g.TWEETS)


#################################################################

@get("/app.js")
def _():
  return static_file("app.js", root=".")


#################################################################

@get("/app.css")
def _():
  return static_file("app.css" , root=".")
#################################################################

@get("/validator.js")
def _():
  return static_file("validator.js", root=".")


#################################################################
@get("/image/<image_name>")
def _(image_name):
  return static_file(image_name, root="./image")




run(host="127.0.0.1" , port ="4533" , debug=True , reloader=True , server="paste")