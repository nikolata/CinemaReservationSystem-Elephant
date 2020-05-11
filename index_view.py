from users.client_view import ClientView
from users.views import AdminViews
from settings import ADMIN_PASSWORD
from users.models import UserModel
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

    def quit(self):
        self._frame.quit()


class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        header_frame = tk.Frame(self)
        header_frame.grid(row=0, column=0)
        tk.Label(header_frame, text="Cinema Reservation System", font=('Helvetica', 18, "bold"))\
            .pack()
        tk.Label(header_frame, text="Made by Nikola and Tanya", font=('Helvetica', 14, "bold"))\
            .pack()
        tk.Button(header_frame, text="Log in", command=lambda: master.switch_frame(LoginAsClient))\
            .pack()
        tk.Button(header_frame, text="Sign up", command=lambda: master.switch_frame(SighUp)).pack()
        tk.Button(header_frame, text="Log in as admin", command=lambda: master.switch_frame(LoginAsAdmin))\
            .pack()


class LoginAsAdmin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        header_frame = tk.Frame(master, pady=2)
        body_frame = tk.Frame(header_frame, pady=5)
        header_frame.pack(side='top')
        body_frame.pack(side='bottom')
        tk.Label(header_frame, text="Secret password page", font=('Helvetica', 18, "bold")).pack()

        tk.Label(body_frame, text="Username", font=('Helvetica', 10)).pack(side='left')
        self.username = tk.Entry(body_frame, width='10')
        self.username.pack(side='left')
        # # self.username.pack(side='left')
        frame_pass = tk.Frame(body_frame, pady=5)
        frame_pass.pack(side='bottom')
        tk.Label(frame_pass, text="Password", font=('Helvetica', 10)).pack(side='left')
        self.password = tk.Entry(frame_pass, show='*', width='10')
        self.password.pack(side='left')

        tk.Label(frame_pass, text="Secret pass", font=('Helvetica', 10)).pack(side='left')
        self.secret_password = tk.Entry(frame_pass, show='*', width='10')
        self.secret_password.pack(side='left')
        frame_btn = tk.Frame(frame_pass).pack(side='bottom')
        tk.Button(frame_btn, text='Submit', command=lambda: self.check_password()).pack(side='top')

    def check_password(self):
        admin_view = AdminViews()
        password = self.secret_password.get()
        if password == ADMIN_PASSWORD:
            if admin_view.login_as_admin(self.username.get(), self.password.get()) is True:
                master = App()
                master.switch_frame(AdminOptions)
            else:
                master = App()
                master.switch_frame(LoginPage)
        else:
            raise ValueError(f'Wrong password')


