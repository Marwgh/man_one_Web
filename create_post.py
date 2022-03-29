from bottle import post , request , redirect , response
import g
import uuid
import time


@post("/create")
def _():
  try:
    if not request.forms.get("tweet_title") :
      return redirect("/create")
    if not request.forms.get("tweet_description") :
      return redirect("/create")

  
    title = request.forms.get("tweet_title")
    description = request.forms.get("tweet_description")
    id = str(uuid.uuid4())
    issue_time = time.ctime( int(time.time()) )

    tweet={"title" : title , "description" : description , "id": id , "iat" : issue_time }
    g.TWEETS.append(tweet)
    print(tweet)

    return redirect("/tweet")
    
  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}