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
        pos_hint: {'center_x': 0.97, 'center_y': 0.9}
        text_size: (100,500)
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
    

"""