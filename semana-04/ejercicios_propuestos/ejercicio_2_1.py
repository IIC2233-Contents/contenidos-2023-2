import sys
from PyQt6.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self, nombre_ventana: str, x: int, y: int, ancho: int, alto: int):
        super().__init__()
        self.setGeometry(x, y, ancho, alto)
        self.setWindowTitle(nombre_ventana)


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_1 = MiVentana('Ventana 1', 200, 100, 300, 300)
    ventana_2 = MiVentana('Ventana 2', 500, 100, 300, 300)
    ventana_3 = MiVentana('Ventana 3', 800, 100, 300, 300)
    ventana_4 = MiVentana('Ventana 4', 1100, 100, 300, 300)
    ventana_5 = MiVentana('Ventana 5', 1400, 100, 300, 300)
    lista_ventanas = [ventana_1, ventana_2, ventana_3, ventana_4, ventana_5]
    for ventana in lista_ventanas:
        ventana.show()
    sys.exit(app.exec())
