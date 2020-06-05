# instanciada classe de video
class Movie:
    # definindo parametros
    def __init__(
        self, id, name, path, like, description, thumbnail, id_category, comment, views
    ):
        self._id = id
        self._name = name
        self._like = like
        self._description = description
        self._path = path
        self._thumbnail = thumbnail
        self._id_category = id_category
        self._comment = comment
        self._views = views
    # retorna id

    def getId(self):
        return self._id
    # retorna nome

    def getName(self):
        return self._name
    # retorna curtidas

    def getLike(self):
        return self._like
# retorna comentários

    def getComment(self):
        return self._comment
# retorna caminho do vídeo

    def getPath(self):
        return self._path
# retorna caminho da thumbnail

    def getThumb(self):
        return self._thumbnail
# retorna o id da categoria relacionada ao video

    def getCategoryId(self):
        return self._id_category
# retorna a descrição

    def getDescription(self):
        return self._description
# retorna a quantidade de visualizações

    def getViews(self):
        return self._views
# define as visualizações

    def setViews(self, value):
        self._views += value
# define as curtidas

    def setLike(self, value):
        self._like = value
