from kivymd.app import MDApp
from kivy.lang.builder import Builder

code = """
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Calculator"
            right_action_items: [["refresh", lambda x: app.refresh()]]

        MDScreen:

            MDTextField:
                id: firstnum
                hint_text: "First Number"
                mode: "rectangle"
                pos_hint: {"center_y":.9}
                input_filter: "int"

            MDTextField:
                id: secondnum
                hint_text: "Second Number"
                mode: "rectangle"
                pos_hint: {"center_y":.8}
                input_filter: "int"

            MDLabel:
                id: answer
                text: "None"
                pos_hint: {"center_y":.7}

            MDRoundFlatIconButton:
                icon: "calculator"
                text: "Add"
                on_press: app.add()
                pos_hint: {"center_x":.5, "center_y":.6}

            MDRoundFlatIconButton:
                icon: "calculator"
                text: "Substract"
                on_press: app.substract()
                pos_hint: {"center_x":.5, "center_y":.5}

            MDRoundFlatIconButton:
                icon: "calculator"
                text: "Multiple"
                on_press: app.multiple()
                pos_hint: {"center_x":.5, "center_y":.4}

            MDRoundFlatIconButton:
                icon: "calculator"
                text: "Divide"
                on_press: app.divide()
                pos_hint: {"center_x":.5, "center_y":.3}
"""

class Main(MDApp):
    def build(self):
        self.title = "Calculator Program"
        self.data = Builder.load_string(code)
        return self.data

    def add(self):
        firstnum = int(self.data.ids.firstnum.text)
        secondnum = int(self.data.ids.secondnum.text)

        ans = firstnum + secondnum
        self.data.ids.answer.text = "The Answer is: "+str(ans)

    def substract(self):
        firstnum = int(self.data.ids.firstnum.text)
        secondnum = int(self.data.ids.secondnum.text)

        ans = firstnum - secondnum
        self.data.ids.answer.text = "The Answer is: "+str(ans)

    def multiple(self):
        firstnum = int(self.data.ids.firstnum.text)
        secondnum = int(self.data.ids.secondnum.text)

        ans = firstnum * secondnum
        self.data.ids.answer.text = "The Answer is: "+str(ans)

    def divide(self):
        firstnum = int(self.data.ids.firstnum.text)
        secondnum = int(self.data.ids.secondnum.text)

        ans = firstnum / secondnum
        self.data.ids.answer.text = "The Answer is: "+str(ans)

    def refresh(self):
        self.data.ids.firstnum.text = ""
        self.data.ids.secondnum.text = ""
        self.data.ids.answer.text = ""

Main().run()