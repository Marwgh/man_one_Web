from bottle import get , view , request ,response

@get("/login")
@view("login.html")
def _():
  try:
    error = request.params.get("error")
    user_email = request.params.get("user_email")
    return  dict(error=error , user_email=user_email)


  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}