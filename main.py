from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView, MapMarker
from kivymd.uix.fitimage import FitImage
from kivy.core.video import Video

from kivy.lang import Builder

KV = '''
MainLayout:
    MDScreenManager:
        id: main_screenmanager
        MDScreen:
            name: "lockscreen"
            id: lockcreen
            MDBoxLayout:
                orientation: "vertical"
                md_bg_color: 64/255, 64/255, 64/255, 1
                MDLabel:
                    text: "Password verivication"
                    halign: "center"
                    font_size: self.height/10    
'''

# Laad de KV-string


# Nu kun je je app zoals gewoonlijk init

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

class MainLayout(Screen):
    pass

if __name__ == '__main__':
    MainApp().run()
