from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

code = """
Windows:
    Login:
    Home:

<Login>:
    name: "login"
    MDScreen:
        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_y":.5}
            password: True
            password_mask: "*"

        MDLabel:
            id: label
            text: ""
            color: (1,0,0,1)
            pos_hint: {"center_y":.7}

        MDTextButton:
            text: "Login"
            pos_hint: {"center_x":.5, "center_y":.4}
            on_press: app.login()
            on_release:
                if password.text == "123456asd": app.root.current = "home"
                else: app.root.current = "login"
                root.manager.transition.direction = "left"
                app.refresh()

<Home>:
    name: "home"

    MDScreen:
        MDTextButton:
            text: "Back"
            pos_hint: {"center_x":.5, "center_y":.5}
            on_release:
                app.root.current = "login"
                root.manager.transition.direction = "right"

"""

class Login(Screen):
    pass

class Home(Screen):
    pass

class Windows(ScreenManager):
    pass

class Main(MDApp):
    def build(self):
        self.title = "Login System"
        self.data = Builder.load_string(code)
        f = open("password.txt", "r")
        password = f.read()
        if len(password) > 0:
            self.data.get_screen("login").ids.password.text = str(password)
            return self.data
        else:
            return self.data

    def login(self):
        password = self.data.get_screen("login").ids.password.text
        if password == "123456asd":
            self.data.get_screen("login").ids.label.text = ""
            f = open("password.txt", "w")
            f.write(password)
            f.close()

        else:
            self.data.get_screen("login").ids.label.text = "Incorrect Password"

    def refresh(self):
        self.data.get_screen("login").ids.label.text = ""
        self.data.get_screen("login").ids.password.text = ""

Main().run()