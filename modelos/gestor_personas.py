from modelos.persona import Persona

class GestorPersonas:
    """Administra las personas registradas."""

    def __init__(self):
        self._personas = []

    def agregar(self, nombre, ruta_foto):
        persona = Persona(nombre, ruta_foto)
        self._personas.append(persona)
        return persona

    def listar(self):
        return self._personas

    def buscar(self, nombre):
        for p in self._personas:
            if p.nombre.lower() == nombre.lower():
                return p
        return None
