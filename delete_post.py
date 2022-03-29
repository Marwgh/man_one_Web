from bottle import post , redirect , response
import g


@post("/delete/<tweet_id>")
def _(tweet_id):
  #VALIDATION 
  try:
    if not tweet_id :
      return redirect("/tweet")
  
    print(tweet_id)
    print("#"*30)
    for  index ,tweet in enumerate(g.TWEETS):
      if tweet["id"] == tweet_id:
          g.TWEETS.pop(index)
          return redirect("/tweet")
          
  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}




