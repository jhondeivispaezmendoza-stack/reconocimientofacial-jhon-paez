import tkinter as tk
from tkinter import messagebox
from servicios.detector import Detector
from modelos.gestor_personas import GestorPersonas

class VentanaPrincipal:
    def __init__(self):
        self.gestor = GestorPersonas()
        self.detector = Detector()
        self.ventana = tk.Tk()
        self.ventana.title("Reconocimiento Facial - Jhon Paez")
        self.ventana.geometry("400x300")

        tk.Label(self.ventana, text="Reconocimiento Facial", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(self.ventana, text="Sistema de registro y reconocimiento").pack(pady=5)

        tk.Button(self.ventana, text="Registrar Persona", width=30, command=self.registrar).pack(pady=10)
        tk.Button(self.ventana, text="Reconocer Rostro", width=30, command=self.reconocer).pack(pady=10)
        tk.Button(self.ventana, text="Ver Personas", width=30, command=self.ver_personas).pack(pady=10)

    def registrar(self):
        messagebox.showinfo("Registrar", "Funcion de registro en desarrollo")

    def reconocer(self):
        messagebox.showinfo("Reconocer", "Abriendo camara para reconocer...")

    def ver_personas(self):
        personas = self.gestor.listar()
        if not personas:
            messagebox.showinfo("Personas", "No hay personas registradas")
        else:
            texto = "\n".join([f"{p.id} - {p.nombre}" for p in personas])
            messagebox.showinfo("Personas", texto)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.iniciar()
