class Persona:
    """Representa a una persona registrada en el sistema."""

    def __init__(self, nombre, ruta_foto):
        self._nombre = nombre
        self._ruta_foto = ruta_foto

    @property
    def nombre(self):
        return self._nombre

    @property
    def ruta_foto(self):
        return self._ruta_foto

    def __str__(self):
        return f"Persona: {self._nombre}"
