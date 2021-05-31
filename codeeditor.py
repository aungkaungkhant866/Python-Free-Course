import os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

code = """
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Menu"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
            right_action_items: [['play', lambda x: app.run_program()]]

        MDTextFieldRect:
            id: data
            hint_text: "Code"
            max_height: "200dp"
            multiline: True
            font_size: '32sp'

    MDNavigationDrawer:
        id: nav_drawer

        Content:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"

            MDLabel:
                text: "Code Hub"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "2021 © Lazy_Coder Corporation"
                size_hint_y: None
                font_style: "Caption"
                height: self.texture_size[1]

            ScrollView:

                DrawerList:
                    id: md_list
                        
                    MDList:

                        OneLineIconListItem:
                            text: "Open"
                            on_press: app.open_file()
                            on_release:
                                nav_drawer.set_state("close")
                            
                            IconLeftWidget:
                                icon: "folder-open-outline"
                                on_press: app.open_file()
                                on_release:
                                    nav_drawer.set_state("close")

                        OneLineIconListItem:
                            text: "Save"
                            on_press: app.save()
                            on_release:
                                nav_drawer.set_state("close")

                            IconLeftWidget:
                                icon: "content-save-edit-outline"
                                on_press: app.save()
                                on_release:
                                    nav_drawer.set_state("close")
"""

class Content(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass

class Main(MDApp):
    dialog = None

    def build(self):
        self.title = "Code Hub"
        self.data = Builder.load_string(code)
        return self.data

    def open_file(self):
        Tk().withdraw()
        path = askopenfilename(filetypes=[('Python Files', '*.py')])

        try:
            self.title = path + "-Code Hub"
            file = open(path, "r")
            code = file.read()
            self.data.ids.data.text = str(code)

        except:
            self.title = "Untitled-Code Hub"
            self.data.ids.data.text = ""

    def save(self):
        Tk().withdraw()
        code = self.data.ids.data.text
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])

        file = open(path, "w")
        file.write(code)
        file.close()

    def run_program(self):
        Tk().withdraw()
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        code = self.data.ids.data.text
        
        try:
            file = open(path, "w")
            file.write(code)
            file.close()
            os.system(f"gnome-terminal -e 'bash -c \"python3 {path}; exec bash\"'")

        except:
            pass

if __name__ == "__main__":
    Main().run()
