from flask import current_app
from application.model.entity.comment_entity import Comment


class Comment_DAO:
    def __init__(self):
        self._commentList = []

    def getComments(self):
        return self._commentList

    def addComment(self, comment):
        self._commentList.append(comment)

    def findComment(self, id):
        comments = current_app.config["comments"]
        commentsList = []
        for i, item in enumerate(comments.getComments()):
            if item.getIdMovie() == id:
                commentsList.append(item)
        return commentsList
