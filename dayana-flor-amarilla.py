import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Flor amarilla para @harolrop29

# Parámetros de la flor
num_petals = 7
petal_length = 2
petal_width = 1

fig, ax = plt.subplots(figsize=(6,6))

# Dibuja los pétalos
for i in range(num_petals):
    angle = i * 2 * np.pi / num_petals
    t = np.linspace(0, np.pi, 100)
    # Fórmula para pétalos
    x = petal_length * np.sin(t) * np.cos(angle) - petal_width * np.cos(t) * np.sin(angle)
    y = petal_length * np.sin(t) * np.sin(angle) + petal_width * np.cos(t) * np.cos(angle)
    ax.fill(x, y, color='yellow', edgecolor='orange')

# Dibuja el centro de la flor
center = plt.Circle((0, 0), 0.3, color='darkgoldenrod')
ax.add_patch(center)

ax.set_aspect('equal')
ax.axis('off')

st.title("Flor amarilla para @harolrop29 🌼")
st.pyplot(fig)