from flask import current_app
from application.model.entity.comment_entity import Comment

# inicia classe onde serão armazenados os comentários


class Comment_DAO:
    def __init__(self):
        # inicia lista de comentários
        self._commentList = []
# retorna lista de comentários

    def getComments(self):
        return self._commentList
# adiciona comentário na lista

    def addComment(self, comment):
        self._commentList.append(comment)
# retorna comentário pelo id inputado

    def findComment(self, id):
        comments = current_app.config["comments"]
        commentsList = []
        for i, item in enumerate(comments.getComments()):
            if item.getIdMovie() == id:
                commentsList.append(item)
        return commentsList
