class Comment:
    def __init__(self, text, idMovie):
        self._comment = text
        self._MovieId = idMovie

    def getComment(self):
        return self._comment

    def setComment(self, text):
        self._comment = text

    def getIdMovie(self):
        return self._MovieId
