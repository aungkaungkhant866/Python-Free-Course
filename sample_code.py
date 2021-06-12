from kivymd.app import MDApp
from kivy.lang.builder import Builder

code = """
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDScreen:

            MDIconButton:
                id: plus
                icon: "plus-circle-outline"
                pos_hint: {"center_x": .1, "center_y": .1}
                user_font_size: "70sp"
                on_press: app.plus()

            MDIconButton:
                id: equal
                icon: "equal"
                pos_hint: {"center_x": .9, "center_y": .1}
                user_font_size: "70sp"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.equal()

            MDIconButton:
                id: one
                icon: "numeric-1-circle-outline"
                pos_hint: {"center_x": .1, "center_y": .3}
                user_font_size: "70sp"
                on_press: app.one()

            MDLabel:
                id: label
                text: ""
                font_size: '50sp'
                pos_hint: {"center_y": .8}

"""

class App(MDApp):
    def build(self):
        self.title = "Calculator"
        self.data = Builder.load_string(code)
        return self.data

    def plus(self):
        label = self.data.ids.label.text

        if label == "":
            label2 = label+""
            self.data.ids.label.text = label2

        else:
            data = open("calculator.txt", "w")
            data.write(label)
            data.close()
            self.data.ids.label.text = "+"

    def one(self):
        label = self.data.ids.label.text
        label2 = label+"1"
        self.data.ids.label.text = label2

    def equal(self):
        try:
            label = self.data.ids.label.text
            ans = open("calculator.txt", "r")
            ans2 = ans.read()

            if "+" in label:
                label2 = label.replace("+", "")
                ans3 = int(ans2) + int(label2)
                self.data.ids.label.text = str(ans3)

        except:
            self.data.ids.label.text = "Error"
            
if __name__ == "__main__":
    App().run()