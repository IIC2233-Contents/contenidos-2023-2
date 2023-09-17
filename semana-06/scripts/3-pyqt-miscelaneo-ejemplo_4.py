import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from os.path import join


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Configuramos los widgets de la interfaz
        self.boton_sorpresa = QPushButton("Wooow", self)
        self.boton_empezar = QPushButton("Empezar musica de fondo", self)
        self.boton_parar = QPushButton("Parar música de fondo", self)
        self.boton_umineko = QPushButton("Umineko", self)

        self.boton_sorpresa.setGeometry(10, 10, 230, 30)
        self.boton_empezar.setGeometry(10, 50, 230, 30)
        self.boton_parar.setGeometry(10, 90, 230, 30)
        self.boton_umineko.setGeometry(10, 130, 230, 30)

        self.boton_sorpresa.clicked.connect(self.empezar_sonido_sorpresa)
        self.boton_empezar.clicked.connect(self.empezar_musica_fondo)
        self.boton_parar.clicked.connect(self.parar_musica_fondo)
        self.boton_umineko.clicked.connect(self.empezar_musica_umineko)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Sonidos")
        self.setGeometry(50, 50, 250, 200)

        # Opción MP3: QMediaPlayer junto a QAudioOutput
        # No te preocupes si te sale, en consola.
        #  "Could not update timestamps for skipped samples"
        self.media_player_mp3 = QMediaPlayer(self)
        self.media_player_mp3.setAudioOutput(QAudioOutput(self))
        file_url = QUrl.fromLocalFile(join("sounds", "waku-waku.mp3"))
        self.media_player_mp3.setSource(file_url)

        # Opción Wav: QSoundEffect
        self.media_player_wav = QSoundEffect(self)
        self.media_player_wav.setVolume(0.1)  # Opcional
        file_url = QUrl.fromLocalFile(join("sounds", "see-you-again.wav"))
        self.media_player_wav.setSource(file_url)

        self.media_player_umineko = QSoundEffect(self)
        self.media_player_umineko.setVolume(0.1)  # Opcional
        file_url = QUrl.fromLocalFile(join("sounds", "umineko.wav"))
        self.media_player_umineko.setSource(file_url)

        # Mostrar ventana
        self.show()

    def empezar_sonido_sorpresa(self):
        self.media_player_mp3.play()

    def empezar_musica_fondo(self):
        if not self.media_player_wav.isPlaying():
            self.media_player_wav.play()

    def parar_musica_fondo(self):
        if self.media_player_wav.isPlaying():
            self.media_player_wav.stop()

    def empezar_musica_umineko(self):
        if not self.media_player_umineko.isPlaying():
            self.media_player_umineko.play()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())
