import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuración de página y marca
st.set_page_config(
    page_title="Observatorio CEMBU Lab",
    page_icon="📊",
    layout="wide"
)

# Paleta Institucional CEMBU Lab
COLOR_TERRACOTA = "#E3532B"
COLOR_VERDE_AGUA = "#338B85"
COLOR_AMARILLO = "#E8AC33"
COLOR_VIOLETA = "#77569B"

# Función auxiliar robusta para convertir números
def limpiar_valor_numerico(serie):
    s_clean = serie.astype(str).str.replace("%", "", regex=False).str.strip()
    s_clean = s_clean.str.replace(",", ".", regex=False)
    return pd.to_numeric(s_clean, errors="coerce")

# 2. Carga optimizada de datos con caché
@st.cache_data
def cargar_datos_macro_meso():
    ruta = "base_de_datos_consolidada 23-08-26.xlsx"
    if os.path.exists(ruta):
        df = pd.read_excel(ruta, sheet_name="Datos_Formato_Largo")
        return df
    else:
        st.error(f"No se encontró el archivo consolidado en: {ruta}")
        return pd.DataFrame()

df_largo = cargar_datos_macro_meso()

# Mapeo de Tipos de Variable a las 5 Dimensiones Teóricas
MAPEO_DIMENSIONES = {
    "Población / Demografía": "1. Demografía, Hábitat y Estructura Social",
    "Vivienda / Hábitat": "1. Demografía, Hábitat y Estructura Social",
    "Barrios populares": "1. Demografía, Hábitat y Estructura Social",
    "Educación": "2. Estructura Productiva, Empleo y Capital Humano",
    "Empleo / Actividad económica": "2. Estructura Productiva, Empleo y Capital Humano",
    "Actividad Económica": "2. Estructura Productiva, Empleo y Capital Humano",
    "Infraestructura": "3. Infraestructura y Equipamiento Urbano",
    "Salud": "3. Infraestructura y Equipamiento Urbano",
    "Tecnología / Conectividad": "3. Infraestructura y Equipamiento Urbano",
    "Elecciones / Resultados electorales": "4. Comportamiento Electoral y Representación Política",
    "Percepción / Imagen política": "5. Percepción Ciudadana, Imagen y Clima de Opinión",
    "Situación económica percibida": "5. Percepción Ciudadana, Imagen y Clima de Opinión"
}

if not df_largo.empty:
    df_largo["Dimensión"] = df_largo["Tipo"].map(MAPEO_DIMENSIONES).fillna("Otras Dimensiones / Macro")

# 3. Encabezado principal y botón de recarga
col_title, col_btn = st.columns([4, 1])

with col_title:
    st.title("📊 Observatorio CEMBU Lab")
    st.caption("Base de datos e Inteligencia Territorial para el Desarrollo | Centro de Estudios Manuel Baldomero Ugarte")

with col_btn:
    st.write("")
    if st.button("🔄 Actualizar Base"):
        st.cache_data.clear()
        st.rerun()

# 4. Navegación lateral con las 6 solapas estructuradas
st.sidebar.header("Menú de Navegación")
modulo = st.sidebar.radio(
    "Seleccioná el módulo:",
    [
        "1. Presentación / Inicio",
        "2. Módulo Macro, Meso y Territorial",
        "3. Microdatos (Censo + EPH)",
        "4. Cruces Multivariables",
        "5. Informes y Publicaciones",
        "6. Staff / Quiénes Somos"
    ]
)

# 5. Enrutamiento según la solapa seleccionada
if modulo == "1. Presentación / Inicio":
    st.header("Presentación Institucional y Marco Teórico")
    st.write("Espacio destinado a la presentación general del observatorio, sus objetivos y el marco teórico del CEMBU Lab.")
    st.info("Próximamente se cargará el contenido institucional detallado.")

elif modulo == "2. Módulo Macro, Meso y Territorial":
    st.header("Módulo Macro, Meso y Territorial")
    st.write("Exploración de la base de datos consolidada actual con filtros por dimensión, escala territorial e indicadores.")
    
    # Aquí irá el motor del dashboard que ya veníamos armando
    if not df_largo.empty:
        st.success(f"Base de datos cargada correctamente ({len(df_largo)} registros).")
        # Selector rápido de prueba para verificar que el tablero responde
        dimension_sel = st.selectbox("Filtrar por Dimensión:", df_largo["Dimensión"].unique())
        df_filtrado = df_largo[df_largo["Dimensión"] == dimension_sel]
        st.dataframe(df_filtrado.head(10), use_container_width=True)
    else:
        st.warning("No hay datos disponibles para mostrar en el tablero.")

elif modulo == "3. Microdatos (Censo + EPH)":
    st.header("Microdatos (Censo + EPH)")
    st.write("Espacio reservado para la ingestión y análisis de microdatos censales y de hogares en archivos separados.")
    st.info("Módulo en preparación para incorporar nuevas fuentes e insumos.")

elif modulo == "4. Cruces Multivariables":
    st.header("Cruces Multivariables (Gráficos en Paralelo)")
    st.write("Área destinada al análisis comparativo y gráficos apareados en simultáneo (ej. evolución electoral vs. inflación o desocupación).")
    st.info("Próximamente disponible para configurar cruces dinámicos entre múltiples variables.")

elif modulo == "5. Informes y Publicaciones":
    st.header("Informes y Publicaciones")
    st.write("Repositorio documental de notas técnicas, informes de coyuntura y papers de investigación.")
    st.info("Próximamente se listarán los documentos listos para lectura y descarga.")

elif modulo == "6. Staff / Quiénes Somos":
    st.header("Equipo de Investigación / Staff")
    st.write("Integrantes, investigadores colaboradores y autoridades del Centro de Estudios Manuel Baldomero Ugarte.")
    st.info("Próximamente se actualizará la nómina del equipo.")
