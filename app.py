import streamlit as st

# Configuración de página centrada
st.set_page_config(
    page_title="CEMBU - Conocimiento Territorial",
    page_icon="assets/cembu_logo.png",
    layout="wide"
)

# Estilos CSS personalizados para ajustar contenedores, fuentes y banner
st.markdown("""
    <style>
    /* Estilo del Header Principal (Contenido dentro del margen, no de lado a lado) */
    .header-banner {
        background-color: #0e1117;
        color: white;
        padding: 25px 30px;
        border-radius: 8px;
        border-bottom: 3px solid #ff4b4b;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .header-title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
    }
    
    .header-title {
        font-family: 'serif'; /* Podés cambiar la tipografía aquí */
        color: #ff4b4b;
        font-size: 2.2rem;
        font-weight: bold;
        letter-spacing: 2px;
        margin: 0;
    }

    .header-subtitle {
        color: #d1d5db;
        font-size: 1rem;
        margin-top: 8px;
    }

    /* Tarjetas del Footer y Secciones */
    .section-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        height: 100%;
    }
    
    .custom-icon {
        height: 28px;
        vertical-align: middle;
        margin-right: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Menú de Navegación (Con 'Página Principal' en lugar de 'Tablero de Control')
menu_opcion = st.radio(
    "",
    ["Página Principal", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True
)

if menu_opcion == "Página Principal":

    # 2. Banner Header (Con logo CEMBU al lado del texto y sin desbordar los márgenes)
    st.markdown("""
        <div class="header-banner">
            <div class="header-title-container">
                <!-- Reemplazar 'assets/cembu_logo.png' por el path o URL de tu logo -->
                <img src="https://via.placeholder.com/40" style="height: 40px;" alt="CEMBU Logo">
                <span class="header-title">CEMBU</span>
            </div>
            <div class="header-subtitle">Conocimiento territorial para el desarrollo soberano</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Bloques de Objetivos / Pilares
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="border-left: 4px solid #ff4b4b; padding-left: 10px;">
            <h4 style="color: #ff4b4b; margin:0;">1. Decisión & Ejecución</h4>
            <p style="font-size: 0.9rem; color: #555;">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="border-left: 4px solid #0066cc; padding-left: 10px;">
            <h4 style="color: #0066cc; margin:0;">2. Análisis & Modelización</h4>
            <p style="font-size: 0.9rem; color: #555;">Quienes estudian las complejidades socioeconómicas: academias e institutos.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div style="border-left: 4px solid #8a2be2; padding-left: 10px;">
            <h4 style="color: #8a2be2; margin:0;">3. Transformación Real</h4>
            <p style="font-size: 0.9rem; color: #555;">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # 4. Sección Novedades (Espacio listo para el Carrusel) & Tablero / Monitor
    col_nov, col_map = st.columns([1, 1])

    with col_nov:
        st.subheader("📌 Novedades & Actividades")
        # AQUÍ VA EL COMPONENTE DE CARRUSEL
        st.info("Espacio reservado para el Carrusel de Novedades")

    with col_map:
        st.subheader("📍 Tablero de Control Territorial & Modelización")
        st.caption("Monitor Territorial: Región Metropolitana / AMBA")
        # Aquí va el mapa folium/leaflet o iframe del monitor
        st.write("[ Mapa / Monitor Interactivo ]")

    st.write("---")

    # 5. Accesos a las Unidades / Observatorios (Con espacio para Logos Vectoriales/PNG)
    col_lab, col_matria, col_ohd = st.columns(3)

    with col_lab:
        st.markdown("""
        <h3>
            <img src="https://via.placeholder.com/24" class="custom-icon">
            CEMBU LAB
        </h3>
        <p style="color: #666; font-size: 0.9rem;">Laboratorio de innovación, datos y metodologías territoriales.</p>
        """, unsafe_allow_html=True)

    with col_matria:
        st.markdown("""
        <h3>
            <img src="https://via.placeholder.com/24" class="custom-icon">
            MATRIA
        </h3>
        <p style="color: #666; font-size: 0.9rem;">Observatorio de dinámicas productivas y desarrollo regional.</p>
        """, unsafe_allow_html=True)

    with col_ohd:
        st.markdown("""
        <h3>
            <img src="https://via.placeholder.com/24" class="custom-icon">
            OHD MONETARIO
        </h3>
        <p style="color: #666; font-size: 0.9rem;">Seguimiento y análisis de coyuntura macrofinanciera.</p>
        """, unsafe_allow_html=True)

    # 6. Banner Inferior de Contacto / Pie de página (Mantenido intacto como indicaste)
    st.markdown("""
    <div style="background-color: #0e1117; color: white; padding: 30px; border-radius: 8px; margin-top: 40px;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div>
                <h4 style="color: #ff4b4b;">CEMBU</h4>
                <p style="font-size: 0.85rem; color: #aaa;">Centro de Estudios Multidisciplinarios.<br>Conocimiento territorial para el desarrollo soberano.</p>
            </div>
            <div>
                <h4 style="color: #ff4b4b;">Contacto Directo</h4>
                <p style="font-size: 0.85rem; color: #aaa;">📧 Email: contacto@cembu.org<br>📱 WhatsApp: 11-4993-8695</p>
            </div>
            <div>
                <h4 style="color: #ff4b4b;">Ubicación</h4>
                <p style="font-size: 0.85rem; color: #aaa;">📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 20px 0 10px 0;">
        <p style="text-align: center; font-size: 0.75rem; color: #777; margin: 0;">© CEMBU - Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)
