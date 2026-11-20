import cv2

class Detector:
    """Detecta rostros con la camara usando OpenCV."""

    def __init__(self):
        self._clasificador = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def detectar(self, frame):
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostros = self._clasificador.detectMultiScale(gris, 1.3, 5)
        return rostros

    def abrir_camara(self):
        return cv2.VideoCapture(0)
