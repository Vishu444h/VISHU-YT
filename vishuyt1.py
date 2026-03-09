from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
categories = {
    'anime': [
        {'title':'Naruto Hindi Dub','id':'VIDEO_ID_1','quality':['720','1080','1440','2160']},
        {'title':'One Piece Hindi Dub','id':'VIDEO_ID_2','quality':['720','1080','1440','2160']},
    ],
    'movies': [
        {'title':'Movie 1','id':'MOVIE_ID_1','quality':['720','1080','1440','2160']},
        {'title':'Movie 2','id':'MOVIE_ID_2','quality':['720','1080','1440','2160']},
    ],
    'songs': [
        {'title':'Song 1','id':'SONG_ID_1','quality':['720','1080','1440','2160']},
        {'title':'Song 2','id':'SONG_ID_2','quality':['720','1080','1440','2160']},
    ]
}

@app.route('/')
def home():
    return render_template('index.html', categories=categories)

@app.route('/get_category')
def get_category():
    cat_name = request.args.get('cat')
    videos = categories.get(cat_name, [])
    return jsonify(videos)

if __name__ == '__main__':
    app.run(debug=True)
