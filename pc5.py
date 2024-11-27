# -*- coding: utf-8 -*-
"""PC5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NxM5yPEoRHIWkPFOaIJ5gK5A3_Gd4k3f
"""

import streamlit as st
from PIL import Image

# Configuración inicial de la página
st.set_page_config(
    page_title="Una experiencia aprendiendo a programar con python por Camila Zagaztizabal",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Encabezado principal
st.title("💻 Una experiencia aprendiendo a programar con python por Camila Zagaztizabal")
st.write("Les presento algunos retos que enfrenté, momentos de aprendizaje y consejos clave a lo largo del ciclo.")

# Sección: Introducción
st.header("🤖 Introducción")
st.write(
    """
    Personalmente, aprender a programar ha sido una experiencia llena de retos, pues nunca pensé hacerlo.
    Este camino me ha enseñado habilidades técnicas y sobre todo, tener paciencia. En esta página comparto mi breve historia
    con la programación y los obstáculos que enfrenté en su momento.
    """
)

# Imagen decorativa de programación
st.image("https://img.freepik.com/vector-premium/concepto-trabajo-programador-escena-personas-ilustracion-vectorial_198565-2479.jpg", caption="Mis primeros pasos en programación", use_container_width=True)

# Sección: Retos enfrentados
st.header("💡 Retos enfrentados")
st.write(
    """
    - **Conceptos abstractos:** Al inicio, entender estructuras de datos como listas o diccionarios fue un desafío.
    - **Depuración:** Aprender a leer mensajes de error fue algo que tomó un poco de tiempo.
    - **Persistencia:** Con práctica constante todo se pudo.
    """
)

# Sección: Momentos clave de mi aprendizaje
st.header("📒 Momentos clave de aprendizaje")
st.write(
    """
    - **Conceptos básicos:** Me fue fundamental entender conceptos claves y básicos en este nuevo mundo para mí.
    - **Primera práctica:** A partir de la primera práctica, decidó estudiar mucho más para cada una de las que me faltaban.
    - **Estructuras condicionales:** Uno de los temas que más disfrute aprender, por lo que lo relaciono con las decisiones que tomamos en el día.
    - **Estructuras iterativas:** Sintetizan muchas líneas de código, sin embargo es un tema que me sigue costando un poco.
    """
)

# Sección interactiva: Consejos para otros estudiantes
st.header("📏 Consejos para quienes están aprendiendo a programar")
st.write(
    """
    Si estás comenzando tu camino en programación, aquí tienes algunos consejos que me ayudaron:
    """
)
tips = st.radio(
    "Selecciona uno de los siguientes consejos:",
    ("Sé constante", "Aprende de tus errores", "Practica con los ejercicios de clase", "Disfruta el proceso")
)

if tips == "Sé constante":
    st.write("La prácica constante es fundamental. Dedicale un poco de tiempo todos los días a practicar y estudiar.")
elif tips == "Aprende de tus errores":
    st.write("Los errores son una oportunidad para aprender. Revisa las retroalimentaciones que te brindan en cada práctica.")
elif tips == "Practica con los ejercicios de clase":
    st.write("Realiza nuevamente a modo de práctica los ejercicios realizados en clase, así como los propuestos.")
elif tips == "Disfruta el proceso":
    st.write("Al inicio cuesta, pero al final del día te irás sabiendo algo más.")

# Sección: Reflexión final
st.header("🎯 Reflexión final")
st.write(
    """
    El curso de programación me ha ayudado mucho a descubrir capacidades que no conocía y desarrollar creatividad para resolver problemas del día.
    Hoy me siento más preparado para enfrentar nuevos desafíos, sin embargo para llegar a ello me costó horas de dedicación y esfuerzo.
    Espero que te ayude esta pequeña guía hecha con mucha dedicación y tiempo, pero por sobretodo poder ayudarte en este camino tan lindo.
    """
)

# Contacto
st.sidebar.title("📩 Contacto")
st.sidebar.write("Hecho por: Camila Zagastizabal - 20220925")
st.sidebar.write("Para cualquier duda al respecto contáctame en: a20220925@pucp.edu.pe.")
st.sidebar.write("Visita mi perfil de GitHub: https://github.com/camilaAriana.")