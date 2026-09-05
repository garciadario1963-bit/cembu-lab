import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA & ESTILOS VISUALES (CEMBU BRANDING)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carga de FontAwesome para contar con los íconos oficiales SVG de las 7 redes
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    /* Fondo General Institucional */
    .stApp {
        background-color: #F4F6F8;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Ajuste Barra Lateral */
    section[data-testid="stSidebar"] {
        background-color: #EAEFF4;
        border-right: 1px solid #D0D7DE;
    }
    
    /* Encabezados Principales */
    .cembu-super {
        color: #555555;
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

    /* Estilo Íconos Oficiales Redes */
    .social-icon {
        color: #FFFFFF !important;
        font-size: 1.25rem;
        margin-left: 16px;
        text-decoration: none;
        transition: color 0.2s ease, transform 0.2s ease;
        display: inline-block;
    }
    .social-icon:hover {
        transform: scale(1.2);
        color: #E3532B !important;
    }

    /* Tarjetas de Contenido (Mosaico) con Sombras y Bordes */
    .card-gancho {
        border: 1px solid #D8E0E8;
        border-radius: 8px;
        padding: 18px;
        background-color: #FFFFFF;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        margin-bottom: 16px;
    }
    .badge-tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 4px 10px;
        border-radius: 4px;
        color: #FFFFFF;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Ocultar elementos por defecto */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. FUNCIÓN DE CARGA DINÁMICA DE NOTICIAS (EXCEL O VALOR POR DEFECTO)
# -----------------------------------------------------------------------------
@st.cache_data(ttl=300)
def cargar_noticia_semanal():
    archivo_excel = "noticia_semanal.xlsx"
    archivo_csv = "noticia_semanal.csv"
    
    noticia_default = {
        "etiqueta": "Informe Destacado Semanal",
        "titulo": "📊 Monitor de Coyuntura Global & Tasas Centrales",
        "copete": "Análisis de la trayectoria de las tasas de interés de la Fed, BCE y BoJ. Evaluamos la liquidez internacional y sus efectos de transmisión en la economía regional.",
        "imagen_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80",
        "epirafe_img": "Actualización semanal de variables macroeconómicas e indicadores clave."
    }

    try:
        if os.path.exists(archivo_excel):
            df = pd.read_excel(archivo_excel)
            return df.iloc[0].to_dict()
        elif os.path.exists(archivo_csv):
            df = pd.read_csv(archivo_csv)
            return df.iloc[0].to_dict()
    except Exception:
        pass
    
    return noticia_default


# -----------------------------------------------------------------------------
# 3. NAVEGACIÓN LATERAL CON LOGO INSTITUCIONAL
# -----------------------------------------------------------------------------
with st.sidebar:
    logo_path = "logo_cembu.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown("## 🏛️ **CEMBU**")
    
    st.markdown("**Portal CEMBU**")
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
# 4. PORTADA DINÁMICA TIPO PORTAL (ESTILO CLACSO / NOTICIAS)
# -----------------------------------------------------------------------------
if "📰 Portada & Difusión" in opcion_menu:
    
    noticia = cargar_noticia_semanal()

    # --- DIRECCIONES REALES DE REDES SOCIALES ---
    url_whatsapp = "https://wa.me/"
    url_x        = "https://x.com/cembu"
    url_linkedin = "https://linkedin.com/company/cembu"
    url_youtube  = "https://youtube.com/@cembu"
    url_instagram= "https://instagram.com/cembu"
    url_facebook = "https://facebook.com/cembu"
    url_telegram = "https://t.me/cembu"

    # BARRA SUPERIOR CON LOS 7 ÍCONOS OFICIALES
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #111827; color: #FFFFFF; padding: 10px 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
            <div style="font-weight: 600; font-size: 0.9rem;">🏛️ <strong>CEMBU</strong> — Centro de Estudios Manuel Baldomero Ugarte</div>
            <div style="display: flex; align-items: center;">
                <a href="{url_whatsapp}" target="_blank" class="social-icon" title="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
                <a href="{url_x}" target="_blank" class="social-icon" title="X (Twitter)"><i class="fa-brands fa-x-twitter"></i></a>
                <a href="{url_linkedin}" target="_blank" class="social-icon" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                <a href="{url_youtube}" target="_blank" class="social-icon" title="YouTube"><i class="fa-brands fa-youtube"></i></a>
                <a href="{url_instagram}" target="_blank" class="social-icon" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
                <a href="{url_facebook}" target="_blank" class="social-icon" title="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
                <a href="{url_telegram}" target="_blank" class="social-icon" title="Telegram"><i class="fa-brands fa-telegram"></i></a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CABECERA PRINCIPAL CON LOGO Y MARCA
    col_logo, col_titulo = st.columns([1, 4])
    with col_logo:
        if os.path.exists("logo_cembu.png"):
            st.image("logo_cembu.png", use_container_width=True)
    with col_titulo:
        st.markdown("<div class='cembu-super'>CENTRO DE ESTUDIOS MANUEL BALDOMERO UGARTE</div>", unsafe_allow_html=True)
        st.markdown("<div class='cembu-title'>Observatorio de Coyuntura, Modelización & Territorio</div>", unsafe_allow_html=True)
        st.markdown("<div class='cembu-sub'>Generación de conocimiento y herramientas predictivas para el desarrollo soberano</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📰 **Destacados & Publicaciones Gancho de la Semana**")
    st.caption("Contenido sincronizado con nuestras campañas de difusión en redes sociales.")

    col_principal, col_secundaria = st.columns([2.2, 1.2], gap="large")

    with col_principal:
        # GANCHO PRINCIPAL SEMANAL
        st.markdown(f'<span class="badge-tag" style="background-color: #E3532B;">{noticia.get("etiqueta", "Destacado")}</span>', unsafe_allow_html=True)
        
        st.image(
            noticia.get("imagen_url"), 
            caption=noticia.get("epirafe_img", ""),
            use_container_width=True
        )
        
        st.markdown(f"<h2 style='color: #111111; margin-top: 10px; font-weight: 700;'>{noticia.get('titulo')}</h2>", unsafe_allow_html=True)
        st.write(noticia.get("copete"))
        
        c1, c2 = st.columns([1, 1])
        with c1:
            st.button("📖 Leer Publicación Completa", key="btn_pub_main", use_container_width=True)
        with c2:
            st.button("📥 Descargar Base de Datos", key="btn_data_main", use_container_width=True)

    with col_secundaria:
        # TARJETAS SECUNDARIAS
        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #E3532B;">
                <span class="badge-tag" style="background-color: #E3532B;">CEMBU LAB</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Modelización Predictiva & Indicadores</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Estimación de tendencia de la actividad económica mediante modelos de alta frecuencia.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Panel de Coyuntura →", key="btn_lab_side", use_container_width=True)

        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #338B85;">
                <span class="badge-tag" style="background-color: #338B85;">CEMBU MATRIA</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Unidades de Producción Soberana (UPS)</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Relevamiento territorial de encadenamientos productivos y ZEE.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Mapa Productivo →", key="btn_matria_side", use_container_width=True)

        st.markdown("""
            <div class="card-gancho" style="border-left: 5px solid #77569B;">
                <span class="badge-tag" style="background-color: #77569B;">MICRODATOS</span>
                <h4 style="margin: 4px 0 8px 0; color: #111;">Consultor Interactivo EPH</h4>
                <p style="font-size: 0.88rem; color: #555; margin-bottom: 10px;">Acceso a microdatos normalizados de empleo e ingresos.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Consultar Microdatos →", key="btn_data_side", use_container_width=True)


# -----------------------------------------------------------------------------
# 5. RESTO DE SECCIONES DEL PROYECTO
# -----------------------------------------------------------------------------
elif "📊 CEMBU LAB" in opcion_menu:
    st.markdown("<div class='cembu-super'>LABORATORIO DE COYUNTURA</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU LAB</div>", unsafe_allow_html=True)
    st.write("Seguimiento de datos de alta frecuencia y modelización de variables económicas.")

elif "🌐 CEMBU MATRIA" in opcion_menu:
    st.markdown("<div class='cembu-super'>TERRITORIO & PLANIFICACIÓN</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU MATRIA</div>", unsafe_allow_html=True)
    st.write("Observatorio de Unidades de Producción Soberana (UPS) y geopolítica productiva.")

elif "📈 CEMBU OHD" in opcion_menu:
    st.markdown("<div class='cembu-super'>SISTEMA FINANCIERO INTERNACIONAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU OHD</div>", unsafe_allow_html=True)
    st.write("Monitoreo de Bancos Centrales (Fed, BCE, BoJ) y hegemonía del dólar.")

elif "📂 Base de Microdatos" in opcion_menu:
    st.markdown("<div class='cembu-super'>REPOSITORIO ABIERTO</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>Microdatos Normalizados</div>", unsafe_allow_html=True)
    st.write("Bases procesadas de EPH, Censos e indicadores sociales.")

elif "🏛️ Institucional" in opcion_menu:
    st.markdown("<div class='cembu-super'>ACERCA DEL CENTRO DE ESTUDIOS</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>Centro Ugarte (CEMBU)</div>", unsafe_allow_html=True)
    st.write("Investigación aplicada a la planificación económica e integración regional.")
