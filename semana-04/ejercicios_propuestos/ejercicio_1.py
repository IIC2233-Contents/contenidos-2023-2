import sys
from PyQt6.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Mi Primera Ventana')


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana2 = MiVentana()
    lista_ventanas = []
    for cantidad in range(100):
        ventana = MiVentana()
        lista_ventanas.append(ventana)
    for ventana in lista_ventanas:
        ventana.show()
    sys.exit(app.exec())

# Editado el código para probar colapso abriendo 100 ventanas al mismo tiempo casi xddd.
