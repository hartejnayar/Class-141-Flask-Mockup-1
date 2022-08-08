from flask import Flask, jsonify, request
import csv

from importlib_metadata import method_cache

app = Flask(__name__)


all_movies = []

with open('movie_recommendation.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []



@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "Success!",
    })


@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route("/not-liked-movie", methods = ["POST"])
def not_liked_movie():
    movie = all_movies[0]
    all_movies  = all_movies[1:]
    not_liked_movies.append(movie)

    return jsonify({
        "status" : "Success!"
    }),201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)

    return jsonify({
        "status" : "Success!"
    }),201


if __name__ == "__main__":
    app.run()
