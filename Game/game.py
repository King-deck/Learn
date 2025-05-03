import streamlit as st

# ======================================
# CONFIGURACIÓN BÁSICA
# ======================================
st.set_page_config(
    page_title="Consultoría Estratégica | Nova",
    page_icon="✨",
    layout="centered"
)

# CSS Minimalista
st.markdown("""
<style>
    .header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 1.5rem;
    }
    .subheader {
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    .divider {
        border-top: 1px solid #ecf0f1;
        margin: 2rem 0;
    }
    .service-card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .testimonial {
        font-style: italic;
        border-left: 3px solid #3498db;
        padding-left: 1rem;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ======================================
# CONTENIDO PRINCIPAL
# ======================================
st.markdown('<div class="header">Nova Consultoría Estratégica</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Soluciones inteligentes para negocios disruptivos</div>', unsafe_allow_html=True)

# Sección Hero
st.write("""
Ofrecemos **asesoramiento especializado** en transformación digital, estrategia de mercado 
y optimización de procesos. Nuestro enfoque basado en datos garantiza resultados medibles 
y sostenibles para tu organización.
""")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Servicios
st.markdown("### 📦 Nuestros Servicios")
services = [
    {"name": "Estrategia Digital", "desc": "Desarrollo de roadmap tecnológico personalizado para alcanzar tus objetivos de negocio."},
    {"name": "Análisis de Datos", "desc": "Extracción de insights accionables a partir de tus fuentes de información."},
    {"name": "Optimización de Procesos", "desc": "Rediseño de flujos de trabajo para maximizar eficiencia y reducir costos."}
]

for service in services:
    st.markdown(f"""
    <div class="service-card">
        <strong>{service['name']}</strong>
        <p>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Testimonios
st.markdown("### 💬 Lo que dicen nuestros clientes")
testimonials = [
    {"text": "Nova transformó nuestra operación logística, reduciendo tiempos de entrega en un 40%.", "author": "Carlos M., Director de Operaciones"},
    {"text": "El análisis de mercado que realizaron nos permitió identificar 3 nuevas líneas de negocio.", "author": "Ana L., CEO"}
]

for testimonial in testimonials:
    st.markdown(f"""
    <div class="testimonial">
        <p>"{testimonial['text']}"</p>
        <strong>- {testimonial['author']}</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Contacto
st.markdown("### 📩 Contacto")
with st.form("contact_form"):
    name = st.text_input("Nombre completo*")
    email = st.text_input("Email corporativo*")
    company = st.text_input("Empresa")
    message = st.text_area("Cuéntanos sobre tus necesidades*")
    submitted = st.form_submit_button("Enviar consulta")
    if submitted:
        st.success("¡Gracias! Nos pondremos en contacto en menos de 24 horas.")

# Footer
st.markdown("---")
st.markdown("""
<p style="text-align: center; color: #7f8c8d;">
    © 2024 Nova Consultoría Estratégica | 
    <a href="#" style="color: #7f8c8d;">Términos</a> | 
    <a href="#" style="color: #7f8c8d;">Privacidad</a>
</p>
""", unsafe_allow_html=True)