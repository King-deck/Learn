import streamlit as st
import base64
import os

# ======================================
# CONFIGURACIÓN INICIAL
# ======================================
st.set_page_config(
    page_title="Héroes - Transformación Educativa",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================
# FUNCIÓN PARA CONVERTIR IMÁGENES A BASE64
# ======================================
def image_to_base64(image_path):
    """Convierte imágenes a base64 para incrustación directa"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        st.error(f"Error al cargar {image_path}: {str(e)}")
        return ""

# ======================================
# ESTILOS CSS PERSONALIZADOS
# ======================================
st.markdown("""
<style>
    /* Fondo principal */
    .main {
        background-color: #0A0A0A;
        color: white;
    }
    
    /* Encabezado */
    .header {
        display: flex;
        justify-content: space-between;
        padding: 1rem 2rem;
    }
    
    /* Títulos */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        color: white;
        margin-bottom: 1rem;
        line-height: 1.2;
        text-transform: uppercase;
    }
    
    .subtitle {
        color: #CCCCCC;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Botón CTA */
    .cta-button {
        background-color: #D94136;
        color: white !important;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        border: none;
        font-size: 1rem;
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .cta-button:hover {
        background-color: #C0392B;
        transform: scale(1.05);
    }
    
    /* Tarjetas de métricas */
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin-right: 1rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        color: #CCCCCC;
        font-size: 0.9rem;
    }
    
    /* Efectos para imágenes */
    .main-image {
        border-radius: 16px;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        transform: perspective(1000px) rotateY(-5deg);
        position: relative;
        z-index: 1;
        width: 85%;
    }
    
    .overlay-image {
        border-radius: 12px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        position: absolute;
        right: 0;
        top: 15%;
        transform: rotate(-5deg);
        z-index: 2;
        width: 50%;
    }
    
    .mental-text {
        position: absolute;
        bottom: 30px;
        left: 30px;
        font-family: 'Brush Script MT', cursive;
        color: #00FF88;
        font-size: 2.5rem;
        z-index: 3;
    }
    
    .image-container {
        position: relative;
        height: 500px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ======================================
# SECCIÓN HERO (CONTENIDO PRINCIPAL)
# ======================================
def main():
    # Encabezado
    st.markdown("""
    <div class="header">
        <div style="font-size: 1.8rem; font-weight: 700; letter-spacing: 2px;">HÉROES</div>
        <button class="cta-button">¡QUIERO UNIRME!</button>
    </div>
    """, unsafe_allow_html=True)
    
    # Contenido principal
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        # Columna izquierda (Texto)
        with col1:
            st.markdown("""
            <h1 class="main-title">CONVIRTIENDO ADOLESCENTES AMBICIOSOS EN HÉROES</h1>
            <p class="subtitle">Héroes es una universidad online donde los jóvenes aprenden todo lo que no se enseña en el sistema educativo:</p>
            """, unsafe_allow_html=True)
            
            # Botón CTA adicional
            st.button("¡QUIERO UNIRME!", key="main_cta")
            
            # Métricas
            metrics = st.columns(3)
            with metrics[0]:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-value">20K+</div>
                    <div class="metric-label">Estudiantes</div>
                    <div class="metric-label">(gratis)</div>
                </div>
                """, unsafe_allow_html=True)
                
            with metrics[1]:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-value">400+</div>
                    <div class="metric-label">Héroes</div>
                </div>
                """, unsafe_allow_html=True)
                
            with metrics[2]:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-value">4.9<span style="color: #D94136">★</span></div>
                    <div class="metric-label">Calificación</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Columna derecha (Imágenes)
        with col2:
            # Debug: Verificar rutas de imágenes
            if st.checkbox("Mostrar información de depuración", False):
                st.write("Directorio actual:", os.getcwd())
                st.write("Contenido de Images/:", os.listdir("Images"))
                st.write("Ruta Image3.png:", os.path.abspath("Images/Image3.png"))
                st.write("Ruta Image2.png:", os.path.abspath("Images/Image2.png"))
            
            # Contenedor de imágenes con Base64
            st.markdown(f"""
            <div class="image-container">
                <!-- Imagen principal -->
                <img src="data:image/png;base64,{image_to_base64('Images/Image3.png')}" 
                     class="main-image">
                

            """, unsafe_allow_html=True)

# ======================================
# EJECUCIÓN PRINCIPAL
# ======================================
if __name__ == "__main__":
    main()