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

# 4. Navegación lateral
st.sidebar.header("Menú de Navegación")
modulo = st.sidebar.radio(
    "Seleccioná el módulo:",
    ["Macro & Meso Económico / Territorial", "Cruce de Variables (Estructural vs. Percepción)", "Microdatos (Censo + EPH)"]
)

# MÓDULO 1: MACRO & MESO
if modulo == "Macro & Meso Económico / Territorial":
    st.subheader("🏛️ Módulo Macro, Meso y Territorial")

    if df_largo.empty:
        st.stop()

    col1, col2, col3 = st.columns(3)

    with col1:
        dimensiones_disponibles = sorted(list(df_largo["Dimensión"].unique()))
        dim_sel = st.selectbox("1. Dimensión de Análisis (Marco Teórico):", dimensiones_disponibles)

    df_dim = df_largo[df_largo["Dimensión"] == dim_sel]

    with col2:
        niveles_disponibles = sorted(list(df_dim["Nivel_Analisis"].dropna().unique()))
        nivel_sel = st.selectbox("2. Nivel de Análisis (Escala):", niveles_disponibles)

    df_nivel = df_dim[df_dim["Nivel_Analisis"] == nivel_sel]

    with col3:
        fuentes_disponibles = sorted(list(df_nivel["Fuente"].dropna().unique()))
        if fuentes_disponibles:
            fuente_sel = st.selectbox("3. Fuente de Datos:", fuentes_disponibles)
            df_fuente = df_nivel[df_nivel["Fuente"] == fuente_sel]
        else:
            fuente_sel = None
            df_fuente = pd.DataFrame()

    st.markdown("---")

    if df_fuente.empty:
        st.info("ℹ️ No existen registros disponibles para la combinación de Dimensión, Escala y Fuente seleccionadas.")
    else:
        variables_disponibles = sorted(list(df_fuente["Variable"].dropna().unique()))
        var_sel = st.selectbox("4. Seleccioná el Indicador / Variable a analizar:", variables_disponibles)

        df_var = df_fuente[df_fuente["Variable"] == var_sel].copy()

        # Limpieza numérica
        df_var["Valor_Num"] = limpiar_valor_numerico(df_var["Valor"])

        # Filtrar filas sin valor numérico válido
        df_var = df_var.dropna(subset=["Valor_Num"])

        # Control de escala
        val_max = df_var["Valor_Num"].max() if not df_var.empty else 0
        val_min = df_var["Valor_Num"].min() if not df_var.empty else 0

        es_proporcion_pura = (pd.notna(val_max) and pd.notna(val_min) and val_min >= -1.0 and val_max <= 1.0)

        if es_proporcion_pura:
            df_var["Valor_Grafico"] = (df_var["Valor_Num"] * 100).round(2)
        else:
            df_var["Valor_Grafico"] = df_var["Valor_Num"].round(2)

        # Filtros territoriales a nivel municipal
        if nivel_sel == "Meso_Municipal":
            st.markdown("##### 📍 Filtros Territoriales (GBA / AMBA)")
            col_f1, col_f2 = st.columns(2)
            
            with col_f1:
                cordones = ["Todos"] + sorted([str(x) for x in df_var["Cordón"].dropna().unique()])
                cordon_sel = st.selectbox("Filtrar por Cordón:", cordones)
            
            with col_f2:
                sectores = ["Todos"] + sorted([str(x) for x in df_var["Sector_Geografico"].dropna().unique()])
                sector_sel = st.selectbox("Filtrar por Sector:", sectores)

            if cordon_sel != "Todos":
                df_var = df_var[df_var["Cordón"] == cordon_sel]
            if sector_sel != "Todos":
                df_var = df_var[df_var["Sector_Geografico"] == sector_sel]

        # Visualización de datos
        st.markdown(f"### 📈 Resultados: {var_sel}")
        st.caption(f"Fuente: **{fuente_sel}** | Dimensión: **{dim_sel}** | Escala: **{nivel_sel}**")

        label_y = "Diferencial (%)" if "Dif" in var_sel else ("Valor (%)" if "%" in var_sel or es_proporcion_pura else "Valor")

        if df_var.empty:
            st.warning("⚠️ No se encontraron valores numéricos válidos para esta variable en la base actual.")
        elif "Municipio" in df_var.columns and df_var["Municipio"].notna().any():
            fig = px.bar(
                df_var,
                x="Municipio",
                y="Valor_Grafico",
                color="Cordón" if "Cordón" in df_var.columns else None,
                labels={"Valor_Grafico": label_y},
                title=f"{var_sel} por Municipio",
                color_discrete_sequence=[COLOR_TERRACOTA, COLOR_VERDE_AGUA, COLOR_AMARILLO, COLOR_VIOLETA]
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            fig = px.line(
                df_var,
                x="Periodo",
                y="Valor_Grafico",
                markers=True,
                labels={"Valor_Grafico": label_y},
                title=f"Evolución Temporal: {var_sel}",
                color_discrete_sequence=[COLOR_TERRACOTA]
            )
            st.plotly_chart(fig, use_container_width=True)

        with st.expander("🔍 Ver Tabla de Datos Detallada"):
            cols_mostrar = [c for c in ["Municipio", "Región", "Periodo", "Variable", "Valor_Grafico", "Cordón", "Fuente"] if c in df_var.columns]
            df_mostrar = df_var[cols_mostrar].rename(columns={"Valor_Grafico": "Valor Procesado"})
            st.dataframe(df_mostrar, use_container_width=True)

# MÓDULO 2: CRUCE DE VARIABLES
elif modulo == "Cruce de Variables (Estructural vs. Percepción)":
    st.subheader("🔀 Cruce de Variables Municipales")
    st.caption("Compará dos indicadores a nivel municipal para identificar patrones y relaciones territoriales.")

    df_mun = df_largo[df_largo["Nivel_Analisis"] == "Meso_Municipal"].copy()

    if df_mun.empty:
        st.warning("No hay datos municipales disponibles para cruzar.")
    else:
        vars_disponibles = sorted(list(df_mun["Variable"].unique()))

        c1, c2 = st.columns(2)
        with c1:
            var_x = st.selectbox("Eje X (Variable 1 - ej. Estructural):", vars_disponibles, index=0)
        with c2:
            var_y = st.selectbox("Eje Y (Variable 2 - ej. Percepción):", vars_disponibles, index=min(1, len(vars_disponibles)-1))

        df_x = df_mun[(df_mun["Variable"] == var_x) & (df_mun["Periodo"].notna()) & (df_mun["Periodo"].astype(str).str.strip() != "")].copy()
        df_y = df_mun[(df_mun["Variable"] == var_y) & (df_mun["Periodo"].notna()) & (df_mun["Periodo"].astype(str).str.strip() != "")].copy()

        df_x["Val_X"] = limpiar_valor_numerico(df_x["Valor"])
        df_y["Val_Y"] = limpiar_valor_numerico(df_y["Valor"])

        if df_x["Val_X"].min() >= -1.0 and df_x["Val_X"].max() <= 1.0:
            df_x["Val_X"] = (df_x["Val_X"] * 100).round(2)
        else:
            df_x["Val_X"] = df_x["Val_X"].round(2)

        if df_y["Val_Y"].min() >= -1.0 and df_y["Val_Y"].max() <= 1.0:
            df_y["Val_Y"] = (df_y["Val_Y"] * 100).round(2)
        else:
            df_y["Val_Y"] = df_y["Val_Y"].round(2)

        df_x_sub = df_x[["Municipio", "Val_X", "Cordón", "Sector_Geografico"]].rename(columns={"Val_X": var_x})
        df_y_sub = df_y[["Municipio", "Val_Y"]].rename(columns={"Val_Y": var_y})

        df_cruce = pd.merge(df_x_sub, df_y_sub, on="Municipio", how="inner").dropna(subset=[var_x, var_y])

        if df_cruce.empty:
            st.info("No se encontraron coincidencias municipales válidas entre las dos variables seleccionadas.")
        else:
            if df_cruce[var_x].nunique() == 1:
                st.warning(f"⚠️ La variable '{var_x}' tiene el valor único {df_cruce[var_x].iloc[0]} en todos los municipios. Es un dato regional/AMBA.")
            if df_cruce[var_y].nunique() == 1:
                st.warning(f"⚠️ La variable '{var_y}' tiene el valor único {df_cruce[var_y].iloc[0]} en todos los municipios. Es un dato regional/AMBA.")

            fig_scatter = px.scatter(
                df_cruce,
                x=var_x,
                y=var_y,
                text="Municipio",
                color="Cordón",
                title=f"Cruce: {var_x} vs. {var_y}",
                color_discrete_sequence=[COLOR_TERRACOTA, COLOR_VERDE_AGUA, COLOR_AMARILLO, COLOR_VIOLETA]
            )
            fig_scatter.update_traces(textposition='top center', marker=dict(size=12))
            st.plotly_chart(fig_scatter, use_container_width=True)

            with st.expander("🔍 Ver Tabla del Cruce"):
                st.dataframe(df_cruce, use_container_width=True)

# MÓDULO 3: MICRODATOS
else:
    st.subheader("👥 Módulo de Microdatos Integrados")
    st.info("Espacio reservado para las consultas de la Matriz Maestra Integrada (Censo + EPH).")
