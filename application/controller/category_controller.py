from application import app
from flask import render_template, current_app


@app.route("/category/<int:id>")
def category(id):
    category = current_app.config["categories"].getCategoryById(id)

    movie = category.getVideosByCategory()
    return render_template(
        "category.html",
        category=category,
        movie=movie,
        categories=current_app.config["categories"].getListCategory(),
    )
