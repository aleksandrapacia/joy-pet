screen_management = """
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