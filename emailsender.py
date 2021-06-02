from kivymd.app import MDApp
from kivy.lang.builder import Builder
import smtplib

code = """
MDScreen:
    MDTextField:
        id: user
        hint_text: "Email"
        pos_hint: {"center_y":.8}

    MDTextField:
        id: subject
        hint_text: "Subject"
        pos_hint:{"center_y":.7}

    MDTextField:
        id: content
        hint_text: "Content"
        multiline: True
        pos_hint:{"center_y":.6}

    MDTextButton:
        text: "Send"
        on_press: app.send()
        pos_hint: {"center_x":.5, "center_y":.4}

    MDLabel:
        id: success
        text: ""
        pos_hint: {"center_y":.3}
"""

class Main(MDApp):
    def build(self):
        self.title= "Email Sender"
        self.data = Builder.load_string(code)
        return self.data

    def send(self):
        email = self.data.ids.user.text
        subject = self.data.ids.subject.text
        mail = self.data.ids.content.text

        sender_email = "aungkaungkhant866@gmail.com"
        password = "aung@192"
        message = "Subject: {0}\n\n{1}".format(subject,mail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        self.data.ids.success.text = "Login Success"
        server.sendmail(sender_email, email, message)
        self.data.ids.success.text = "Email was sent to "+email

Main().run()