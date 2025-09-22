import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Hola, feliz inicio de primavera monga :) 🌷")

# Total de pasos para dibujar el tulipán
total_steps = 5

# Inicialización segura de variables en session_state
if "step" not in st.session_state:
    st.session_state.step = 1
if "animating" not in st.session_state:
    st.session_state.animating = True

# Si la animación está activa y aún no terminó, avanza cada 1 segundo
if st.session_state.animating and st.session_state.step < total_steps:
    time.sleep(1)
    st.session_state.step += 1
    st.experimental_rerun()

# Permite reiniciar la animación
if st.button("Reiniciar animación"):
    st.session_state.step = 1
    st.session_state.animating = True
    st.experimental_rerun()

# Cuando termina la animación, desactiva el flag
if st.session_state.step >= total_steps:
    st.session_state.animating = False

# Crear figura
fig, ax = plt.subplots(figsize=(5,7))
ax.set_xlim(-2,2)
ax.set_ylim(-1,7)
ax.axis('off')

# Paso 1: Tallo
if st.session_state.step >= 1:
    ax.plot([0,0], [0,4], color='green', linewidth=8)

# Paso 2: Hoja
if st
