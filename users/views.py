from .controller import AdminController
from movies.views import MovieView, ProjectionView
from decorators import atomic, login_required


class AdminViews:
    def __init__(self):
        self.admin = AdminController()

    def login_as_admin(self, username, password):
        if self.admin.login(username=username, password=password) is True:
            return True
        else:
            print('ERROR IN LOGIN')
        return False

    @atomic
    @login_required
    def show_all_admins(self):
        admins = self.admin.show_all_admins()
        for admin in admins:
            print(f'{admin.user_id} | {admin.user.name}')

    @atomic
    @login_required
    def add_admin(self):
        username = input('Username: ')
        password = input('Password: ')
        self.admin.create_admin(username, password)

    @atomic
    @login_required
    def delete_admin(self):
        print('Please, choose which admin to delete (id number)')
        self.admin.show_all_admins()
        to_be_deleted_id = input('Input: ')
        deleted_admin = self.admin.delete_admin(to_be_deleted_id)
        print(f'You deleted {deleted_admin}')

    @atomic
    @login_required
    def add_movie(self):
        temp_movie_admin = MovieView()
        temp_movie_admin.add_movie()

    @atomic
    @login_required
    def edit_movie(self):
        temp_movie_admin = MovieView()
        temp_movie_admin.edit_movie()

    @atomic
    @login_required
    def add_projection(self):
        temp_projection_admin = ProjectionView()
        temp_projection_admin.add_projection()

    @atomic
    @login_required
    def edit_projection(self):
        temp_projections_admin = ProjectionView()
        temp_projections_admin.edit_projection()

    @atomic
    @login_required
    def show_all_movies(self):
        temp_movie_admin = MovieView()
        temp_movie_admin.show_all_movies()

    @atomic
    @login_required
    def show_all_projections(self):
        temp_projections_admin = ProjectionView()
        temp_projections_admin.show_all_projections()

    @atomic
    @login_required
    def delete_projection(self):
        temp_projections_admin = ProjectionView()
        temp_projections_admin.delete_projection()

    @atomic
    @login_required
    def delete_movie(self):
        temp_movie_admin = MovieView()
        temp_movie_admin.delete_movie()
