from flask import current_app


class Category:
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getVideosByCategory(self):
        movies = current_app.config["movie"]
        moviesCategory = []
        for i, item in enumerate(movies.getMovies()):
            if item.getCategoryId() == self.getId():
                moviesCategory.append(item)
        return moviesCategory
