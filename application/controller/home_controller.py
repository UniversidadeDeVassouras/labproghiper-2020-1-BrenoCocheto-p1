from application import app
from flask import render_template, current_app, Response, request
from application.model.dao.category_dao import Category_DAO
import json


@app.route("/")
@app.route("/home")
def home():
    categories = current_app.config["categories"].getListCategory()
    movies = current_app.config["movie"]
    movie = movies.getMoviesMostViews()

    return render_template("home.html", categories=categories, movie=movie,)


@app.route("/movies/search")
def search():
    try:
        textSearched = request.args.get("search").upper()
        movies = current_app.config["movie"].getMovies()
        search = [x.__dict__ for x in movies if textSearched in x.getName().upper()]
        return Response(json.dumps(search), mimetype="application/json")
    except Exception as e:
        return str(e)
