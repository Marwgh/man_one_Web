from bottle import view , get , request , response ,redirect
import g

@get("/updating")
@view("updating.html")

def _():
  try:
    if not request.params.get('title'):
      return redirect("/tweet?error=invalidTweet")
    if not request.params.get('description'):
      return redirect("/tweet?error=invalidTweet")
    if not request.params.get('iat'):
      return redirect("/tweet?error=invalidTweet")
    if not request.params.get('id'):
      return redirect("/tweet?error=invalidTweet")


    updated_title = request.params.get('title')
    updated_description = request.params.get('description')
    time = request.params.get('iat')
    id = request.params.get('id')
    error = request.params.get('error')

    print("#"*40)
    print(error)
    print(updated_title)
    print(updated_description)
    if not (updated_title, updated_description , time , id) :
      return redirect("/tweet?error=invalidTweet")
    

    return dict(updated_title=updated_title , updated_description=updated_description , time=time , id=id , error=error)

  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}