
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
        on_press: root.manager.current = 'nav_l'
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

<MenuScreen>:
    name: 'nav_l'
    Screen:
        MDNavigationLayout:
        
            ScreenManager:
            
                Screen:
                
                    BoxLayout:
                        orientation: 'vertical'
                        
                        MDToolbar:
                            title: "Navigation Drawer"
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                            
                            
                        ScreenManager:
                        
                            id: screen_manager
                            Screen:
                                name: "screen1"
                                MDLabel:
                                    text: "Screen 1"
                                    
                            Screen:
                                name: "screen2"
                                MDLabel:
                                    text: "Screen 2"
                                    
                                    
                        Widget:
                        
            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    
                    Image:
                        id: avatar
                        source: 'profile_img.png'
                        
    
                    ScrollView:
                        DrawerList:
                            id: md_list
                            MDList:
                                OneLineListItem:
                                    text: "Screen 1"
                                    on_press:
                                        nav_drawer.set_state("close")
                                        screen_manager.current = "screen1"
                                OneLineListItem:
                                    text: "Screen 2"
                                    on_press:
                                        nav_drawer.set_state("close")
                                        screen_manager.current = "screen2"
                
    
          
"""

