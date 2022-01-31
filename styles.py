screen_management = """
ScreenManager:
    MainButtonScr:
    MenuScreen:
    UpdatesScreen:

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
        pos_hint: {"x":0.8, "top":0.8}

        

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