from bottle import view , get


@get("/create")
@view("create.html")

def _():
  return 