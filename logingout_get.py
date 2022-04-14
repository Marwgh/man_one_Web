from bottle import get , request , redirect , response
import jwt
import g

@get("/logingout")
def _():
  if not request.get_cookie("jwt") :
    return redirect("/login?error=invalidS")

  encoded_jwt = request.get_cookie("jwt")
  user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
  session = user_info
  g.SESSIONS.remove(session)
  
  return redirect("/")
