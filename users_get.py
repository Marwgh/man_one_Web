from bottle import get , view ,redirect , request , response
import g
import jwt




@get("/users")
@view("users.html")
def _():
  try:
    if len(g.SESSIONS) < 1 :
      return redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
      return redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for  session in g.SESSIONS :
      if not session['user_id'] == user_info["user_id"]:
        return redirect("/login?error=invalidS")

    return dict(users=g.USERS , sessions=g.SESSIONS)

  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}
