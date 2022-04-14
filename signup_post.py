import re
from bottle import post, redirect , request , response
import uuid
import g


@post("/signup")
def _():
  if not request.forms.get("user_name"):
    return redirect("/signup")
  if not request.forms.get("user_email"):
    return redirect("/signup")
  
  for user in g.USERS :
    if request.forms.get("user_email") == user["email"]:
      return redirect("/signup")


  if not request.forms.get("user_password"):
    return redirect("/signup")
  if len(request.forms.get("user_password")) < 6 :
    return redirect("/signup")
  if len(request.forms.get("user_password")) > 20 :
    return redirect("/signup")

  
  user_name = request.forms.get("user_name")
  user_email = request.forms.get("user_email")
  user_password = request.forms.get("user_password")
  user_id = str(uuid.uuid4())
  user = { "id": user_id , "email":user_email , "name":user_name , "password":user_password}
  g.USERS.append(user)
  
  return redirect("/login")

    