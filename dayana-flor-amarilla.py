import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Configuración de la página
st.set_page_config(
    page_title="Feliz Primavera 🌷",
    page_icon="🌷",
    layout="wide"
)

# Título principal
st.title("Hola, feliz inicio de primavera monga :)")

# Placeholder para la animación
placeholder = st.empty()

# Coordenadas del tulipán (muy simple)
def get_tulipan_coords():
    # Tallo (línea vertical)
    tallo_x = [0, 0]
    tallo_y = [0, 3]
    
    # Pétalo izquierdo
    petalo_izq_x = [0, -0.8, -0.5, 0]
    petalo_izq_y = [3, 4.5, 5.2, 4.8]
    
    # Pétalo derecho  
    petalo_der_x = [0, 0.8, 0.5, 0]
    petalo_der_y = [3, 4.5, 5.2, 4.8]
    
    # Pétalo central
    petalo_centro_x = [0, 0, 0]
    petalo_centro_y = [3, 5.5, 4.8]
    
    # Hoja izquierda
    hoja_izq_x = [-0.1, -1.2, -0.8, -0.1]
    hoja_izq_y = [1.5, 2.5, 3.2, 2.8]
    
    # Hoja derecha
    hoja_der_x = [0.1, 1.2, 0.8, 0.1]
    hoja_der_y = [1.5, 2.5, 3.2, 2.8]
    
    return [
        (tallo_x, tallo_y, 'green', 'Tallo'),
        (hoja_izq_x, hoja_izq_y, 'lightgreen', 'Hoja izquierda'),
        (hoja_der_x, hoja_der_y, 'lightgreen', 'Hoja derecha'),
        (petalo_izq_x, petalo_izq_y, 'gold', 'Pétalo izquierdo'),
        (petalo_der_x, petalo_der_y, 'gold', 'Pétalo derecho'),
        (petalo_centro_x, petalo_centro_y, 'yellow', 'Pétalo central')
    ]

# Función para dibujar progresivamente
def dibujar_tulipan_animado():
    partes = get_tulipan_coords()
    
    # Configurar la figura
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.5, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('white')
    
    # Dibujar cada parte progresivamente
    for parte_idx, (x_coords, y_coords, color, nombre) in enumerate(partes):
        
        # Dibujar línea por línea
        for i in range(1, len(x_coords)):
            # Limpiar y redibujar todo hasta este punto
            ax.clear()
            ax.set_xlim(-2, 2)
            ax.set_ylim(-0.5, 6)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Dibujar partes anteriores completas
            for prev_idx in range(parte_idx):
                prev_x, prev_y, prev_color, _ = partes[prev_idx]
                ax.plot(prev_x, prev_y, color=prev_color, linewidth=3)
                ax.fill(prev_x, prev_y, color=prev_color, alpha=0.6)
            
            # Dibujar la parte actual hasta el punto i
            current_x = x_coords[:i+1]
            current_y = y_coords[:i+1]
            ax.plot(current_x, current_y, color=color, linewidth=3)
            
            # Si es el último punto de la parte, rellenar
            if i == len(x_coords) - 1:
                ax.fill(x_coords, y_coords, color=color, alpha=0.6)
            
            # Actualizar la visualización
            with placeholder.container():
                st.pyplot(fig, use_container_width=True)
            
            # Pausa para el efecto de animación
            time.sleep(0.8)

# Botón para iniciar la animación
if st.button("🎨 Has click aquí", type="primary"):
    dibujar_tulipan_animado()

st.write("👆Click arriba")
