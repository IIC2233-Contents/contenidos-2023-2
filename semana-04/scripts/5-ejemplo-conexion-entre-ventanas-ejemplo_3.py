import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Ventana(QWidget):
    def __init__(self, titulo, x, y):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)
        self.show()

    def abrir_otra_ventana(self):
        self.hide()
        # Básicamente, el usar self para guardar la otra ventana es una solución al problema de que la ventana se destruye al salir de la función, y, sin recurrir a usar señales.
        self.otra_ventana = Ventana("Otra ventana", 300, 100)
        self.otra_ventana.show()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = Ventana("Inicial", 100, 100)
    sys.exit(app.exec())
