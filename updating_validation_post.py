from bottle import post , request , redirect , response
import g

@post("/updating-validation")
def _():
  try:
    error = "invalid-update"
    if not request.forms.get("tweet_title") :
      redirect(f"/updating?title={request.forms.get('tweet_title')}&description={request.forms.get('tweet_description')}&iat={request.forms.get('time')}&id={request.forms.get('id')}&error={error}")
    if not request.forms.get("tweet_description") :
      redirect(f"/updating?title={request.forms.get('tweet_title')}&description={request.forms.get('tweet_description')}&iat={request.forms.get('time')}&id={request.forms.get('id')}&error={error}")
    new_title = request.forms.get("tweet_title")
    new_description = request.forms.get("tweet_description")
    time = request.forms.get("time")
    id = request.forms.get("id")
    new_tweet = {"title" :new_title , "description" : new_description , "id": id , "iat" : time}
    
    
    
    for  index ,tweet in enumerate(g.TWEETS):
      if tweet["id"] == new_tweet["id"]:
          g.TWEETS.pop(index)
          g.TWEETS.append(new_tweet)
          return redirect("/tweet")



    return  redirect("/tweet")

  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}