import os
import sys

# Agregar el directorio 'src' al PATH para que Python pueda encontrar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from controller.clustering import process_csv_and_cluster
from controller.database import Database
from console.secretconfig import PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT

def build_connection_string():
    return f"dbname={PGDATABASE}, user={PGUSER}, password={PGPASSWORD}, host={PGHOST}, port={PGPORT}"

class ClusteringApp(App):
    def build(self):
        self.file_path = ""
        self.num_clusters = 0
        connection_string = build_connection_string()
        self.db = Database(connection_string)
        self.db.connect()
        self.db.create_tables()

        layout = BoxLayout(orientation='vertical', padding=10)
        self.file_chooser = FileChooserListView()
        self.file_chooser.filters = ["*.csv"]
        self.file_chooser.bind(on_submit=self.selected)
        layout.add_widget(Label(text="Select CSV File:"))
        layout.add_widget(self.file_chooser)
        file_size_limit_label = Label(text="MAX FILE SIZE PERMITTED: 60KB", color=(1, 0, 0, 1))
        layout.add_widget(file_size_limit_label)
        self.num_clusters_input = TextInput(hint_text="Enter number of clusters", multiline=False)
        layout.add_widget(self.num_clusters_input)
        start_button = Button(text="Start Clustering", size_hint=(None, None), size=(150, 50))
        start_button.bind(on_press=self.start_clustering)
        layout.add_widget(start_button)
        return layout

    def selected(self, filechooser, file_path, *args):
        self.file_path = file_path[0] if file_path else ""

    def start_clustering(self, instance):
        try:
            self.num_clusters = int(self.num_clusters_input.text)
            if self.num_clusters <= 0 or self.num_clusters > 30:
                raise ValueError("Number of clusters invalid --> Only <30.")
        except ValueError as e:
            self.show_error_popup("Invalid Input", str(e))
            return

        if not self.file_path:
            self.show_error_popup("Error", "Please select a CSV file.")
            return

        file_size_kb = os.path.getsize(self.file_path) / 1024
        if file_size_kb > 60:
            self.show_error_popup("Error", "File size exceeds the limit (60KB). Please select a smaller file.")
            return

        success, message = process_csv_and_cluster(self.db, self.file_path, self.num_clusters)
        if success:
            self.show_success_popup("Success", message)
        else:
            self.show_error_popup("Error", message)

    def show_error_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_success_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    ClusteringApp().run()
