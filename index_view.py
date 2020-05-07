from users.views import AdminViews
from settings import ADMIN_PASSWORD
try:
    import Tkinter as tk
except Exception:
    import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tk.Button(self, text="Log in", command=lambda: master.switch_frame(PageOne)).pack()
        #tk.Button(self, text="Sign up", command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Log in as admin", command=lambda: master.switch_frame(LoginAsAdmin)).pack()

    def welcome():
        print('Welcome to HackCinema!')
        command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n 3 - log in as admin\n Input: '))
        admin_view = AdminViews()

        # if command == 1:
        #     return user_views.login()

        # if command == 2:
        #     return user_views.signup()

        # if command == 3:
        #     secret_password = input('Input the secret password: ')
        #     if secret_password == ADMIN_PASSWORD:
        #         return admin_view.login_as_admin()
        #     else:
        #         raise ValueError(f'Wrong password')

        # raise ValueError(f'Unknown command {command}.')


class LoginAsAdmin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.secret_password = tk.Entry(master)
        self.secret_password.pack()
        tk.Label(self, text="Secret password page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Frame.configure(self, bg='blue')
        tk.Button(self, text='Submit', command=lambda: self.check_password()).pack()

    def check_password(self):
        admin_view = AdminViews()
        password = self.secret_password.get()
        if password == ADMIN_PASSWORD:
            if admin_view.login_as_admin() is True:
                master = App()
                master.switch_frame(AdminOptions)
        else:
            raise ValueError(f'Wrong password')


class AdminOptions(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.command = tk.Entry(master)
        self.command.pack()
        tk.Label(self, text='''
            Choose a command:
            1 - show all admins
            2 - add admin
            3 - delete admin
            4 - add movie
            5 - add projection
            6 - show all movies
            7 - show all projections
            8 - edit movie
            9 - edit projection
            10 - delete projection
            11 - delete movie
            100 - exit''').pack(side="top", fill="x", pady=5)
        tk.Frame.configure(self, bg='black')
        tk.Button(self, text='Submit', command=lambda: self.admin_options()).pack()

    def admin_options(self):
        command = self.command.get()
        admin_views = AdminViews()
        if command == 1:
            return admin_views.show_all_admins()
        if command == 2:
            return admin_views.add_admin()
        if command == 3:
            return admin_views.delete_admin()
        if command == 4:
            return admin_views.add_movie()
        if command == 5:
            return admin_views.add_projection()
        if command == 6:
            return admin_views.show_all_movies()
        if command == 7:
            return admin_views.show_all_projections()
        if command == 8:
            return admin_views.edit_movie()
        if command == 9:
            return admin_views.edit_projection()
        if command == 10:
            return admin_views.delete_projection()
        if command == 11:
            return admin_views.delete_movie()
        if command == 100:
            return 'Exit'
        #raise ValueError('Error in admin_options')


def login_start():
    app = App()
    app.mainloop()
