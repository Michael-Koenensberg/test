#подключение библиотек
#создание элементов интерфейса
#привязка элементов к вертикальной линии
#обработка событий
#запуск приложения
users = ['YourReal_naaaame']



from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Кнопка-определитель')
button = QPushButton('Генерэйшн')
text = QLabel('УЗНАЙ')
winner = QLabel('?')
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
def test():
   
    
    winner.setText(str(randint(1, 10)))
    
    

button.clicked.connect(test)
main_win.setLayout(line)
main_win.show()
app.exec_()