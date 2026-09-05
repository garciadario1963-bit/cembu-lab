import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuración de página e identidad visual en la pestaña
st.set_page_config(
    page_title="CEMBU",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definición de la Paleta Institucional CEMBU
COLOR_TERRACOTA = "#E3532B"
COLOR_VERDE_AGUA = "#338B85"
COLOR_AMARILLO = "#E8AC33"
COLOR_VIOLETA = "#77569B"
COLOR_FONDO_GRIS = "#F8F9FA"

# CSS Personalizado para elevar el diseño visual
st.markdown(f"""
    <style>
    /* Tipografía y fuentes generales */
    html, body, [class*="css"] {{
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}
    
    /* Títulos Principales */
    h1 {{
        color: {COLOR_TERRACOTA};
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }}
    
    h2, h3 {{
        color: {COLOR_VERDE_AGUA};
        font-weight: 600;
    }}

    /* Fondo y diseño del Menú Lateral */
    section[data-testid="stSidebar"] {{
        background-color: {COLOR_FONDO_GRIS};
        border-right: 3px solid {COLOR_VERDE_AGUA};
    }}
    
    /* Estilizado de Tarjetas Institucionales (Cards) */
    .cembu-card {{
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 20px;
        border-left: 5px solid {COLOR_TERRACOTA};
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }}
    
    .cembu-card-header {{
        color: {COLOR_TERRACOTA};
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 8px;
    }}

    .cembu-badge {{
        background-color: {COLOR_VERDE_AGUA};
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }}

    /* Botones estilo CEMBU */
    .stButton>button {{
        background-color: {COLOR_VERDE_AGUA};
        color: white !important;
        font-weight: 600;
        border-radius: 6px;
        border: none;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }}
    
    .stButton>button:hover {{
        background-color: {COLOR_TERRACOTA};
        color: white !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}
    </style>
""", unsafe_allow_html=True)

# 2. Carga Inteligente de Base de Datos
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
            return pd.read_excel(ruta), None
    return None, f"No se encontró el archivo '{nombre_archivo}'."

# 3. Menú Lateral con Iconografía Refinada
st.sidebar.markdown(f"<h2 style='color: {COLOR_TERRACOTA}; margin-bottom: 0;'>CEMBU</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 0.85rem; color: #6c757d;'>Centro de Estudios M. B. Ugarte</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

opcion_menu = st.sidebar.radio(
    "Navegación del Portal:",
    [
        "🏛️ Presentación e Inicio",
        "📊 Macro & Meso Económico",
        "🔀 Cruce de Variables",
        "👥 Microdatos (Censo / EPH)",
        "🇦🇷 CEMBU Matria",
        "🌐 CEMBU OHD",
        "💼 Proyectos & Consultoría",
        "📰 Publicaciones & Difusión"
    ]
)

df, error_carga = cargar_datos()

# 4. Modulo: Presentación e Inicio
if "Presentación e Inicio" in opcion_menu:
    
    # Encabezado Limpio Institucional
    st.markdown(f"""
        <div style="border-bottom: 3px solid {COLOR_TERRACOTA}; padding-bottom: 10px; margin-bottom: 25px;">
            <h1>Centro de Estudios Manuel Baldomero Ugarte</h1>
            <p style="font-size: 1.1rem; color: #555; margin-top: 5px;">Plataforma Integrada de Inteligencia Territorial y Analítica Económica</p>
        </div>
    """, unsafe_allow_html=True)

    # Tarjeta de Propósito Institucional
    st.markdown(f"""
        <div class="cembu-card">
            <div class="cembu-badge">Plataforma Oficial</div>
            <div class="cembu-card-header">Propósito Institucional</div>
            <p style="color: #333; line-height: 1.6; margin: 0;">
                El <strong>CEMBU</strong> es una plataforma orientada a la generación, procesamiento y modelización de datos cuantitativos y cualitativos para el diseño de políticas públicas de desarrollo territorial, con foco estratégico en la Provincia de Buenos Aires y la CABA.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Estado de la Base de Datos
    if df is not None:
        st.markdown(f"""
            <div style="background-color: #E8F5E9; border-left: 5px solid {COLOR_VERDE_AGUA}; padding: 12px 20px; border-radius: 6px; margin-bottom: 20px;">
                <span style="color: #2E7D32; font-weight: bold;"> Base de datos integrada correctamente</span>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🔍 Explorar Estructura de la Base de Datos Consolidada", expanded=False):
            st.dataframe(df.head(10), use_container_width=True)
    else:
        st.warning(f"⚠️ {error_carga}")

# 5. Resto de los módulos (Estructura base estilizada)
elif "Macro & Meso Económico" in opcion_menu:
    st.markdown(f"<h1>📊 Módulo Macro & Meso Económico</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.05rem; color: #666;'>Indicadores coyunturales, precios, actividad y análisis territorial.</p>", unsafe_allow_html=True)
    st.write("---")

elif "Cruce de Variables" in opcion_menu:
    st.markdown(f"<h1>🔀 Cruce de Variables</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.05rem; color: #666;'>Matriz de correlación entre variables estructurales y percepción social.</p>", unsafe_allow_html=True)
    st.write("---")

elif "Microdatos" in opcion_menu:
    st.markdown(f"<h1>👥 Módulo de Microdatos</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.05rem; color: #666;'>Procesamiento avanzado de microdatos (Censo y EPH).</p>", unsafe_allow_html=True)
    st.write("---")

else:
    st.markdown(f"<h1>{opcion_menu}</h1>", unsafe_allow_html=True)
    st.info("Módulo en fase de integración dentro del sistema CEMBU.")
