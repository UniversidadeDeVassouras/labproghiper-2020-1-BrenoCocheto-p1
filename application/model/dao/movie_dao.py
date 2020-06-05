from application.model.entity.movie_entity import Movie
from flask import current_app

# define a classe onde serão armazenados os videos


class Movie_DAO:
    def __init__(self):
        # inicia uma lista vazia onde serão armazenados os videos
        self._movies = []
        # adiciona vídeos
        self._movies.append(
            Movie(
                1,
                "Curry de Carangueijo",
                "/movies/comida1.mp4",
                0,
                "Como fazer um delicioso curry de carangueijo",
                "/thumbnails/comida1.jpg",
                1,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                2,
                "Curry Vegano",
                "/movies/comida2.mp4",
                0,
                "Como fazer um delicioso curry vegano",
                "/thumbnails/comida2.jpg",
                1,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                3,
                "Lasanha Vegana",
                "/movies/comida3.mp4",
                0,
                "Um delicioso lanche",
                "/thumbnails/comida3.jpg",
                1,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                4,
                "PC Gamer",
                "/movies/tecnologia1.mp4",
                0,
                "Como montar um PC Gamer",
                "/thumbnails/tecnologia1.jpg",
                2,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                5,
                "Lentidão",
                "/movies/tecnologia2.mp4",
                0,
                "Como solucionar a lentidão no MAC",
                "/thumbnails/tecnologia2.png",
                2,
                [],
                0,
            )
        )

        self._movies.append(
            Movie(
                6,
                "Hack",
                "/movies/tecnologia3.mp4",
                0,
                "Como hackear um pc",
                "/thumbnails/tecnologia3.jpg",
                2,
                [],
                0,
            )
        )

        self._movies.append(
            Movie(
                7,
                "Montar uma mala",
                "/movies/diversos1.mp4",
                0,
                "Como montar uma mala corretamente",
                "/thumbnails/diversos1.jpg",
                3,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                8,
                "Andar de Moto",
                "/movies/diversos2.mp4",
                0,
                "Como andar de moto corretamente",
                "/thumbnails/diversos2.jpg",
                3,
                [],
                0,
            )
        )
        self._movies.append(
            Movie(
                9,
                "Escultura",
                "/movies/diversos3.mp4",
                0,
                "Como fazer uma escultura",
                "/thumbnails/diversos3.jpg",
                3,
                [],
                0,
            )
        )
# retorna lista de videos

    def getMovies(self):
        return self._movies
# retorna o video pelo id

    def getMoviesById(self, id, moviesList):
        movie = None
        for i, item in enumerate(moviesList):
            if item.getId() == id:
                movie = item
                return movie
        return movie
# retorna o vídeo com maior quantidade de curtidas

    def getMoviesMostLikes(self):
        movies = current_app.config["movie"]
        most = sorted(movies.getMovies(),
                      key=lambda x: x.getLike(), reverse=True)
        return most
