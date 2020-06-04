class Movie:
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

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getLike(self):
        return self._like

    def getComment(self):
        return self._comment

    def getPath(self):
        return self._path

    def getThumb(self):
        return self._thumbnail

    def getCategoryId(self):
        return self._id_category

    def getDescription(self):
        return self._description

    def getViews(self):
        return self._views

    def setViews(self, value):
        self._views += value

    def setLike(self, value):
        self._like = value
