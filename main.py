from kivymd.app import MDApp

"""
from kivymd.uix.screen import Screen
from widgets import *
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
"""
from kivymd.uix.screen import Screen
from kivymd.uix.list import ThreeLineListItem, MDList, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class JoyPet(MDApp):

    def build(self):
        screen = Screen()
        scroll = ScrollView()

        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(101):
            icon = IconLeftWidget(icon="bomb")
            items = ThreeLineAvatarListItem(text="Item " + str(i), secondary_text="jest to item nr" + " " + str(i),
                                            tertiary_text="and this is the third text")
            list_view.add_widget(items)
            items.add_widget(icon)

        screen.add_widget(scroll)

        return screen

        """
        self.theme_cls.primary_palette = "Yellow"
        button = MDRectangleFlatButton(text="Confirm",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       theme_text_color="Custom",
                                       text_color=(1, 0, 0, 1),
                                       line_color=(0, 0, 1, 1),
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen


    def show_data(self, obj):
        #when there is an empty space for username
        if self.username.text == "":
            check = "Please enter your username"
        else:
            check = "Click the continue button"

        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

        self.dialog = MDDialog(title="Username checking",
                                  text=check,
                                  size_hint=(0.7, 1),
                                  buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    """


JoyPet().run()


