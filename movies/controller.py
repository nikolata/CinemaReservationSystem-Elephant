# from .movie_gateway import MovieGateway
# from .projection_gateway import ProjectionGateway


# class MovieController:
#     def __init__(self):
#         self.movie_gateway = MovieGateway()

#     def add_movie(self, name, rating):
#         self.movie_gateway.add_movie(name, rating)

#     def show_all_movies(self):
#         return self.movie_gateway.show_all_movies()

#     def get_all_movies_id(self):
#         return self.movie_gateway.get_all_movies_id()

#     def edit_movie(self, movie_id):
#         self.movie_gateway.edit_movie(movie_id)

#     def delete_movie(self, movie_id):
#         self.movie_gateway.delete_movie(movie_id)


# class ProjectionController:
#     def __init__(self):
#         self.projection_gateway = ProjectionGateway()

#     def add_projection(self, movie_id, movie_type, date, time):
#         temp = MovieController()
#         ids = temp.get_all_movies_id()
#         if movie_id in ids:
#             self.projection_gateway.add_projection(movie_id, movie_type, date, time)
#         else:
#             print('Wrong movie id!')

#     def show_all_projections(self):
#         return self.projection_gateway.show_all_projections()

#     def edit_projection(self, projection_id):
#         self.projection_gateway.edit_projection(projection_id)

#     def delete_projection(self, projection_id):
#         self.projection_gateway.delete_projection(projection_id)
