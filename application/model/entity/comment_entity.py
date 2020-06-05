# cria classe de comentários
class Comment:
    # define parametros
    def __init__(self, text, idMovie):
        self._comment = text
        self._MovieId = idMovie
    # retorna comentários

    def getComment(self):
        return self._comment
    # define comentários

    def setComment(self, text):
        self._comment = text
    # retorna id do video relacionado ao comentário

    def getIdMovie(self):
        return self._MovieId
