from kivymd.app import MDApp
from kivy.lang.builder import Builder
from styles import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField

class MainButtonScr(Screen):
    pass


class MenuScreen(Screen):
    pass

class UpdatesScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainButtonScr(name='mainbtn'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(UpdatesScreen(name='updatescreen'))
sm.add_widget(LoginScreen(name='loginscreen'))


class JoyPet(MDApp):

    def build(self):
        screen = Builder.load_string(screen_management)
        return screen

JoyPet().run()

#TODO: start tutorial from 5:47. You stopped watching at the moment when tutorial was showing
#TODO: the basics and now you are gonna learn how to ACTUALLY change the screeens