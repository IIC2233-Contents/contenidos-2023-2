import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 110, 400)
        self.label = QLabel("Haz clic en mí", self)
        self.label.setGeometry(10, 90, 90, 100)
        self.label.setStyleSheet("background-color: lightblue;")
        self.label.show()
        self.click_dentro_del_label = False

        self.setMouseTracking(True)  # Activamos el tracking en nuestra ventana

        # Descomentar la siguiente línea si queremos seguir el mouse cuando estamos sobre el label
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.position().x()
        y = event.position().y()
        print(f"El mouse se mueve... está en {x},{y}")


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    window = MiVentana()
    window.show()
    sys.exit(app.exec())
