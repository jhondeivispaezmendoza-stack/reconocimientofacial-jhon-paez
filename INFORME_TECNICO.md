# INFORME TÉCNICO - RECONOCIMIENTO FACIAL
**Parcial III - Programación Orientada a Objetos**
**Estudiante:** Jhon Deivis Paez Mendoza

## 1. Introducción
Sistema que permite registrar personas con su foto, entrenar un modelo de reconocimiento facial y reconocer en tiempo real quién es la persona frente a la cámara.

## 2. Objetivos
- Registrar personas con foto y datos
- Entrenar modelo LBPH
- Reconocer rostros en vivo
- Aplicar POO: abstracción, encapsulamiento, herencia y polimorfismo

## 3. Tecnologías
Python, OpenCV, Tkinter, NumPy, Pillow, GitHub

## 4. Estructura del Proyecto
- modelos/persona.py: Clase Persona
- modelos/gestor_personas.py: Gestiona lista de personas
- servicios/reconocedor.py: Clase ReconocedorFacial con LBPH
- servicios/lbph.py: Entrenamiento y predicción
- interfaz/ventana_principal.py: Ventana con Tkinter
- main.py: Punto de entrada

## 5. POO Aplicada
**Abstracción:** Clase Persona solo expone nombre, id y foto.
**Encapsulamiento:** Atributos privados con getters/setters, _personas en Gestor.
**Herencia:** PersonaRegistrada hereda de Persona y agrega fecha_registro. ReconocedorLBPH hereda de ReconocedorBase.
**Polimorfismo:** Método reconocer() se comporta diferente en cada reconocedor. Método mostrar_info() diferente en Persona y PersonaRegistrada.

## 6. Funcionalidades
1. Registrar Persona: Guarda nombre, ID y captura 50 fotos del rostro.
2. Entrenar Modelo: Crea y entrena el modelo LBPH con las fotos guardadas.
3. Reconocer en Vivo: Abre cámara, detecta rostro y muestra nombre y confianza.

## 7. Cómo Ejecutar
pip install -r requirements.txt
python main.py

## 8. Conclusión
Se cumplió el objetivo. El sistema funciona con POO completa, interfaz gráfica y reconocimiento real con OpenCV.
