from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


from kivy.modules import inspector
from kivy.core.window import Window
inspector.create_inspector(Window, App)



class BackgroundApp(App):
    def build(self):
        layout = FloatLayout()

        # Set the background image
        background = Image(source='images/background.jpeg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Add a label on top of the background image
        label = Label(text='Convert Your Black & White Image \n           into Colorfull',
                      size_hint=(10000, 100),
                      size=(5000, 100),
                      pos_hint={'center_x': .5, 'center_y': 0.90},
                      bold=True,
                      color=(1,1,1,1))  # Color in RGBA (white)
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    BackgroundApp().run()
