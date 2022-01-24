from kivymd.app import MDApp
from kivy.lang.builder import Builder
from styles import *
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))


class JoyPet(MDApp):

    def build(self):
        screen = Builder.load_string(screen_management)
        return screen


JoyPet().run()