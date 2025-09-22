import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle
import matplotlib.patches as patches

# Configuración de la página
st.set_page_config(
    page_title="Feliz Primavera 🌷",
    page_icon="🌷",
    layout="wide"
)

# Título principal
st.title("Hola, feliz inicio de primavera monga :) 🌷")

# Función para dibujar el tulipán
def dibujar_tulipan():
    fig, ax = plt.subplots(figsize=(10, 12))
    
    # Configurar límites y aspecto
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    
    # Ocultar ejes
    ax.axis('off')
    
    # Color de fondo suave
    fig.patch.set_facecolor('#f0f8ff')
    
    # Dibujar el tallo (verde)
    tallo = patches.Rectangle((-0.1, -2), 0.2, 4, 
                             facecolor='#228B22', 
                             edgecolor='#006400', 
                             linewidth=2)
    ax.add_patch(tallo)
    
    # Dibujar hojas (verde)
    # Hoja izquierda
    hoja_izq = patches.Ellipse((-1.2, 0.5), 1.5, 0.8, 
                              angle=45,
                              facecolor='#32CD32', 
                              edgecolor='#228B22',
                              linewidth=2)
    ax.add_patch(hoja_izq)
    
    # Hoja derecha
    hoja_der = patches.Ellipse((1.2, 0.5), 1.5, 0.8, 
                              angle=-45,
                              facecolor='#32CD32', 
                              edgecolor='#228B22',
                              linewidth=2)
    ax.add_patch(hoja_der)
    
    # Dibujar pétalos del tulipán (amarillo)
    # Pétalo central trasero
    petalo1 = patches.Ellipse((0, 4), 1.2, 2.5,
                             facecolor='#FFD700',
                             edgecolor='#FFA500',
                             linewidth=2,
                             alpha=0.9)
    ax.add_patch(petalo1)
    
    # Pétalo izquierdo
    petalo2 = patches.Ellipse((-0.8, 4.2), 1.0, 2.2,
                             angle=15,
                             facecolor='#FFFF00',
                             edgecolor='#FFA500',
                             linewidth=2,
                             alpha=0.9)
    ax.add_patch(petalo2)
    
    # Pétalo derecho
    petalo3 = patches.Ellipse((0.8, 4.2), 1.0, 2.2,
                             angle=-15,
                             facecolor='#FFFF00',
                             edgecolor='#FFA500',
                             linewidth=2,
                             alpha=0.9)
    ax.add_patch(petalo3)
    
    # Pétalo central delantero (más brillante)
    petalo4 = patches.Ellipse((0, 4.5), 0.8, 2.0,
                             facecolor='#FFFF66',
                             edgecolor='#FFD700',
                             linewidth=2)
    ax.add_patch(petalo4)
    
    # Agregar centro de la flor
    centro = Circle((0, 3.5), 0.2, 
                   facecolor='#FF8C00',
                   edgecolor='#FF6347',
                   linewidth=1)
    ax.add_patch(centro)
    
    # Agregar algunos detalles decorativos (pequeñas líneas en los pétalos)
    for i in range(3):
        ax.plot([0, 0], [3.2 + i*0.3, 3.4 + i*0.3], 
               color='#FFA500', linewidth=1, alpha=0.6)
    
    # Título en la imagen
    ax.text(0, 7, '🌷 ¡Feliz Primavera! 🌷', 
           ha='center', va='center', 
           fontsize=20, fontweight='bold',
           color='#FF69B4',
           bbox=dict(boxstyle="round,pad=0.3", 
                    facecolor='white', 
                    edgecolor='#FF69B4',
                    alpha=0.8))
    
    return fig

# Crear y mostrar el tulipán
st.write("## 🌸 Tu tulipán amarillo está aquí 🌸")

# Centrar la imagen
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig = dibujar_tulipan()
    st.pyplot(fig, use_container_width=True)

# Mensaje adicional
st.write("---")
st.markdown("""
### 🌺 ¡Que tengas un día lleno de flores y alegría! 🌺

La primavera trae consigo nuevos comienzos, colores vibrantes y la promesa de días más cálidos. 
¡Espero que este tulipán amarillo brighte tu día tanto como tú brighteas el mío! 

*¡Disfruta esta hermosa temporada!* ✨
""")

# Agregar algunos emojis decorativos
st.write("🌷 🌸 🌺 🌻 🌹 🌼 🌷 🌸 🌺 🌻 🌹 🌼")

# Footer
st.write("---")
st.write("*Hecho con ❤️ y Python para celebrar la primavera*")
