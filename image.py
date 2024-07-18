from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):

    def build(self):
        image = Image(source="avto.jpg")
        box_layout = BoxLayout()
        box_layout.add_widget(image)

        return box_layout


if __name__ == "__main__":
    MyApp().run()