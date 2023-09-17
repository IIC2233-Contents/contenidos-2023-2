import sys
from time import sleep
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiThread(QThread):
    # Se define para la clase MiThread,
    # para que cada instancia tenga una propia
    senal_actualizar = pyqtSignal(int, str)

    def __init__(self, i, tiempo):
        super().__init__()
        self.indice = i
        self.tiempo = tiempo

    def run(self):
        for i in range(10):
            sleep(self.tiempo)
            self.senal_actualizar.emit(self.indice, str(i))

        sleep(self.tiempo)
        self.senal_actualizar.emit(self.indice, "Status: Qthread terminado")


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.threads = []
        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        # Definimos un montón de labels que corresponderán a un thread cada uno
        self.labels = {
            i: QLabel("Status: esperando Qthread", self) for i in range(1, 6)
        }
        self.boton = QPushButton("Ejecutar QThreads", self)
        self.boton.clicked.connect(self.ejecutar_threads)

        for i in range(1, 6):
            self.labels[i].setGeometry(10, (i - 1) * 30, 230, 30)

        self.boton.setGeometry(10, 150, 230, 30)
        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Qthreads")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_threads(self):
        """
        Este método crea cinco threads cada vez que se presiona el botón en la
        interfaz. Los threads recibirán como argumento el índice del label
        que les corresponde y el tiempo que toman entre cada iteración.
        """
        if any([thread.isRunning() for thread in self.threads]):
            return

        self.threads = []
        for i in range(1, 6):
            thread = MiThread(i, i / 10)
            # Se conecta la señal emitida por el thread a un método
            # de la ventana
            thread.senal_actualizar.connect(self.actualizar_labels)
            self.threads.append(thread)
            thread.start()

    def actualizar_labels(self, indice, texto):
        """
        Este método actualiza el label correspondiente según los datos
        enviados desde un thread a través del índice y aplica el texto.
        """
        self.labels[indice].setText(texto)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())
