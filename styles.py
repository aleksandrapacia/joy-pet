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
        text: 'Menu'
        font_size: '100sp'
        halign: 'center'
        italic: True
        bold: True
        

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

nav_drawer ="""
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
"""