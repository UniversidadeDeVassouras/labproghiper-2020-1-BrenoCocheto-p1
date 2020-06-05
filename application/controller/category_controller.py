from application import app
from flask import render_template, current_app

# rota da oagina de categoria


@app.route("/category/<int:id>")
# função de categoria
def category(id):
    # rota padrão com o id de cada categoria
    category = current_app.config["categories"].getCategoryById(id)
    # pega o vídeo pela categoria
    movie = category.getVideosByCategory()
    # retorna dados para uso
    return render_template(
        "category.html",
        category=category,
        movie=movie,
        categories=current_app.config["categories"].getListCategory(),
    )
