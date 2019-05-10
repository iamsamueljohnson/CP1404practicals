from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class SimpleApp(App):
    status_text = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Sam Smith", "David Bowie"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "SIMPLE"
        self.root = Builder.load_file('simple_app.kv')
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.name_box.add_widget(temp_label)
        return self.root


SimpleApp().run()
