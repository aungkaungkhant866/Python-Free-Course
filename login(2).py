from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, ScreenManagerException

class MainScreen(Screen):
    pass

class Login(Screen):
    pass

class SignUp(Screen):
    pass

class Home(Screen):
    pass

class Manager(ScreenManager):
    pass

class Main(MDApp):
    def build(self):
        self.title = "Login System"
        self.data = Builder.load_file("login(2).kv")

        file = open("username.txt", "r")
        username = file.read()

        if len(username) > 0:
            self.data.get_screen("main").ids.btn.text = "Home"
            self.data.get_screen("main").ids.btn.icon = "home-circle-outline"
            self.data.get_screen("home").ids.username.text = "Welcome, "+username
            return self.data

        else:
            return self.data

    def login(self):
        email = self.data.get_screen("login").ids.email.text
        password = self.data.get_screen("login").ids.password.text

        file1 = open("email.txt", "r")
        file2 = open("password.txt", "r")
        file3 = open("username.txt", "r")

        email2 = file1.read()
        password2 = file2.read()
        username3 = file3.read()

        if (email == email2 and password == password2):
            self.data.get_screen("login").ids.success.text = "Logged In!"
            self.data.get_screen("main").ids.btn.text = "Home"
            self.data.get_screen("main").ids.btn.icon = "home-circle-outline"

            self.data.get_screen("login").ids.email.text = ""
            self.data.get_screen("login").ids.password.text = ""

            self.data.get_screen("home").ids.username.text = "Welcome, "+username3

        else:
            self.data.get_screen("login").ids.success.text = "Incorrect Email Or Password!"

    def signup(self):
        username = self.data.get_screen("signup").ids.username.text
        email = self.data.get_screen("signup").ids.email.text
        password = self.data.get_screen("signup").ids.password.text

        file1 = open("username.txt", "w")
        file1.write(username)
        file1.close()

        file2 = open("email.txt", "w")
        file2.write(email)
        file2.close()

        file3 = open("password.txt", "w")
        file3.write(password)
        file3.close()

        self.data.get_screen("signup").ids.success.text = "Created An Account!"
        self.data.get_screen("main").ids.btn.text = "Home"
        self.data.get_screen("main").ids.btn.icon = "home-circle-outline"

        self.data.get_screen("signup").ids.username.text = ""
        self.data.get_screen("signup").ids.email.text = ""
        self.data.get_screen("signup").ids.password.text = ""

        self.data.get_screen("home").ids.username.text = "Welcome, "+username

    def logout(self):
        self.data.get_screen("main").ids.btn.text = "Login/Sign Up"
        self.data.get_screen("main").ids.btn.icon = "account"

Main().run()