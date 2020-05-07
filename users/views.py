from .client_controller import ClientController
from .controller import UserContoller, AdminController, AdminControllerInApp
from movies.views import MovieViews, ProjectionViews


class AdminViews:
    def __init__(self):
        self.admin = AdminController()

    def login_as_admin(self):
        username = input('Username: ')
        password = input('Password: ')
        if self.admin.login(username=username, password=password) is True:
            return True
        return False

    def show_all_admins(self):
        admins = self.admin.show_all_admins()
        for admin in admins:
            print(f'{admin.id} | {admin.name}')

    def add_admin(self):
        username = input('Username: ')
        password = input('Password: ')
        self.admin.create_admin(username, password)

    def delete_admin(self):
        print('Please, choose which admin to delete (id number)')
        self.admin.show_all_admins()
        to_be_deleted_id = input('Input: ')
        deleted_admin = self.admin.delete_admin(to_be_deleted_id)
        print(f'You deleted {deleted_admin}')

    def add_movie(self):
        temp_movie_admin = MovieViews()
        temp_movie_admin.add_movie()

    def edit_movie(self):
        temp_movie_admin = MovieViews()
        temp_movie_admin.edit_movie()

    def add_projection(self):
        temp_projection_admin = ProjectionViews()
        temp_projection_admin.add_projection()

    def edit_projection(self):
        temp_projections_admin = ProjectionViews()
        temp_projections_admin.edit_projection()

    def show_all_movies(self):
        temp_movie_admin = MovieViews()
        temp_movie_admin.show_all_movies()

    def show_all_projections(self):
        temp_projections_admin = ProjectionViews()
        temp_projections_admin.show_all_projections()

    def delete_projection(self):
        temp_projections_admin = ProjectionViews()
        temp_projections_admin.delete_projection()

    def delete_movie(self):
        temp_movie_admin = MovieViews()
        temp_movie_admin.delete_movie()
