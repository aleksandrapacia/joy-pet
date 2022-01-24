screen_management = """
ScreenManager:
    LoginScreen:
    MenuScreen:
            
<MenuScreen>
    name: 'menu'
        MDRectangleFlatButton:
            text: 'Menu'
            pos_hint: {center_x: 0.5, center_y: 0.7}
            
    
<LoginScreen>
    name: 'login'
        MDLabel:
            text: 'Log in!'
            halign: 'center'
            
"""