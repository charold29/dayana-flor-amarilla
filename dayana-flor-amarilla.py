import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Flor amarilla para Dayana 🌼")

st.write("""
¡Hola Dayana!  
Desliza el control para ver cómo se va dibujando tu flor amarilla, pétalo por pétalo.
""")

# Parámetros de la flor
total_petals = 7
petal_length = 2
petal_width = 1

# Slider para controlar el número de pétalos dibujados
num_petals = st.slider(
    "Número de pétalos dibujados:",
    min_value=1, max_value=total_petals, value=1
)

fig, ax = plt.subplots(figsize=(6,6))

# Dibuja los pétalos uno a uno
for i in range(num_petals):
    angle = i * 2 * np.pi / total_petals
    t = np.linspace(0, np.pi, 100)
    x = petal_length * np.sin(t) * np.cos(angle) - petal_width * np.cos(t) * np.sin(angle)
    y = petal_length * np.sin(t) * np.sin(angle) + petal_width * np.cos(t) * np.cos(angle)
    ax.fill(x, y, color='yellow', edgecolor='orange')

# Dibuja el centro de la flor solo si hay al menos 3 pétalos
if num_petals >= 3:
    center = plt.Circle((0, 0), 0.3, color='darkgoldenrod')
    ax.add_patch(center)

ax.set_aspect('equal')
ax.axis('off')

st.pyplot(fig)

st.info("¡Usa el slider para ver cómo aparece la flor amarilla de Dayana!")
