from kivymd.app import MDApp
from kivy.lang.builder import Builder
from styles import *
from kivy.uix.screenmanager import ScreenManager, Screen


class Start(Screen):
    pass


class MenuScreen(Screen):
    pass

class UpdatesScreen(Screen):
    pass

class LoginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Start(name='mainbtn'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(UpdatesScreen(name='updatescreen'))
sm.add_widget(LoginScreen(name='loginscreen'))


class JoyPet(MDApp):

    def build(self):
        screen = Builder.load_string(screen_management)
        self.title = 'JoyPet'
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "500"

        return screen

    @staticmethod
    def navigation_draw():
        print("NavBar")


JoyPet().run()
