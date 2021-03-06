
screen_management = """
ScreenManager:
    Start:
    MenuScreen:
    UpdatesScreen:
    LoginScreen:
    AboutUs:
    ContactScreen:
    


<Start>:
    name: 'mainbtn'
    MDRectangleFlatButton:
        text: 'Start'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'nav_l'
    MDRectangleFlatButton:
        text: 'Updates'
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
                            title: 'Navigation Drawer'
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                            
                        ScreenManager:
                            id: screen_manager
                            Screen:
                                name: "menu"
                                
                                ScrollView:
                                    size: self.size
                                    MDGridLayout:
                                        cols: 2
                                        size_hint_y: None
                                        height: self.minimum_height
                                        width: self.minimum_width
                                        spacing: '20dp'
                                        padding: '20dp'
                                        
                                        MDCard:
                                            orientation: 'vertical'
                                            padding: '8dp'
                                            size_hint: 1, None
                                            height: '210dp'
                                            elevation: 5
                                            border_radius: 20
                                            radius: [15]
                                            on_press: root.manager.current = 'aboutus_screen'
                                            MDLabel:
                                                text: 'About us'
                                                font_name: 'Quicksand'
                                                font_size: 20
                                                halign: 'center'
                                                size_hint_y: .2
                                                
                                                pos_hint: {'center_x':.5, 'center_y':0.9}
                                            Image:
                                                source: 'images/vector_aboutus.png'
                                                size: self.texture_size
                                                
                                        MDCard:
                                            orientation: 'vertical'
                                            padding: '8dp'
                                            size_hint: 1, None
                                            height: '210dp'
                                            elevation: 5
                                            border_radius: 20
                                            radius: [15]
                                            on_press: root.manager.current = 'contact_screen'
                                            MDLabel:
                                                text: 'Contact'
                                                font_name: 'Quicksand'
                                                font_size: 20
                                                halign: 'center'
                                                size_hint_y: .2
                                                
                                                pos_hint: {'center_x':.5, 'center_y':0.9}
                                            Image:
                                                source: 'images/contact.png'
                                                size: self.texture_size
                                                halign: 'center'
                                                pos_hint: {'center_x': 0.5, 'center_y':0.2}
                                                    
                                    
                            Screen:
                                name: "profile"
                                MDFloatLayout:
                                    md_bg_color: 1, 1, 1, 1
                                    MDFloatLayout:
                                        size_hint_x: 1
                                        size_hint_y: .33
                                        pos_hint: {'center_x': .5, 'center_y': .85}
                                        canvas:
                                            Color:
                                                rgb: (1,1,1,1)
                                            Rectangle: 
                                                size: self.size
                                                pos: self.pos
                                                source: 'images/background.jpg'
                                    MDFloatLayout:
                                        size_hint_x: .28
                                        size_hint_y: .30
                                        pos_hint: {'center_x':.5, 'center_y': .6}
                                        canvas:
                                            Color:
                                                rgb: (1,1,1,1)
                                            Ellipse:
                                                size: 200 , 200
                                                pos: self.pos
                                                angle_start: 0
                                                angle_end: 360

                                                source: 'images/ugly.jpg'
                                                                
                                
                        
                                

                        
            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    
                    Image:
                        id: avatar
                        source: 'profile_img.png'
                        
                    MDLabel:
                        text: '                     Aleksandra Pacia'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDLabel:
                        text: '                            username'
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    ScrollView:
                        DrawerList:
                            id: md_list
                            MDList:
                                OneLineListItem:
                                    text: "Menu"
                                
                                    on_press:
                                        nav_drawer.set_state("close")
                                        screen_manager.current = "menu"
                                OneLineListItem:
                                    text: "Profile"
                                    on_press:
                                        nav_drawer.set_state("close")
                                        screen_manager.current = "profile"

                                        
<AboutUs>:
    name: 'aboutus_screen'
    MDLabel:
        text: 'About us'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '80sp'
        halign: 'center'
        font_name: 'Quicksand'
        bold: True
    MDIconButton:
        icon: 'arrow-collapse-left'
        theme_icon_color: 'Custom'
        icon_color: app.theme_cls.primary_color
        on_press: root.manager.current = 'nav_l'
    
<ContactScreen>:
    name: 'contact_screen'
    MDLabel:
        text: 'Contact'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '80sp'
        halign: 'center'
        font_name: 'Quicksand'
        bold: True
    MDIconButton:
        icon: 'arrow-collapse-left'
        theme_icon_color: 'Custom'
        icon_color: app.theme_cls.primary_color
        on_press: root.manager.current = 'nav_l'
   
"""