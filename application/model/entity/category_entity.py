from flask import current_app

# inicia a classe de categoria


class Category:
    # passa parametros
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description
    # retorna o id

    def getId(self):
        return self._id
    # retorna o nome

    def getName(self):
        return self._name
    # retorna a descrição

    def getDescription(self):
        return self._description
    # retorna os vídeos pelo id da categoria

    def getVideosByCategory(self):
        movies = current_app.config["movie"]
        moviesCategory = []
        for i, item in enumerate(movies.getMovies()):
            if item.getCategoryId() == self.getId():
                moviesCategory.append(item)
        return moviesCategory
