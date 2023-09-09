import sys
from time import sleep
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiThread(QThread):
    """
    Esta clase representa un thread personalizado que será utilizado durante
    la ejecución de la GUI.
    """

    def __init__(self, senal_actualizar):
        super().__init__()
        self.senal_actualizar = senal_actualizar

    def run(self):
        for i in range(10):
            sleep(0.5)
            self.senal_actualizar.emit(str(i))

        sleep(0.5)
        self.senal_actualizar.emit("Status: Qthread terminado")


class MiVentana(QWidget):
    # Creamos una señal para manejar la respuesta del thread
    senal_thread = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.thread = None
        # Conectamos la señal del thread al método que maneja
        self.senal_thread.connect(self.actualizar_labels)

        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        self.label = QLabel("Status: esperando Qthread", self)
        self.boton = QPushButton("Ejecutar QThread", self)
        self.boton.clicked.connect(self.ejecutar_threads)

        self.label.setGeometry(10, 10, 230, 30)
        self.boton.setGeometry(10, 50, 230, 30)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Qthreads")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_threads(self):
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        # Aquí debemos ocupar isRunning en lugar de is_alive
        if self.thread is None or not self.thread.isRunning():
            self.thread = MiThread(self.senal_thread)
            self.thread.start()

    def actualizar_labels(self, evento):
        """
        Este método actualiza el label según los datos enviados desde el
        thread através del objeto evento. Para este ejemplo, el método
        recibe el evento, pero podría también no recibir nada.
        """
        self.label.setText(evento)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())
