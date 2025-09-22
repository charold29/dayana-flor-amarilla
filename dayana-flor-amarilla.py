import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Hola, feliz inicio de primavera monga :) 🌷")

# Total de pasos para dibujar el tulipán
total_steps = 5

# Estado en session_state
if "step" not in st.session_state:
    st.session_state.step = 1
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
if st.session_state.step >= 2:
    leaf_x = np.array([0,0.8,0.2,0])
    leaf_y = np.array([2,3,2.5,2])
    ax.fill(leaf_x, leaf_y, color='forestgreen')

# Paso 3: Base de la flor
if st.session_state.step >= 3:
    base_x = np.linspace(-0.8, 0.8, 100)
    base_y = 4 + 0.5 * np.sqrt(1 - (base_x/0.8)**2)
    ax.fill(base_x, base_y, color='gold', zorder=2)

# Paso 4: Pétalos laterales
if st.session_state.step >= 4:
    petal_xl = np.array([0, -0.7, -0.3, 0])
    petal_yl = np.array([4.5, 5.5, 6.2, 5.6])
    ax.fill(petal_xl, petal_yl, color='gold', zorder=2)
    petal_xr = np.array([0, 0.7, 0.3, 0])
    petal_yr = np.array([4.5, 5.5, 6.2, 5.6])
    ax.fill(petal_xr, petal_yr, color='gold', zorder=2)

# Paso 5: Pétalo central
if st.session_state.step >= 5:
    t = np.linspace(0, 1, 50)
    petal_cx = 0.25 * np.sin(np.pi*t)
    petal_cy = 4.5 + 2.5*t
    ax.fill(petal_cx, petal_cy, color='gold', zorder=3)

st.pyplot(fig)

if st.session_state.step < total_steps:
    st.info(f"Dibujando... Paso actual: {st.session_state.step} / {total_steps}")
else:
    st.success("¡El tulipán amarillo para Dayana está listo! 🌷")
