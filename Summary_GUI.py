from kivy.app import App
from kivy.core.window import Window
from ss import summary
import os


class Drop_window(Screen):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return


    def _on_file_drop(self, window, file_path):
        window.close()
        Get_all_text(file_path)
        return

def Get_all_text(directory):
    texts = []

    for filename in os.listdir(directory):
        suffix = '.txt'
        try:
            f = open(directory + str.encode('\\') + filename)
            texts.append(f.read())
        except Exception as e:
            pass
            
    summary(texts)

if __name__ == '__main__':
    Drop_window().run()
