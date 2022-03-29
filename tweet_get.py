from bottle import view , get , redirect , request ,response
import jwt
import g

@get("/tweet")
@view("tweet.html")

def _():
  try:
    if len(g.SESSIONS) < 1 :
      return redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
      redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for session in g.SESSIONS :
      if not session['user_id'] == user_info["user_id"]:
        redirect("/login?error=invalidS")
        
    return dict(tweets=g.TWEETS)

  
  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}

  