screen_management = """
ScreenManager:
    Start:
    MenuScreen:
    UpdatesScreen:
    LoginScreen:

<Start>:
    name: 'mainbtn'
    MDRectangleFlatButton:
        text: 'Start'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'updatescreen'
    MDLabel:
        text: 'JoyPet'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '100sp'
        halign: 'center'
        italic: True
        bold: True
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
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                icon: 'bed'
                type: 'bottom'
                left_action_items: [["language-python", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()

        
<UpdatesScreen>:
    name: 'updatescreen'
    MDLabel:
        text: 'Updates'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '100sp'
        halign: 'center'
        italic: True
        bold: True

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'mainbtn'
    
<LoginScreen>:
    name: 'loginscreen'
    MDTextField:
        mode: 'rectangle'
        hint_text: 'Enter username'
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        
        width: 250
    MDTextField:
        mode: 'rectangle'
        hint_text: 'Enter password'
        pos_hint: {'center_x':0.5,'center_y':0.45}
        size_hint_x:None
        width:250
    MDLabel:
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '100sp'
        halign: 'center'
        italic: True
        bold: True
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'mainbtn'

    
"""