class LoginAsClient(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(master, text="Client Login", font=('Helvetica', 18, 'bold')).pack(side='top')
        body_frame = tk.Frame(master, pady=2)
        body_frame.pack(side='top')
        tk.Label(body_frame, text="Username", font=('Helvetica', 10)).pack(side='left')
        self.username = tk.Entry(body_frame, width=15)
        self.username.pack(side='left')
        tk.Label(body_frame, text="Password", font=('Helvetica', 10)).pack(side='left')
        self.password = tk.Entry(body_frame, show='*', width=15)
        self.password.pack(side='left')
        frame_btn = tk.Frame(body_frame).pack(side='bottom')
        tk.Button(frame_btn, text='Submit', command=lambda: self.log_in()).pack(side='top')

    def log_in(self):
        client_view = ClientView()
        result = client_view.login(self.username.get(), self.password.get())
        if result is False:
            text = "You haven't signed up or wrong input"
            tk.Label(self, text=text, font=('Helvetica', 20, 'bold')).pack(side='bottom')
            tk.Button(self.master, text="Go back", command=lambda: self.master.switch_frame(LoginPage)).pack()
        else:
            master = App()
            master.switch_frame(ClientCommands)


class SighUp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(master, text="Sign up", font=('Helvetica', 18, 'bold')).pack(side='top')
        body_frame = tk.Frame(master, pady=2)
        body_frame.pack(side='top')
        tk.Label(body_frame, text="Username", font=('Helvetica', 10)).pack(side='left')
        self.username = tk.Entry(body_frame, width=10)
        self.username.pack(side='left')
        tk.Label(body_frame, text="Password", font=('Helvetica', 10)).pack(side='left')
        self.password = tk.Entry(body_frame, show='*', width=10)
        self.password.pack(side='left')
        tk.Label(body_frame, text="Password again", font=('Helvetica', 10)).pack(side='left')
        self.password_again = tk.Entry(body_frame, show='*', width=10)
        self.password_again.pack(side='left')
        frame_btn = tk.Frame(body_frame).pack(side='bottom')
        tk.Button(frame_btn, text='Submit', command=lambda: self.sign_up()).pack(side='top')

    def sign_up(self):
        client_view = ClientView()
        try:
            if not client_view.signup(self.username.get(), self.password.get(), self.password_again.get()):
                text = 'Passwords should be with length at least 8 symbols,\n 1 capital letter and a special symbol'
                tk.Label(self, text=text, font=('Helvetica', 13, 'bold')).pack(side='bottom')
            else:
                master = App()
                master.switch_frame(ClientCommands)

        except ValueError:
            tk.Label(self, text="Passwords are not the same", font=('Helvetica', 20, 'bold')).pack(side='bottom')


class ClientCommands(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text='Show movies', command=lambda: self.client_commands(1)).pack()
        tk.Button(self, text='Show movie projections', command=lambda: self.client_commands(2)).pack()
        tk.Button(self, text='Make reservation', command=lambda: self.client_commands(3)).pack()
        tk.Button(self, text='Quit', command=lambda: master.quit()).pack()

    def client_commands(self, command):
        client_view = ClientView()
        if command == 1:
            client_view.commands(1)
        if command == 2:
            client_view.commands(2)
        if command == 3:
            client_view.commands(3)


class AdminOptions(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text='Show all admins', command=lambda: self.admin_options(1)).pack()
        tk.Button(self, text='Add admin', command=lambda: self.admin_options(2)).pack()
        tk.Button(self, text='Delete admin', command=lambda: self.admin_options(3)).pack()
        tk.Button(self, text='Add movie', command=lambda: self.admin_options(4)).pack()
        tk.Button(self, text='Add projection', command=lambda: self.admin_options(5)).pack()
        tk.Button(self, text='Show all movies', command=lambda: self.admin_options(6)).pack()
        tk.Button(self, text='Show all projections', command=lambda: self.admin_options(7)).pack()
        tk.Button(self, text='Edit movie', command=lambda: self.admin_options(8)).pack()
        tk.Button(self, text='Edit projection', command=lambda: self.admin_options(9)).pack()
        tk.Button(self, text='Delete projection', command=lambda: self.admin_options(10)).pack()
        tk.Button(self, text='Delete movie', command=lambda: self.admin_options(11)).pack()
        tk.Button(self, text='Quit', command=lambda: master.quit()).pack()

    def admin_options(self, command):
        admin_views = AdminViews()
        if command == 1:
            admin_views.show_all_admins()
        if command == 2:
            admin_views.add_admin()
        if command == 3:
            admin_views.delete_admin()
        if command == 4:
            admin_views.add_movie()
        if command == 5:
            admin_views.add_projection()
        if command == 6:
            admin_views.show_all_movies()
        if command == 7:
            admin_views.show_all_projections()
        if command == 8:
            admin_views.edit_movie()
        if command == 9:
            admin_views.edit_projection()
        if command == 10:
            admin_views.delete_projection()
        if command == 11:
            admin_views.delete_movie()


def login_start():
    app = App()
    app.title("Cinema Reservation System")
    app.geometry('500x500')
    app.mainloop()
