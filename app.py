import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. INYECCIÓN CSS CORREGIDA (Evita renderizado de código crudo en pantalla)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F4F6F8 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: #EAEFF4 !important;
        border-right: 1px solid #D0D7DE;
    }
    .cembu-super {
        color: #555555;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .cembu-title {
        color: #111111;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    .cembu-sub {
        color: #E3532B;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 20px;
    }
    .social-link {
        color: #FFFFFF !important;
        margin-left: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
        transition: transform 0.2s ease, opacity 0.2s ease;
    }
    .social-link:hover {
        transform: scale(1.2);
        opacity: 0.85;
    }
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
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. FUNCIÓN DE CARGA DINÁMICA DE NOTICIAS
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
# 4. NAVEGACIÓN LATERAL CON LOGO
# -----------------------------------------------------------------------------
with st.sidebar:
    # Busca el archivo de imagen del logo (soporta varios nombres comunes)
    posibles_logos = ["logo_cembu.png", "logo.png", "logo_cembu.jpg", "logo.jpg"]
    logo_encontrado = None
    for nombre_logo in posibles_logos:
        if os.path.exists(nombre_logo):
            logo_encontrado = nombre_logo
            break

    if logo_encontrado:
        st.image(logo_encontrado, use_container_width=True)
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
# 5. PORTADA PRINCIPAL
# -----------------------------------------------------------------------------
if "📰 Portada & Difusión" in opcion_menu:
    
    noticia = cargar_noticia_semanal()

    # URLs de Redes Sociales
    url_whatsapp = "https://wa.me/"
    url_x        = "https://x.com/"
    url_linkedin = "https://linkedin.com/"
    url_youtube  = "https://youtube.com/"
    url_instagram= "https://instagram.com/"
    url_facebook = "https://facebook.com/"
    url_telegram = "https://t.me/"

    # BARRA SUPERIOR DE REDES CON ÍCONOS SVG PUROS (Garantiza visualización perfecta)
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #111827; color: #FFFFFF; padding: 10px 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
            <div style="font-weight: 600; font-size: 0.9rem;">🏛️ <strong>CEMBU</strong> — Centro de Estudios Manuel Baldomero Ugarte</div>
            <div style="display: flex; align-items: center;">
                <a href="{url_whatsapp}" target="_blank" class="social-link" title="WhatsApp">
                    <svg width="20" height="20" fill="#25D366" viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984 0 1.758.459 3.474 1.33 4.982l-1.413 5.161 5.283-1.386a9.937 9.937 0 004.782 1.228h.005c5.507 0 9.991-4.479 9.991-9.986 0-2.668-1.038-5.176-2.925-7.063A9.927 9.927 0 0012.012 2z"/></svg>
                </a>
                <a href="{url_x}" target="_blank" class="social-link" title="X (Twitter)">
                    <svg width="18" height="18" fill="#FFFFFF" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="{url_linkedin}" target="_blank" class="social-link" title="LinkedIn">
                    <svg width="18" height="18" fill="#0A66C2" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/></svg>
                </a>
                <a href="{url_youtube}" target="_blank" class="social-link" title="YouTube">
                    <svg width="20" height="20" fill="#FF0000" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                </a>
                <a href="{url_instagram}" target="_blank" class="social-link" title="Instagram">
                    <svg width="18" height="18" fill="#E4405F" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                </a>
                <a href="{url_facebook}" target="_blank" class="social-link" title="Facebook">
                    <svg width="18" height="18" fill="#1877F2" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
                <a href="{url_telegram}" target="_blank" class="social-link" title="Telegram">
                    <svg width="18" height="18" fill="#26A5E4" viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm5.262 7.26a.603.603 0 0 1 .582.077c.182.146.257.387.195.612l-2.09 9.84a.602.602 0 0 1-.84.415l-3.37-1.39-1.63 1.57a.603.603 0 0 1-1.02-.43v-2.32l5.72-5.17c.13-.12.05-.34-.12-.31l-7.08 4.47-2.65-.83a.603.603 0 0 1-.02-1.14l11.66-4.5a.603.603 0 0 1 .71.105z"/></svg>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CABECERA CON LOGO (SI EXISTE EL ARCHIVO DE IMAGEN)
    col_logo, col_titulo = st.columns([1, 4])
    with col_logo:
        if logo_encontrado:
            st.image(logo_encontrado, use_container_width=True)
    with col_titulo:
        st.markdown("<div class='cembu-super'>CENTRO DE ESTUDIOS MANUEL BALDOMERO UGARTE</div>", unsafe_allow_html=True)
        st.markdown("<div class='cembu-title'>Observatorio de Coyuntura, Modelización & Territorio</div>", unsafe_allow_html=True)
        st.markdown("<div class='cembu-sub'>Generación de conocimiento y herramientas predictivas para el desarrollo soberano</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📰 **Destacados & Publicaciones Gancho de la Semana**")
    st.caption("Contenido sincronizado con nuestras campañas de difusión en redes sociales.")

    col_principal, col_secundaria = st.columns([2.2, 1.2], gap="large")

    with col_principal:
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
# 6. RESTO DE SECCIONES
# -----------------------------------------------------------------------------
elif "📊 CEMBU LAB" in opcion_menu:
    st.markdown("<div class='cembu-super'>LABORATORIO DE COYUNTURA</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU LAB</div>", unsafe_allow_html=True)

elif "🌐 CEMBU MATRIA" in opcion_menu:
    st.markdown("<div class='cembu-super'>TERRITORIO & PLANIFICACIÓN</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU MATRIA</div>", unsafe_allow_html=True)

elif "📈 CEMBU OHD" in opcion_menu:
    st.markdown("<div class='cembu-super'>SISTEMA FINANCIERO INTERNACIONAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>CEMBU OHD</div>", unsafe_allow_html=True)

elif "📂 Base de Microdatos" in opcion_menu:
    st.markdown("<div class='cembu-super'>REPOSITORIO ABIERTO</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>Microdatos Normalizados</div>", unsafe_allow_html=True)

elif "🏛️ Institucional" in opcion_menu:
    st.markdown("<div class='cembu-super'>ACERCA DEL CENTRO DE ESTUDIOS</div>", unsafe_allow_html=True)
    st.markdown("<div class='cembu-title'>Centro Ugarte (CEMBU)</div>", unsafe_allow_html=True)
