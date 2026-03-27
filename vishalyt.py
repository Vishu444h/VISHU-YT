from flask import Flask, render_template, request
from youtubesearchpython import VideosSearch

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["search"]

        if "youtube.com" in query or "youtu.be" in query:
            results = [{"title":"Direct Video","link":query}]
        else:
            videosSearch = VideosSearch(query, limit = 10)
            for v in videosSearch.result()["result"]:
                results.append({
                    "title": v["title"],
                    "link": v["link"],
                    "thumb": v["thumbnails"][0]["url"]
                })

    return render_template("index.html", results=results)

app.run(host="0.0.0.0",port=5000)
