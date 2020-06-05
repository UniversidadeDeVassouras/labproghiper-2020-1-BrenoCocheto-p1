from application.model.entity.category_entity import Category
from application.model.dao.movie_dao import Movie_DAO

# inicializa classe onde serão armazenadas as categorias


class Category_DAO:
    def __init__(self):
        # cria lista das categorias
        self._categorias = []
        # adiciona itens na lista
        self._categorias.append(Category(1, "Comida", "Deliciosas comidas",))
        self._categorias.append(
            Category(2, "Tecnologia", "Hacks sobre tecnologia",))
        self._categorias.append(Category(3, "Variados", "Assuntos variados",))
# retorna lista de categorias

    def getListCategory(self):
        return self._categorias
# retorna a categoria pelo id inserido

    def getCategoryById(self, id):
        for i, category in enumerate(self.getListCategory()):
            if category.getId() == id:
                return category
        return None
