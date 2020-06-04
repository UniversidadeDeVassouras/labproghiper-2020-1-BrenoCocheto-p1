from application import app
from flask import render_template, current_app, request
from application.model.entity.comment_entity import Comment
from flask.json import jsonify


@app.route("/movie/<int:categoryId>/<int:movieId>")
def movie(categoryId, movieId):
    movies = current_app.config["movie"]
    categories = current_app.config["categories"]
    comment = current_app.config["comments"]
    category = categories.getCategoryById(categoryId)
    categoryMovies = category.getVideosByCategory()
    movie = movies.getMoviesById(movieId, categoryMovies)
    movie.setViews(movie.getViews() + 1)
    comments = comment.findComment(movie.getId())
    return render_template(
        "movie.html",
        movie=movie,
        category=categories,
        comments=comments,
        categories=categories.getListCategory(),
    )


@app.route("/movie/comment")
def comment():
    try:

        comments = current_app.config["comments"]
        comment = Comment(request.args.get("comment"), int(request.args.get("movieId")))

        comments.addComment(comment)

        return jsonify(comment.getComment())

    except Exception as e:
        return str(e)


@app.route("/movie/like")
def like():
    try:
        categoryId = int(request.args.get("categoryId"))
        movieId = int(request.args.get("movieId"))
        categories = current_app.config["categories"]
        category = categories.getCategoryById(categoryId)
        movies = current_app.config["movie"]
        categoryMovies = category.getVideosByCategory()
        movie = movies.getMoviesById(movieId, categoryMovies)
        movie.setLike(movie.getLike() + 1)
        return jsonify(like=movie.getLike())
    except Exception as e:
        return str(e)
