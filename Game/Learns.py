import streamlit as st
from PIL import Image
import numpy as np
import os

# ======================================
# CONFIGURACIÓN INICIAL DE LA PÁGINA
# ======================================
st.set_page_config(layout="wide")

# ======================================
# ESTILOS CSS PERSONALIZADOS
# ======================================
custom_css = """
<style>
    /* Contenedor principal */
    .hero-section {
        background-color: #0A0A0A;
        border-radius: 16px;
        padding: 4rem 2rem;
        margin-bottom: 3rem;
    }
    
    /* Tipografía */
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        color: white;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        color: #CCCCCC;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Botón CTA */
    .cta-button {
        background-color: #D94136;
        color: white !important;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
    }
    
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(217, 65, 54, 0.5);
    }
    
    /* Tarjetas de métricas */
    .metric-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-right: 1rem;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
    }
    
    .metric-label {
        color: #CCCCCC;
        font-size: 0.9rem;
    }
    
    /* Efectos para imágenes */
    .image-card {
        border-radius: 16px;
        transition: transform 0.5s;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
    }
    
    .image-card:hover {
        transform: perspective(1000px) rotateX(5deg) rotateY(-5deg);
    }
    
    .image-overlay-text {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Brush Script MT', cursive;
        color: white;
        font-size: 2rem;
    }
    
    .highlight-text {
        color: #00FF88;
        font-weight: bold;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ======================================
# SECCIÓN HERO (CONTENIDO PRINCIPAL)
# ======================================
with st.container():
    # Contenedor principal
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    
    # Layout de dos columnas
    col1, col2 = st.columns([1, 1], gap="large")
    
    # Columna izquierda (Texto y métricas)
    with col1:
        # Títulos
        st.markdown(
            '<h1 class="hero-title">Convirtiendo <span style="color: #CCCCCC">adolescentes ambiciosos</span> en Héroes</h1>',
            unsafe_allow_html=True
        )
        
        st.markdown(
            '<p class="hero-subtitle">Domina tu mente, transforma tu realidad. Programa de entrenamiento mental para jóvenes que quieren superar límites.</p>',
            unsafe_allow_html=True
        )
        
        # Botón CTA
        st.button(
            "¡Quiero unirme!",
            key="cta",
            help="Comienza tu transformación hoy"
        )
        
        # Métricas (3 columnas)
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.markdown(
                '<div class="metric-box"><div class="metric-value">20K+</div><div class="metric-label">Estudiantes (gratis)</div></div>',
                unsafe_allow_html=True
            )
            
        with metric_col2:
            st.markdown(
                '<div class="metric-box"><div class="metric-value">400+</div><div class="metric-label">Héroes</div></div>',
                unsafe_allow_html=True
            )
            
        with metric_col3:
            st.markdown(
                '<div class="metric-box"><div class="metric-value">4.9<span style="color: #D94136">★</span></div><div class="metric-label">Calificación</div></div>',
                unsafe_allow_html=True
            )
    
    # Columna derecha (Imágenes)
    with col2:
        # Debug: Verificar existencia de imágenes
        st.write("¿First_Image.png existe?", os.path.exists("Game/Images/First_image.png"))
        st.write("¿Second_Image.png existe?", os.path.exists("Game/Images/Second_image.png"))
        
        # Contenedor de imágenes con efecto 3D
        st.markdown("""
        <div style="position: relative;">
            <!-- Imagen principal -->
            <img src="Game/Images/First_image.png"
                 class="image-card" 
                 style="width: 80%; position: relative; z-index: 1;">
            <div class="image-overlay-text">Salud <span class="highlight-text">Mental</span></div>
            
            <!-- Imagen superpuesta -->
            <img src="Game/Images/Second_image.png"
                 class="image-card" 
                 style="width: 60%; position: absolute; right: 0; top: 30%; transform: rotate(-5deg); z-index: 2;">
        </div>
        """, unsafe_allow_html=True)
    
    # Cierre del contenedor
    st.markdown('</div>', unsafe_allow_html=True)