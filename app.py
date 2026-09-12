import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="CEMBU", layout="wide")

# 2. Estilos CSS personalizados (Encabezado oscuro + Reducción de espacios)
st.markdown("""
    <style>
    /* Reducir espacio superior general de Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }

    /* Ocultar barra superior por defecto de Streamlit para limpiar la vista */
    header[data-testid="stHeader"] {
        background-color: transparent;
    }

    /* ENCABEZADO ESTILO IMAGEN 2 */
    .cembu-header {
        background-color: #0b0f19;
        border-bottom: 3px solid #ff5722;
        padding: 15px 25px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-radius: 4px;
        margin-bottom: 10px;
    }

    .cembu-title-box {
        text-align: center;
        flex-grow: 1;
    }

    .cembu-title {
        color: #ff5722;
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin: 0;
        line-height: 1;
    }

    .cembu-subtitle {
        color: #d0d5dd;
        font-size: 0.95rem;
        margin-top: 4px;
        font-weight: 300;
    }

    .cembu-socials {
        display: flex;
        gap: 12px;
        color: #1565c0;
        font-size: 1.2rem;
    }

    /* Estilo del menú horizontal compacto */
    div[data-testid="stRadio"] > div {
        display: flex;
        justify-content: flex-start;
        gap: 15px;
    }

    /* Espaciado ajustado para las secciones de abajo */
    .section-box {
        margin-top: 5px;
    }
    </style>

    <!-- Estructura HTML del Encabezado Oscuro -->
    <div class="cembu-header">
        <div style="display: flex; align-items: center;">
            <span style="font-size: 2.2rem; margin-right: 10px;">📙</span>
        </div>
        <div class="cembu-title-box">
            <h1 class="cembu-title">CEMBU</h1>
            <div class="cembu-subtitle">Conocimiento territorial para el desarrollo soberano</div>
        </div>
        <div class="cembu-socials">
            <span>🌐</span> <span>🐦</span> <span>💼</span> <span>📷</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. Menú de navegación horizontal (como lo teníamos en la imagen 1)
opcion_menu = st.radio(
    "",
    ["Página Principal", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)

# 4. Los 3 Pilares en la parte superior con proximidad ajustada
col_pilar1, col_pilar2, col_pilar3 = st.columns(3)

with col_pilar1:
    st.markdown("<h4 style='color: #ff5722; border-left: 4px solid #ff5722; padding-left: 8px; margin-bottom: 2px;'>1. Decisión & Ejecución</h4>", unsafe_allow_html=True)
    st.caption("Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.")

with col_pilar2:
    st.markdown("<h4 style='color: #0288d1; border-left: 4px solid #0288d1; padding-left: 8px; margin-bottom: 2px;'>2. Análisis & Modelización</h4>", unsafe_allow_html=True)
    st.caption("Quienes estudian las complejidades socioeconómicas: academias e institutos.")

with col_pilar3:
    st.markdown("<h4 style='color: #7b1fa2; border-left: 4px solid #7b1fa2; padding-left: 8px; margin-bottom: 2px;'>3. Transformación Real</h4>", unsafe_allow_html=True)
    st.caption("Quienes protagonizan los avances sociales: actores territoriales y trabajadores.")

st.markdown("<hr style='margin: 15px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)

# 5. Estructura inferior en 2 columnas (Carrusel + Tablero Territorial)
col_izq, col_der = st.columns([1, 1])

with col_izq:
    st.markdown("<h4 style='margin-bottom: 5px;'>📌 Novedades & Actividades</h4>", unsafe_allow_html=True)
    st.markdown("**CLACSO EN LA FILUNI & MONITOR TERRITORIAL**")
    st.caption("Nuestras últimas actividades académicas y avances en análisis regional.")
    
    # Imagen/Carrusel compacto adentro del contenedor
    st.image(
        "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=800", 
        use_column_width=True,
        caption="2/2 — MONITOR TERRITORIAL: Mapas dinámicos e infraestructura regional"
    )

with col_der:
    st.markdown("<h4 style='margin-bottom: 5px;'>📍 Tablero de Control Territorial & Modelización</h4>", unsafe_allow_html=True)
    st.caption("Monitor Territorial: Región Metropolitana / AMBA")
    
    # Simulación/Contenedor del mapa/tablero
    st.image(
        "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=800",
        use_column_width=True,
        caption="Vista previa del mapa de control territorial"
    )
