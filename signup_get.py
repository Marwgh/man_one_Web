from bottle import get, view

@get("/signup")
@view("signup.html")
def _():
  return 