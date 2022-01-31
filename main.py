from kivymd.app import MDApp
from kivy.lang.builder import Builder
from styles import *
from kivy.uix.screenmanager import ScreenManager, Screen


class MainButtonScr(Screen):
    pass


class MainScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainButtonScr(name='menubtn'))
sm.add_widget(MainScreen(name='menu'))


class JoyPet(MDApp):

    def build(self):
        screen = Builder.load_string(screen_management)
        return screen


JoyPet().run()

#TODO: start tutorial from 5:47. You stopped watching at the moment when tutorial was showing
#TODO: the basics and now you are gonna learn how to ACTUALLY change the screeens