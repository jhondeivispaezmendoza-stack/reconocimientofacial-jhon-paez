# RECONOCIMIENTO FACIAL - PARCIAL INTEGRADOR POO

**Autor:** Jhon Deivis Paez Mendoza
**Materia:** Programacion Orientada a Objetos con Python
**Entrega:** Repositorio de GitHub

## 1. Descripcion del problema
Muchas veces se necesita identificar a una persona en una foto de forma rapida. Este proyecto permite detectar rostros en imagenes, registrar personas y reconocerlas despues.

## 2. Objetivos
- Aplicar POO: clases, herencia, polimorfismo, encapsulamiento y abstraccion.
- Crear una interfaz grafica funcional.
- Detectar, registrar y reconocer rostros en imagenes.

## 3. Funcionalidades
1. Cargar foto y detectar rostro: Muestra la imagen y marca el rostro con un cuadro.
2. Registrar persona: Guarda nombre y foto de la persona.
3. Reconocer persona: Compara una foto nueva con las registradas y dice quien es.

## 4. Tecnologias utilizadas
- Lenguaje: Python 3.10+
- Interfaz: Tkinter
- Procesamiento de imagenes: Pillow y OpenCV
- Herramienta: GitHub

## 5. Instalacion
1. Tener Python instalado.
2. Clonar el repositorio.
3. Instalar dependencias:
pip install -r requirements.txt

## 6. Ejecucion
Para iniciar la aplicacion ejecutar:
python main.py

## 7. Manual de usuario
1. Abrir la aplicacion.
2. Clic en "Cargar Foto" y elegir una imagen.
3. Clic en "Detectar Rostro" para ver el cuadro.
4. Escribir el nombre y dar clic en "Registrar Persona".
5. Para reconocer, cargar otra foto y dar clic en "Reconocer".

## 8. Estructura del proyecto
reconocimientofacial-jhon-paez/
├── main.py
├── modelos/persona.py
├── servicios/detector.py
├── interfaz/ventana_principal.py
├── docs/INFORME_TECNICO.md
├── requirements.txt
└── README.md

## 9. Autor
Jhon Deivis Paez Mendoza
