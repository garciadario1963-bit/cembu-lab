import streamlit as st
import pandas as pd
import os

# 1. Configuración de página
st.set_page_config(
    page_title="CEMBU",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta de Colores CEMBU
COLOR_NARANJA = "#E3532B"
COLOR_VERDE = "#338B85"
COLOR_AMARILLO = "#E8AC33"
COLOR_VIOLETA = "#77569B"
COLOR_GRIS_TEXTO = "#6E6E6E"
COLOR_FONDO_GRIS = "#F8F9FA"

# CSS Personalizado
st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 18px !important;
    }}
    
    .cembu-super {{
        color: {COLOR_GRIS_TEXTO};
        font-size: 1rem !important;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 2px;
    }}
    
    .cembu-title {{
        color: {COLOR_NARANJA};
        font-size: 2.8rem !important;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 8px;
    }}
    
    .cembu-sub {{
        font-style: italic;
        color: #333333;
        font-size: 1.2rem !important;
        border-top: 1px solid #E0E0E0;
        padding-top: 8px;
        margin-top: 8px;
        margin-bottom: 25px;
    }}

    section[data-testid="stSidebar"] {{
        background-color: {COLOR_FONDO_GRIS};
        border-right: 3px solid {COLOR_VERDE};
    }}
    
    .cembu-card {{
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 22px;
        border-left: 6px solid {COLOR_NARANJA};
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# 2. Carga segura de datos
@st.cache_data
def cargar_datos():
    nombre_archivo = "base_de_datos_consolidada 23-08-26.xlsx"
    rutas_posibles = [
        nombre_archivo,
        os.path.join("Datos procesados", "macro meso", nombre_archivo),
        os.path.join(r"C:\Archivos CEMBU\Datos procesados\macro meso", nombre_archivo)
    ]
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            try:
                return pd.read_excel(ruta), None
            except Exception as e:
                return None, f"El archivo existe pero falló la lectura: {str(e)}"
    return None, f"No se encontró la base de datos en las rutas predefinidas."

df, error_carga = cargar_datos()

# 3. Menú Lateral
st.sidebar.markdown("<div class='cembu-super'>FAMILIA DE MARCAS</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='cembu-title' style='font-size: 2.2rem !important;'>CEMBU</div>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-style: italic; color: #555; font-size: 0.95rem;'>Conocimiento para la transformación social</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

opcion_menu = st.sidebar.radio(
    "Navegación del Portal:",
    [
        "🏛️ Presentación e Inicio",
        "📊 CEMBU LAB (Base Macro & Meso)",
        "🔀 Cruce de Variables",
        "👥 Microdatos (Censo / EPH)",
        "🇦🇷 CEMBU MATRIA",
        "🌐 CEMBU OHD (Hegemonía Dólar)",
        "💼 CEMBU PROYS & SERV. CONS.",
        "📰 PUBS / DIF. (Publicaciones)"
    ]
)

# 4. Modulos
if "Presentación e Inicio" in opcion_menu:
    st.markdown("<div class='cembu-super'>FAMILIA DE MARCAS CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Centro de Estudios Manuel Baldomero Ugarte — Conocimiento para la transformación social</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="cembu-card">
            <div style="color: {COLOR_VERDE}; font-weight: bold; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 5px;">Plataforma Institucional Integrada</div>
            <p style="color: #222; line-height: 1.7; font-size: 1.15rem; margin: 0;">
                El <strong>CEMBU</strong> es una plataforma orientada a la generación, procesamiento y modelización de datos cuantitativos y cualitativos para el diseño de políticas públicas de desarrollo territorial.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if df is not None:
        st.success(" Base de datos macro/meso integrada correctamente.")
    else:
        st.info(f"ℹ️ **Estado del sistema de datos:** {error_carga}")

elif "Microdatos" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>MICRODATOS</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Procesamiento estructurado de Censo y Encuesta Permanente de Hogares (EPH)</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Fuente Principal", value="INDEC / EPH")
    with col2:
        st.metric(label="Cobertura", value="PBA / CABA / Total País")
    with col3:
        st.metric(label="Nivel de Desagregación", value="Individual / Hogar")
        
    st.markdown("---")
    st.markdown("### 🔍 Consultor de Variables Socioeconómicas")
    
    fuente_sel = st.selectbox("Seleccionar Fuente de Datos:", ["EPH - Mercado de Trabajo", "EPH - Ingresos", "Censo Nacional de Población"])
    
    st.info(f"Módulo de procesamiento para **{fuente_sel}**. Listo para vinculación con bases parametrizadas.")

elif "CEMBU LAB" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>LAB.</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Base de datos y modelos predictivos — Inteligencia territorial para el desarrollo</div>", unsafe_allow_html=True)
    
    if df is not None:
        st.markdown("### 📊 Indicadores Macro & Meso Económicos")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning(f"⚠️ {error_carga}")

elif "CEMBU MATRIA" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>MATRIA</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Empresas sociales — Clusters, ZEE 360, Fondo de Hábitat</div>", unsafe_allow_html=True)

elif "CEMBU OHD" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>OHD</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Observatorio monetario — Hegemonía del dólar</div>", unsafe_allow_html=True)

elif "PROYS" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>PROYS. / SERV. CONS.</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Consultoría territorial y líneas de base — Inteligencia electoral</div>", unsafe_allow_html=True)

elif "PUBS" in opcion_menu:
    st.markdown("<div class='cembu-super'>CEMBU</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>PUBS/DIF.</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Publicaciones y difusión — Notas, informes, redes</div>", unsafe_allow_html=True)

else:
    st.markdown(f"<div class='cembu-title'>{opcion_menu}</div>", unsafe_allow_html=True)
