from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    LoginScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Menu'
        pos_hint: {'center_x':0.5,'center_y':0.5}

<LoginScreen>:
    name: 'login'
    MDRectangleFlatButton:
        text: 'Log in'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

"""


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))


class JoyPet(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


JoyPet().run()