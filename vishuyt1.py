from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

# ===== HTML template embedded =====
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>VISHU YT</title>
    <style>                                                                                                                                          body { font-family: Arial; background:#121212; color:white; margin:0; padding:0; text-align:center; }
        .top-bar { background:#222; padding:5px 15px; font-size:14px; display:flex; justify-content:space-between; color:white; }
        .top-bar .left { color:skyblue; text-align:left; }
        .top-bar .right { text-align:right; }                                                                                                        h1 { margin:20px 0; }
        input[type=text]{ padding:10px; width:60%; border-radius:5px; border:none; }
        button{ padding:10px 15px; margin-left:5px; border:none; border-radius:5px; cursor:pointer; background:linear-gradient(to right,#ff9>
        .video-card { background:#222; margin:15px auto; padding:15px; border-radius:10px; max-width:700px; text-align:left; }
        .video-card iframe { margin-top:10px; border-radius:10px; width:100%; height:400px; }
        .qualities a { margin-right:10px; text-decoration:none; color:#ff9900; font-weight:bold; }
        .qualities a:hover{ color:white; }
    </style>
</head>
<body>                                                                                                                                           <div class="top-bar">
        <div class="left">FOLLOW ME ON INSTA freak_vishu</div>
        <div class="right">Developer @freak_vishu</div>
    </div>
    <h1>VISHU YT</h1>                                                                                                                            <form method="POST">
        <input type="text" name="query" placeholder="Search video or song..." required>                                                              <button type="submit">Search</button>
    </form>

    {% if videos %}
        {% for video in videos %}
        <div class="video-card">
            <h3>{{video['title']}}</h3>                                                                                                                  <iframe src="https://www.youtube.com/embed/{{video['id']}}" allowfullscreen></iframe>
            <div class="qualities">
                {% for q in ['1080','1440','2160'] %}
                    <a href="/download/{{video['id']}}/mp4/{{q}}">{{q}}p</a>
                {% endfor %}
                <a href="/download/{{video['id']}}/mp3/0">MP3</a>
                <a href="https://www.youtube.com/watch?v={{video['id']}}" target="_blank">Watch on YT</a>
            </div>
        </div>
        {% endfor %}
    {% endif %}
</body>
</html>
"""

# ===== routes =====
@app.route('/', methods=['GET','POST'])
def home():
    videos = []
    if request.method == 'POST':
        query = request.form.get('query')
        # Search YouTube using yt_dlp
        ydl_opts = {'quiet': True, 'extract_flat': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(f"ytsearch5:{query}", download=False)
                for v in info['entries']:
                    videos.append({'title':v['title'], 'id':v['id']})
            except:
                pass
    return render_template_string(HTML_TEMPLATE, videos=videos)

# ===== dummy download route (to be implemented) =====
@app.route('/download/<video_id>/<format>/<quality>')
def download(video_id, format, quality):
    return f"Download feature for {video_id} in {format} {quality}p coming soon!"

if __name__ == "__main__":
    app.run(debug=True)
