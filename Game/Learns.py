import streamlit as st
from PIL import Image
import os

# ======================================
# CONFIGURACIÓN INICIAL
# ======================================
st.set_page_config(
    page_title="Learnsy - Transformación Mental",
    page_icon="🧠",
    layout="wide"
)

# ======================================
# FUNCIONES AUXILIARES
# ======================================
def cargar_imagen(ruta_imagen, ancho=None):
    """Carga una imagen con manejo de errores"""
    try:
        imagen = Image.open(ruta_imagen)
        return imagen
    except Exception as e:
        st.error(f"Error al cargar {ruta_imagen}: {str(e)}")
        return None

# ======================================
# INTERFAZ PRINCIPAL
# ======================================
def main():
    # --- Sección Hero ---
    st.markdown("""
    <style>
    .hero-section {
        background-color: #0A0A0A;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    .metric-box {
        background: rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="hero-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")

        # --- Columna Izquierda (Texto) ---
        with col1:
            st.markdown('<h1 style="font-size: 2.5rem; color: white;">Convirtiendo <span style="color: #CCCCCC">adolescentes ambiciosos</span> en Héroes</h1>', unsafe_allow_html=True)
            st.markdown('<p style="color: #CCCCCC; font-size: 1.1rem;">Domina tu mente, transforma tu realidad. Programa de entrenamiento mental.</p>', unsafe_allow_html=True)
            
            # Botón CTA
            st.button("¡Quiero unirme!", key="cta_button")
            
            # Métricas
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown('<div class="metric-box"><h3>20K+</h3><p style="color: #CCCCCC">Estudiantes</p></div>', unsafe_allow_html=True)
            with m2:
                st.markdown('<div class="metric-box"><h3>400+</h3><p style="color: #CCCCCC">Héroes</p></div>', unsafe_allow_html=True)
            with m3:
                st.markdown('<div class="metric-box"><h3>4.9★</h3><p style="color: #CCCCCC">Calificación</p></div>', unsafe_allow_html=True)

        # --- Columna Derecha (Imágenes) ---
        with col2:
            # Debug: Mostrar rutas (opcional)
            if st.checkbox("Mostrar información de depuración"):
                st.write("Ruta actual:", os.getcwd())
                st.write("Contenido de Images/:", os.listdir("Images"))
                st.write("Ruta Images1.png:", os.path.abspath("Images/Image1.png"))
            
            # Contenedor de imágenes
            with st.container():
                # Imagen principal
                img_principal = cargar_imagen("Images/Image1.png")
                if img_principal:
                    st.image(img_principal, width=400, caption="Transformación personal")
                
                # Imagen superpuesta (con posición relativa)
                with st.container():
                    st.markdown("<div style='position:relative; top:-50px; left:50px;'>", unsafe_allow_html=True)
                    img_secundaria = cargar_imagen("Images/Image3.png")
                    if img_secundaria:
                        st.image(img_secundaria, width=250, caption="Resultados comprobados")
                    st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ======================================
# EJECUCIÓN
# ======================================
if __name__ == "__main__":
    main()