import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="CEMBU - Conocimiento Territorial",
    page_icon="assets/1_CEMBU.png",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* Contenedor Banner Negro */
    div[data-testid="stHorizontalBlock"]:has(p.header-title-text) {
        background-color: #0e1117;
        padding: 20px 25px;
        border-radius: 8px;
        border-bottom: 4px solid #ea580c;
        margin-bottom: 15px;
        align-items: center;
    }

    .header-title-text {
        color: #f97316 !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        margin: 0 !important;
        line-height: 1 !important;
        letter-spacing: 2px;
        text-align: center;
    }

    .header-subtitle-text {
        color: #f3f4f6 !important;
        font-size: 1.1rem !important;
        margin-top: 8px !important;
        margin-bottom: 0 !important;
        font-weight: 300 !important;
        text-align: center;
    }

    /* Centrado de imágenes en tarjetas */
    [data-testid="stImage"] img {
        margin: 0 auto;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 1. BANNER NEGRO SUPERIOR (Usando componentes nativos de Streamlit para asegurar la carga de la imagen)
with st.container():
    # Creamos un bloque visual contenedor
    st.markdown("""
        <div style="background-color: #0e1117; padding: 20px 30px; border-radius: 8px; border-bottom: 4px solid #ea580c; margin-bottom: 15px;">
    """, unsafe_allow_html=True)
    
    col_logo, col_text = st.columns([1, 4], vertical_alignment="center")
    
    with col_logo:
        st.image("assets/1_CEMBU.png", width=110)
        
    with col_text:
        st.markdown('<p class="header-title-text">CEMBU</p>', unsafe_allow_html=True)
        st.markdown('<p class="header-subtitle-text">Conocimiento territorial para el desarrollo soberano</p>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# 2. MENÚ DE NAVEGACIÓN (Debajo del banner negro)
menu_opcion = st.radio(
    "",
    ["Página Principal", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True
)

st.write("---")

# CONTENIDO DE LA PÁGINA PRINCIPAL
if menu_opcion == "Página Principal":

    # 3. Bloques de Objetivos / Pilares
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="border-left: 4px solid #ea580c; padding-left: 10px;">
            <h4 style="color: #ea580c; margin:0;">1. Decisión & Ejecución</h4>
            <p style="font-size: 0.85rem; color: #555;">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="border-left: 4px solid #0284c7; padding-left: 10px;">
            <h4 style="color: #0284c7; margin:0;">2. Análisis & Modelización</h4>
            <p style="font-size: 0.85rem; color: #555;">Quienes estudian las complejidades socioeconómicas: academias e institutos.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="border-left: 4px solid #9333ea; padding-left: 10px;">
            <h4 style="color: #9333ea; margin:0;">3. Transformación Real</h4>
            <p style="font-size: 0.85rem; color: #555;">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # 4. Sección Novedades & Tablero
    col_nov, col_map = st.columns([1, 1])

    with col_nov:
        st.subheader("📌 Novedades & Actividades")
        st.info("Espacio reservado para el Carrusel de Novedades")

    with col_map:
        st.subheader("📍 Tablero de Control Territorial & Modelización")
        st.caption("Monitor Territorial: Región Metropolitana / AMBA")
        st.write("[ Mapa / Monitor Interactivo ]")

    st.write("---")

    # 5. Unidades del CEMBU (Logos inferiores)
    col_lab, col_matria, col_ohd = st.columns(3)

    with col_lab:
        st.image("assets/CEMBU_LAB_logo.png", width=90)
        st.markdown("<h4 style='text-align: center;'>CEMBU LAB</h4>", unsafe_allow_html=True)
        st.caption("Laboratorio de innovación, datos y metodologías territoriales.")

    with col_matria:
        st.image("assets/2_MATRIA.png", width=90)
        st.markdown("<h4 style='text-align: center;'>MATRIA</h4>", unsafe_allow_html=True)
        st.caption("Empresas sociales — Clusters, ZEE 360, Fondo de Hábitat.")

    with col_ohd:
        st.image("assets/3_OHD.png", width=90)
        st.markdown("<h4 style='text-align: center;'>OHD MONETARIO</h4>", unsafe_allow_html=True)
        st.caption("Observatorio monetario — Hegemonía del dólar y coyuntura macrofinanciera.")

    # 6. Pie de Página
    st.markdown("""
    <div style="background-color: #0e1117; color: white; padding: 25px; border-radius: 8px; margin-top: 30px;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
            <div>
                <h4 style="color: #ea580c; margin-bottom: 5px;">CEMBU</h4>
                <p style="font-size: 0.8rem; color: #aaa;">Centro de Estudios Multidisciplinarios Manuel Baldomero Ugarte.<br>Conocimiento territorial para el desarrollo soberano.</p>
            </div>
            <div>
                <h4 style="color: #ea580c; margin-bottom: 5px;">Contacto Directo</h4>
                <p style="font-size: 0.8rem; color: #aaa;">📧 Email: contacto@cembu.org<br>📱 WhatsApp: 11-4993-8695</p>
            </div>
            <div>
                <h4 style="color: #ea580c; margin-bottom: 5px;">Ubicación</h4>
                <p style="font-size: 0.8rem; color: #aaa;">📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 15px 0 10px 0;">
        <p style="text-align: center; font-size: 0.75rem; color: #777; margin: 0;">© CEMBU - Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)
