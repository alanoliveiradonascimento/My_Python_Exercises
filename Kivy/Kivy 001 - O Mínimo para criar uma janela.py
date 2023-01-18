# Importa a biblioteca App com as configurações da janela
from kivy.app import App

# Importa a bibliote de manipulaç~~ao de Label
from kivy.uix.label import Label

# Classe que chamará a função com a build da janela e retornará o Lable
class janela(App):
    def build(self):
        return Label(text="Hello Kivy!")

# Executa a aplicação
janela().run()
