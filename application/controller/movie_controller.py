from application import app
from flask import render_template, current_app, request
from application.model.entity.comment_entity import Comment
from flask.json import jsonify

# define rota dos videos


@app.route("/movie/<int:categoryId>/<int:movieId>")
# função responsável pela "comunicação"
def movie(categoryId, movieId):
    # rotas padrões
    movies = current_app.config["movie"]
    categories = current_app.config["categories"]
    comment = current_app.config["comments"]
    # define qual categoria foi escolhida
    category = categories.getCategoryById(categoryId)
    # pega os vídeos da categoria definida
    categoryMovies = category.getVideosByCategory()
    # pega o video selecionado
    movie = movies.getMoviesById(movieId, categoryMovies)
    # adiciona visualização
    movie.setViews(movie.getViews() + 1)
    # checa comentários
    comments = comment.findComment(movie.getId())
    # retorna dados para a página
    return render_template(
        "movie.html",
        movie=movie,
        category=categories,
        comments=comments,
        categories=categories.getListCategory(),
    )

# rota de comentários


@app.route("/movie/comment")
# função de comentários
def comment():
    try:

        comments = current_app.config["comments"]
        # request para listar os comentários
        comment = Comment(request.args.get("comment"),
                          int(request.args.get("movieId")))
        # adiciona comentários
        comments.addComment(comment)
        # retorna lista de comentários
        return jsonify(comment.getComment())
# trata excessões
    except Exception as e:
        return str(e)

# rota das curtidas


@app.route("/movie/like")
# função de curtida
def like():
    try:
        # pega id da categoria
        categoryId = int(request.args.get("categoryId"))
        # pega id do video
        movieId = int(request.args.get("movieId"))
        # rota padrão
        categories = current_app.config["categories"]
        # pega categorias pelo id
        category = categories.getCategoryById(categoryId)
        # rota padrão
        movies = current_app.config["movie"]
        # pega os videos pela categoria
        categoryMovies = category.getVideosByCategory()
        # pega o video pelo id do video dentro da lista de videos
        movie = movies.getMoviesById(movieId, categoryMovies)
        # define curtidas
        movie.setLike(movie.getLike() + 1)
        # retorna dados para uso
        return jsonify(like=movie.getLike())
        # trata excessoes
    except Exception as e:
        return str(e)
