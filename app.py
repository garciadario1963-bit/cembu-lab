import streamlit as st

# Configuración de página centrada y con ícono de pestaña
st.set_page_config(
    page_title="CEMBU - Conocimiento Territorial",
    page_icon="assets/1_CEMBU.png",
    layout="wide"
)

# Estilos CSS personalizados para la estética visual
st.markdown("""
    <style>
    /* Ocultar el espacio sobrante superior */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Banner Principal Header (Contenido en recuadro, no full-width) */
    .header-banner {
        background-color: #0e1117;
        color: white;
        padding: 30px 20px;
        border-radius: 10px;
        border-bottom: 4px solid #ea580c;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    .header-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }

    .header-logo {
        height: 50px;
        width: auto;
    }

    .header-title {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #ea580c;
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: 2px;
        margin: 0;
    }

    .header-subtitle {
        color: #d1d5db;
        font-size: 1.05rem;
        margin-top: 10px;
        font-weight: 300;
    }

    /* Tarjetas de Marcas / Unidades con Logo propio */
    .brand-card {
        text-align: center;
        padding: 15px;
    }

    .brand-card img {
        height: 70px;
        object-fit: contain;
        margin-bottom: 12px;
    }

    .brand-card h4 {
        color: #1f2937;
        margin-top: 5px;
        margin-bottom: 8px;
        font-weight: 700;
    }

    .brand-card p {
        color: #6b7280;
        font-size: 0.88rem;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Navegación Principal (Actualizada a "Página Principal")
menu_opcion = st.radio(
    "",
    ["Página Principal", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True
)

if menu_opcion == "Página Principal":

    # 2. Header / Banner con Logo CEMBU al lado del texto
    st.markdown("""
        <div class="header-banner">
            <div class="header-title-container">
                <img src="app/static/assets/1_CEMBU.png" class="header-logo" alt="Logo CEMBU" onerror="this.src='assets/1_CEMBU.png';">
                <span class="header-title">CEMBU</span>
            </div>
            <div class="header-subtitle">Conocimiento territorial para el desarrollo soberano</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Bloques Informativos Superiores
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="border-left: 4px solid #ea580c; padding-left: 12px;">
            <h4 style="color: #ea580c; margin:0;">1. Decisión & Ejecución</h4>
            <p style="font-size: 0.88rem; color: #4b5563; margin-top: 4px;">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="border-left: 4px solid #0284c7; padding-left: 12px;">
            <h4 style="color: #0284c7; margin:0;">2. Análisis & Modelización</h4>
            <p style="font-size: 0.88rem; color: #4b5563; margin-top: 4px;">Quienes estudian las complejidades socioeconómicas: academias e institutos.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="border-left: 4px solid #9333ea; padding-left: 12px;">
            <h4 style="color: #9333ea; margin:0;">3. Transformación Real</h4>
            <p style="font-size: 0.88rem; color: #4b5563; margin-top: 4px;">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # 4. Sección de Novedades (Carrusel) y Tablero Territorial
    col_nov, col_map = st.columns([1, 1])

    with col_nov:
        st.subheader("📌 Novedades & Actividades")
        # Espacio reservado para montar el componente interactivo de carrusel
        st.info("Espacio reservado para el Carrusel de Novedades")

    with col_map:
        st.subheader("📍 Tablero de Control Territorial & Modelización")
        st.caption("Monitor Territorial: Región Metropolitana / AMBA")
        st.write("[ Mapa / Monitor Interactivo ]")

    st.write("---")

    # 5. Sección de Marcas e Indicadores (Usando los logos alojados en assets)
    col_lab, col_matria, col_ohd = st.columns(3)

    with col_lab:
        st.markdown("""
        <div class="brand-card">
            <img src="app/static/assets/1_CEMBU.png" onerror="this.src='assets/1_CEMBU.png';">
            <h4>CEMBU LAB</h4>
            <p>Laboratorio de innovación, datos y metodologías territoriales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_matria:
        st.markdown("""
        <div class="brand-card">
            <img src="app/static/assets/2_MATRIA.png" onerror="this.src='assets/2_MATRIA.png';">
            <h4>MATRIA</h4>
            <p>Empresas sociales — Clusters, ZEE 360, Fondo de Hábitat.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_ohd:
        st.markdown("""
        <div class="brand-card">
            <img src="app/static/assets/3_OHD.png" onerror="this.src='assets/3_OHD.png';">
            <h4>OHD MONETARIO</h4>
            <p>Observatorio monetario — Hegemonía del dólar y coyuntura macrofinanciera.</p>
        </div>
        """, unsafe_allow_html=True)

    # 6. Pie de Página / Banner de Comunicación
    st.markdown("""
    <div style="background-color: #0e1117; color: white; padding: 30px; border-radius: 8px; margin-top: 40px;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #ea580c; margin-bottom: 8px;">CEMBU</h4>
                <p style="font-size: 0.85rem; color: #9ca3af; margin: 0;">Centro de Estudios Multidisciplinarios Manuel Baldomero Ugarte.<br>Conocimiento territorial para el desarrollo soberano.</p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #ea580c; margin-bottom: 8px;">Contacto Directo</h4>
                <p style="font-size: 0.85rem; color: #9ca3af; margin: 0;">📧 Email: contacto@cembu.org<br>📱 WhatsApp: 11-4993-8695</p>
            </div>
            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: #ea580c; margin-bottom: 8px;">Ubicación</h4>
                <p style="font-size: 0.85rem; color: #9ca3af; margin: 0;">📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina</p>
            </div>
        </div>
        <hr style="border-color: #374151; margin: 20px 0 15px 0;">
        <p style="text-align: center; font-size: 0.75rem; color: #6b7280; margin: 0;">© CEMBU - Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)
