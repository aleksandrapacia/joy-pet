screen_management = """
ScreenManager:
    MainButtonScr:
    MenuScreen:
    UpdatesScreen:
    LoginScreen:

<MainButtonScr>:
    name: 'mainbtn'
    MDRectangleFlatButton:
        text: 'Menu'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'updatescreen'
    MDLabel:
        text: 'JoyPet'
        font_size: '100sp'
        bold: True
        italic: True
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'loginscreen'



<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'Welcome Ola!'
        halign: 'center' 
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'mainbtn'
        
<UpdatesScreen>:
    name: 'updatescreen'
    MDLabel:
        text: 'Looking for updates ...'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'mainbtn'
    
<LoginScreen>:
    name: 'loginscreen'
    MDTextField:
        mode: 'rectangle'
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width: 250
        hint_text: 'Enter username'
    MDTextField:
        text: 'Enter password'
        pos_hint: {'center_x':0.5,'center_y':0.2}
    MDLabel:
        pos_hint:{'x':0.3, 'center_y':0.2}
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        theme_text_color: 'Primary'
        font_style: 'H1'
        halign: 'center'
        
"""