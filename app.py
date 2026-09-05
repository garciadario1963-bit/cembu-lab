import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA & ESTILOS (CEMBU BRANDING)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .cembu-super {
        color: #666666;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: -5px;
    }
    .cembu-title {
        color: #111111;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 5px;
    }
    .cembu-sub {
        color: #E3532B;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 25px;
    }
    .card-gancho {
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        background-color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 16px;
    }
    .badge-tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 3px 8px;
        border-radius: 4px;
        color: #FFFFFF;
        display: inline-block;
        margin-bottom: 8px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. FUNCIÓN DE CARGA DINÁMICA DE LA NOTICIA SEMANAL
# -----------------------------------------------------------------------------
@st.cache_data(ttl=300)  # Revisa cambios en el archivo cada 5 minutos
def cargar_noticia_semanal():
    """
    Lee el contenido del destacado desde 'noticia_semanal.xlsx' o 'noticia_semanal.csv'.
    Si el archivo no existe, devuelve datos por defecto.
    """
    archivo_excel = "noticia_semanal.xlsx"
    archivo_csv = "noticia_semanal.csv"
    
    # Noticia por defecto en caso de no encontrar archivo
    noticia_default = {
        "etiqueta": "Informe Destacado Semanal",
        "titulo": "📊 Monitor de Coyuntura Global & Tasas Centrales",
        "copete": "Análisis de la trayectoria de las tasas de interés de la Fed, BCE y BoJ. Evaluamos la liquidez internacional y sus efectos de transmisión en la economía regional.",
        "imagen_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80",
        "epirafe_img": "Actualización semanal de variables macroeconómicas e indicadores clave.",
        "link_informe": "#",
        "link_excel": "#"
    }

    try:
        if os.path.exists(archivo_excel):
            df = pd.read_excel(archivo_excel)
            return df.iloc[0].to_dict()
        elif os.path.exists(archivo_csv):
            df = pd.read_csv(archivo_csv)
            return df.iloc[0].to_dict()
    except Exception as e:
        st.warning(f"No se pudo leer la planilla de noticias: {e}. Usando datos por defecto.")
    
    return noticia_default


# -----------------------------------------------------------------------------
# 3. BARRA NAVEGACIÓN LATERAL
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/logo.png", width=140)
    st.markdown("### **Portal CEMBU**")
    st.caption("Investigación, Coyuntura y Datos")
    
    opcion_menu = st.radio(
        "Navegación:",
        [
            "📰 Portada & Difusión",
            "📊 CEMBU LAB (Coyuntura)",
            "🌐 CEMBU MATRIA (Territorio)",
            "📈 CEMBU OHD (Monetario & Int.)",
            "📂 Base de Microdatos (EPH/Censo)",
            "🏛️ Institucional & Equipo"
        ]
    )
    st.divider()
    st.caption("📍 Buenos Aires, Argentina")


# -----------------------------------------------------------------------------
# 4. PORTADA DINÁMICA (TIPO PORTAL CLACSO)
# -----------------------------------------------------------------------------
if "📰 Portada & Difusión" in opcion_menu:
    
    # Cargar noticia desde Excel/CSV
    noticia = cargar_noticia_semanal()

    # Barra superior de redes
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #1A1A1A; color: #FFFFFF; padding: 8px 18px; border-radius: 6px; font-size: 0.85rem; margin-bottom: 20px;">
            <div>🏛️ <strong>CEMBU</strong> — Centro de Estudios Manuel Baldomero Ugarte</div>
            <div>
                <a href="https://wa.me/" target="_blank" style="color: #25D366; margin-left: 12px; text-decoration: none; font-weight: bold;">💬 WhatsApp</a>
                <a href="https://linkedin.com" target="_blank" style="color: #0A66C2; margin-left: 12px; text-decoration: none; font-weight: bold;">🌐 LinkedIn</a>
                <a href="https://x.com" target="_blank" style="color: #FFFFFF; margin-left: 12px; text-decoration: none; font-weight: bold;">📱 X / Twitter</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<div class='cembu-super'>CENTRO DE ESTUDIOS MANUEL BALDOMERO UGARTE</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>Observatorio de Coyuntura, Modelización & Territorio</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-sub'>Generación de conocimiento y herramientas predictivas para el desarrollo soberano</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📰 **Destacados & Publicaciones Gancho de la Semana**")
    st.caption("Contenido sincronizado con nuestras campañas de difusión en redes sociales.")

    col_principal, col_secundaria = st.columns([2.2, 1.2], gap="large")

    with col_principal:
        # --- DESTACADO DINÁMICO (Cargado desde Excel/CSV) ---
        st.markdown(f'<span class="badge-tag" style="background-color: #E3532B;">{noticia.get("etiqueta", "Destacado")}</span>', unsafe_allow_html=True)
        
        st.image(
            noticia.get("imagen_url"), 
            caption=noticia.get("epirafe_img", ""),
            use_column_width=True
        )
        
        st.markdown(f"<h2 style='color: #111111; margin-top: 10px; font-weight: 700;'>{noticia.get('titulo')}</h2>", unsafe_allow_html=True)
        st.write(noticia.get("copete"))
        
        c1, c2 = st.columns([1, 1])
        with c1:
            st.button("📖 Leer Publicación Completa", key="btn_pub_main", use_container_width=True)
        with c2:
            st.button("📥 Descargar Base de Datos", key="btn_data_main", use_container_width=True)

    with col_secundaria:
        # Tarjetas secundarias permanentes
        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #E3532B;">
                <span class="badge-tag" style="background-color: #E3532B;">CEMBU LAB</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Modelización Predictiva & Indicadores</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Estimación de tendencia de la actividad económica mediante modelos de alta frecuencia.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Panel de Coyuntura →", key="btn_lab_side")

        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #338B85;">
                <span class="badge-tag" style="background-color: #338B85;">CEMBU MATRIA</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Unidades de Producción Soberana (UPS)</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Relevamiento territorial de encadenamientos productivos y ZEE.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Mapa Productivo →", key="btn_matria_side")

        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #77569B;">
                <span class="badge-tag" style="background-color: #77569B;">MICRODATOS</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Consultor Interactivo EPH</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Acceso a microdatos normalizados de empleo e ingresos.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Consultar Microdatos →", key="btn_data_side")


# -----------------------------------------------------------------------------
# 5. RESTO DE SECCIONES
# -----------------------------------------------------------------------------
elif "📊 CEMBU LAB" in opcion_menu:
    st.markdown("<div class='cembu-title'>CEMBU LAB</div>", unsafe_allow_html=True)
    st.write("Seguimiento de datos de alta frecuencia y modelización de variables económicas.")

elif "🌐 CEMBU MATRIA" in opcion_menu:
    st.markdown("<div class='cembu-title'>CEMBU MATRIA</div>", unsafe_allow_html=True)
    st.write("Observatorio de Unidades de Producción Soberana (UPS) y geopolítica productiva.")

elif "📈 CEMBU OHD" in opcion_menu:
    st.markdown("<div class='cembu-title'>CEMBU OHD</div>", unsafe_allow_html=True)
    st.write("Monitoreo de Bancos Centrales (Fed, BCE, BoJ) y estructura del sistema financiero internacional.")

elif "📂 Base de Microdatos" in opcion_menu:
    st.markdown("<div class='cembu-title'>Microdatos Normalizados</div>", unsafe_allow_html=True)

elif "🏛️ Institucional" in opcion_menu:
    st.markdown("<div class='cembu-title'>Centro Ugarte (CEMBU)</div>", unsafe_allow_html=True)
