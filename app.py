import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuración de página e identidad visual en la pestaña (Solo CEMBU)
st.set_page_config(
    page_title="Observatorio CEMBU",
    page_icon="📊",
    layout="wide"
)

# Paleta Institucional CEMBU
COLOR_TERRACOTA = "#E3532B"
COLOR_VERDE_AGUA = "#338B85"
COLOR_AMARILLO = "#E8AC33"
COLOR_VIOLETA = "#77569B"

# Estilos visuales institucionales
st.markdown(f"""
    <style>
    /* Estilos generales y títulos */
    h1, h2, h3 {{
        color: {COLOR_TERRACOTA};
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}
    
    /* Personalización del menú lateral */
    section[data-testid="stSidebar"] {{
        background-color: #f8f9fa;
        border-right: 2px solid {COLOR_VERDE_AGUA};
    }}
    
    /* Color de acento en botones */
    .stButton>button {{
        background-color: {COLOR_VERDE_AGUA};
        color: white;
        border-radius: 6px;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: {COLOR_TERRACOTA};
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# 2. Función para cargar datos (sirve para Local y Web)
@st.cache_data
def cargar_datos():
    nombre_archivo = "base_de_datos_consolidada 23-08-26.xlsx"
    
    # Intentar buscar en rutas locales probables
    rutas_posibles = [
        nombre_archivo,
        os.path.join("Datos procesados", "macro meso", nombre_archivo),
        os.path.join(r"C:\Archivos CEMBU\Datos procesados\macro meso", nombre_archivo)
    ]
    
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            return pd.read_excel(ruta), None
            
    return None, f"No se encontró el archivo '{nombre_archivo}'. Verificá que esté en la misma carpeta o subido al repositorio."

# 3. Menú Lateral de Navegación
st.sidebar.title("Menú Institucional")
st.sidebar.markdown("---")

opcion_menu = st.sidebar.radio(
    "Seleccioná el módulo:",
    [
        "🏛️ Presentación e Inicio",
        "📈 Macro & Meso Económico / Territorial",
        "🔀 Cruce de Variables (Estructural vs. Percepción)",
        "👥 Microdatos (Censo + EPH)",
        "🇦🇷 CEMBU Matria (Modelo Productivo)",
        "🌐 CEMBU OHD (Hegemonía del Dólar)",
        "💼 CEMBU Proys & Consultoría",
        "📰 Publicaciones y Difusión"
    ]
)

# Intentar cargar la base de datos
df, error_carga = cargar_datos()

if error_carga:
    st.warning(f"⚠️ Aviso sobre la Base de Datos: {error_carga}")

# 4. Contenido según sección seleccionada
if "Presentación e Inicio" in opcion_menu:
    st.title("Observatorio CEMBU")
    st.subheader("Centro de Estudios Manuel Baldomero Ugarte")
    
    st.info("""
    **Propósito Institucional:**  
    El **CEMBU** es la plataforma orientada a la generación, procesamiento y modelización de datos para el diseño de políticas públicas de desarrollo territorial, con foco en la Provincia de Buenos Aires y la CABA.
    """)
    
    if df is not None:
        st.success(" Base de datos cargada correctamente.")
        st.write("Vista previa de los datos:", df.head())

elif "Macro & Meso Económico" in opcion_menu:
    st.title("📈 Módulo Macro & Meso Económico / Territorial")
    st.write("Análisis de indicadores coyunturales y estructurales.")

elif "Cruce de Variables" in opcion_menu:
    st.title("🔀 Cruce de Variables (Estructural vs. Percepción)")
    st.write("Matriz de cruce entre variables objetivas e indicadores de opinión pública.")

elif "Microdatos" in opcion_menu:
    st.title("👥 Módulo de Microdatos (Censo + EPH)")
    st.write("Procesamiento de datos censales y de la Encuesta Permanente de Hogares.")

else:
    st.title(opcion_menu)
    st.write("Módulo en desarrollo dentro del Observatorio CEMBU.")
