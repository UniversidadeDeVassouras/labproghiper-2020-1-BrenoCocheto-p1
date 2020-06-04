from application.controller import movie_controller
from application.controller import category_controller
from application.controller import home_controller
from flask import Flask
from application.model.dao.comment_dao import Comment_DAO
from application.model.dao.category_dao import Category_DAO
from application.model.dao.movie_dao import Movie_DAO

import os

app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"),
)
category = Category_DAO()
movie = Movie_DAO()
comment = Comment_DAO()
app.config["movie"] = movie
app.config["comments"] = comment
app.config["categories"] = category
