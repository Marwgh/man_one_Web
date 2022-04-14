function _all(q, e = document) { return e.querySelectorAll(q) }
function _one(q, e = document) { return e.querySelector(q) }


function toggleTweetModal() {
  _one("#tweetModal").classList.toggle("hidden")
}


async function delete_tweet(tweet_id) {
  //_one("#" + tweet_id).remove()
  //event.target.parentElement.parentElement.parentElement.parentElement.remove()
  //document.getElementById(tweet_id).remove()
  console.log(tweet_id)
  const connection = await fetch(`/delete/${tweet_id}`, {
    method: "DELETE",

  })
  if (!connection.ok) {
    return
  }

  document.querySelector(`[id='${tweet_id}']`).remove()





}

async function sendTweet() {
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/create", {
    method: "POST",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }
  console.log(await connection);
  const connection_text = await connection.text();/* tweet id text*/
  const tweet_id = connection_text.slice(0, 36);
  const tweet_image = connection_text.slice(36, 41)
  const image_path = _one("input[type=file]", form).value.replaceAll(" ", "-").replaceAll("’", "").replaceAll("é", "e").replaceAll("(", "").replaceAll(")", "").trim()
  /*SUCCES*/
  let tweet = ''
  if (tweet_image == "true") {
    tweet = `
        <section class="tweet" id="${tweet_id}">
        <p class="Tweet_time">{{tweet["iat"]}}</p>
        <p>${_one("textarea", form).value}</p>
        <article>
          <button onclick="delete_tweet('${tweet_id}')">🗑️</button>
          <button onclick="openModuleUpdate('true' ,'${_one("textarea", form).value}' , '/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}' )">✏️</button>
        </article>
        <img src="/image/${image_path.substring(image_path.lastIndexOf("\\") + 1)}" alt="">
      </section>
    `
  } else {
    tweet = `
        <section class="tweet" id="{{${tweet_id}}}">
        <p class="Tweet_time">{{tweet["iat"]}}</p>
        <p>${_one("textarea", form).value}</p>
        <article>
          <button onclick="delete_tweet('${tweet_id}')">🗑️</button>
          <button onclick="openModuleUpdate('false' ,'${_one("textarea", form).value}')">✏️</button>
        </article>
      </section>
    `
  }

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)


}


function openModuleUpdate(is_image, tweet_text, image_path) {
  console.log(is_image, tweet_text, image_path)

  if (is_image == "true") {
    console.log("zs")
    _one("#updating_module #image_updating_div").style.display = "block";
    _one(" #image_updating_div img").setAttribute("src", image_path);
  }
  _one("#updating_module").style.display = "block";
  _one("#tweet_text_updator").value = tweet_text;
  console.log(tweet_text);
}
document.getElementById("close_update").addEventListener("click", closeModuleUpdate);


function closeModuleUpdate() {
  _one("#updating_module").style.display = " none";
  console.log("yes")
}

async function updateTweet() {
  const form = event.target
  // Get the button, set the data-await, and disable it
  const connection = await fetch("/update", {
    method: "UPDATE",
    body: new FormData(form)
  })

  if (!connection.ok) {
    return
  }
  console.log(await connection);


}
