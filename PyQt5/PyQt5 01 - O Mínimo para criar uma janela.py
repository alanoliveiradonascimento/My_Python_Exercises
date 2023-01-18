# Importando os Módulos QApplication e QWidget da biblioteca PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

# Diferente do Tkinter, o Qt5 encara a janela como um Widget.
# Sendo assim não basta apenas declarar app = QApplication([])
# temos que criar a widget da janela para que, esta, seja mostrada na tela: janela = QWidget()
# e, em seguida, devemos dar um comando para mostrar esse widget: janela.show()
# Parecido com o que faríamos utilizando .pack(), .place() ou .grid() com os widgets do Tkinter


app = QApplication([])  # Manipulador da aplicação
janela = QWidget()  # Criando a widget de janela
janela.show()  # Mostra a widget janela na tela
app.exec()  # Executa a aplicação que conterá a widget janela e a mostrará
