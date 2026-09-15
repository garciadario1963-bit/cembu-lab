import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from streamlit_folium import st_folium

# ============================================================
# 1. CONFIGURACIÓN DE PÁGINA
# ============================================================
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="assets/1_CEMBU.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. ESTILOS CSS
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    html, body, .stApp {
        background-color: #F8FAFC !important;
        font-family: 'Inter', sans-serif;
    }

    .block-container { padding: 0 !important; max-width: 100% !important; }
    .stApp > header { display: none !important; }
    section.main > div:first-child { padding-top: 0 !important; }
    #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }

    .top-black-banner {
        background-color: #0B0F19;
        color: #FFFFFF;
        padding: 22px 40px 18px 40px;
        text-align: center;
        border-bottom: 3px solid #EA580C;
        position: relative;
        width: 100vw;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        box-sizing: border-box;
    }

    .logo-container {
        position: absolute;
        top: 18px;
        left: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 72px;
        height: 72px;
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 6px;
        box-sizing: border-box;
    }

    .logo-container img { width: 100%; height: 100%; object-fit: contain; }

    .social-icons-container {
        position: absolute;
        top: 26px;
        right: 40px;
        display: flex;
        gap: 14px;
        align-items: center;
    }

    .social-link {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        color: #94A3B8;
        text-decoration: none;
        transition: color 0.2s ease, transform 0.2s ease;
    }

    .social-link:hover { color: #EA580C; transform: translateY(-2px); }
    .social-icon-svg { width: 18px; height: 18px; fill: currentColor; }

    .cembu-logo-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.4rem;
        font-weight: 900;
        color: #EA580C;
        letter-spacing: 2px;
        margin: 0 0 4px 0;
        line-height: 1;
    }

    .cembu-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        color: #CBD5E1;
        font-weight: 500;
        letter-spacing: 0.3px;
        margin-bottom: 0;
    }

    .menu-bar-container {
        background-color: #FFFFFF;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        padding: 12px 20px 14px 20px;
        border-bottom: 3px solid #EA580C;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        box-sizing: border-box;
    }

    .menu-bar-container div[data-testid="stButton"] { display: inline-block; margin: 0 2px; }

    .menu-bar-container div[data-testid="stButton"] > button {
        background-color: transparent !important;
        color: #334155 !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        font-size: 0.78rem !important;
        font-weight: 700 !important;
        padding: 8px 12px !important;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        transition: all 0.2s ease;
        white-space: nowrap;
        box-shadow: none !important;
    }

    .menu-bar-container div[data-testid="stButton"] > button:hover {
        color: #EA580C !important;
        background-color: rgba(234, 88, 12, 0.08) !important;
        border-bottom: 2px solid #EA580C !important;
    }

    .menu-bar-container div[data-testid="stButton"] > button[kind="primary"] {
        color: #EA580C !important;
        background-color: rgba(234, 88, 12, 0.10) !important;
        border-bottom: 2px solid #EA580C !important;
    }

    .content-container { padding: 24px 40px 0 40px; }

    .triangle-card {
        background: #FFFFFF;
        border-radius: 6px;
        padding: 14px 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        height: 100%;
    }
    .card-a { border-left: 4px solid #EA580C; }
    .card-b { border-left: 4px solid #0284C7; }
    .card-c { border-left: 4px solid #4F46E5; }

    .tri-title-a { font-family: 'Playfair Display', serif; color: #EA580C; font-weight: 700; font-size: 0.98rem; }
    .tri-title-b { font-family: 'Playfair Display', serif; color: #0284C7; font-weight: 700; font-size: 0.98rem; }
    .tri-title-c { font-family: 'Playfair Display', serif; color: #4F46E5; font-weight: 700; font-size: 0.98rem; }
    .tri-desc { font-size: 0.75rem; color: #64748B; margin-top: 4px; line-height: 1.3; }

    .white-block {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 24px 28px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 16px;
    }
    .block-title {
        font-family: 'Playfair Display', serif;
        font-weight: 800;
        font-size: 1.1rem;
        color: #0F172A;
    }
    .block-sub { font-size: 0.78rem; color: #64748B; margin-bottom: 12px; }

    .section-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 14px;
    }
    .section-logo {
        width: 70px;
        height: 70px;
        object-fit: contain;
        background: #F8FAFC;
        border-radius: 8px;
        padding: 6px;
    }
    .section-title-big {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: #0F172A;
        margin: 0;
        line-height: 1.1;
    }
    .section-subtitle {
        font-size: 0.9rem;
        color: #64748B;
        margin: 4px 0 0 0;
        font-weight: 500;
    }

    .abstract-text {
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.7;
        margin-bottom: 14px;
    }
    .abstract-text strong { color: #0F172A; }

    .struct-block {
        background: #F8FAFC;
        border-left: 3px solid #EA580C;
        border-radius: 4px;
        padding: 12px 16px;
        margin-bottom: 10px;
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.6;
    }
    .struct-block strong { color: #EA580C; }

    .placeholder-box {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
        border: 2px dashed #CBD5E1;
        border-radius: 8px;
        padding: 40px 20px;
        text-align: center;
        color: #64748B;
        font-size: 0.85rem;
        margin-top: 12px;
    }
    .placeholder-box .ph-icon {
        font-size: 2rem;
        margin-bottom: 8px;
        display: block;
    }

    .badge {
        font-size: 0.65rem;
        font-weight: 700;
        color: #FFF;
        padding: 3px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 6px;
    }
    .badge-red { background-color: #DC2626; }
    .badge-teal { background-color: #0D9488; }
    .badge-purple { background-color: #7C3AED; }
    .badge-blue { background-color: #0284C7; }

    .unit-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
    }
    .unit-logo {
        max-width: 80px;
        max-height: 80px;
        width: auto;
        height: auto;
        object-fit: contain;
        margin: 0 auto 10px auto;
        display: block;
    }
    .unit-title {
        font-family: 'Playfair Display', serif;
        font-weight: 800;
        font-size: 1rem;
        color: #0F172A;
        margin: 4px 0 8px 0;
    }
    .unit-desc { font-size: 0.78rem; color: #64748B; line-height: 1.4; }

    .cembu-footer {
        background-color: #0B0F19;
        color: #c9d1d9;
        padding: 2rem 40px 1.2rem 40px;
        margin-top: 3rem;
        border-top: 3px solid #EA580C;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        box-sizing: border-box;
    }
    .footer-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
        gap: 2rem;
    }
    .footer-col { flex: 1; min-width: 240px; }
    .footer-title {
        color: #EA580C;
        font-weight: bold;
        font-size: 1.05rem;
        margin-bottom: 0.8rem;
        font-family: 'Playfair Display', serif;
    }
    .footer-item {
        margin-bottom: 0.6rem;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .footer-copy-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #58a6ff;
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        font-family: monospace;
        user-select: all;
    }
    .footer-bottom {
        text-align: center;
        border-top: 1px solid #21262d;
        margin-top: 1.8rem;
        padding-top: 0.8rem;
        font-size: 0.85rem;
        color: #8b949e;
    }
    .footer-link { color: #25d366; text-decoration: none; font-weight: bold; }
    .footer-link:hover { text-decoration: underline; }

    .btn-contacto {
        display: inline-block;
        padding: 10px 22px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        margin-right: 10px;
        margin-top: 6px;
        color: #FFF !important;
    }
    .btn-whatsapp { background-color: #25D366; }
    .btn-email { background-color: #EA580C; }

    /* Estilo de sub-tabs internas */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        background-color: #F1F5F9;
        padding: 6px 12px;
        border-radius: 8px;
        display: inline-flex;
        gap: 4px;
    }
    div[data-testid="stRadio"] label > div:first-child { display: none !important; }
    div[data-testid="stRadio"] label {
        background-color: transparent !important;
        color: #475569 !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        padding: 8px 16px !important;
        border-radius: 6px !important;
        cursor: pointer;
        border: none !important;
    }
    div[data-testid="stRadio"] label:has(input:checked) {
        background-color: #FFFFFF !important;
        color: #EA580C !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    div[data-testid="stRadio"] label p { color: inherit !important; font-size: inherit !important; }

    /* ============================================ */
    /* CONTENEDOR DE LA LÍNEA DE TIEMPO AL 85%     */
    /* ============================================ */
    .timeline-wrapper {
        max-width: 85% !important;
        margin: 0 auto 20px auto !important;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        background: #F1EEE6;
    }

    /* Contenedor del iframe de Streamlit para limitar ancho */
    .timeline-wrapper + div iframe,
    div[data-testid="stCustomComponentV1"] iframe {
        max-width: 100%;
    }

    /* ============================================ */
    /* CUADRO DE DESCARGA AL 70% CENTRADO           */
    /* ============================================ */
    .download-box {
        max-width: 70% !important;
        margin: 20px auto 20px auto !important;
        padding: 22px 26px;
        background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%);
        border: 2px solid #EA580C;
        border-radius: 10px;
        text-align: center;
    }
    .download-box .dl-title {
        font-family: 'Playfair Display', serif;
        font-weight: 800;
        font-size: 1.1rem;
        color: #0F172A;
        margin-bottom: 8px;
    }
    .download-box .dl-sub {
        font-size: 0.85rem;
        color: #64748B;
        margin-bottom: 16px;
        line-height: 1.5;
    }
    .btn-download {
        display: inline-block;
        background-color: #EA580C;
        color: #FFFFFF !important;
        padding: 12px 30px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.95rem;
        transition: all 0.2s ease;
    }
    .btn-download:hover {
        background-color: #C2410C;
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. HEADER NEGRO
# ============================================================
st.markdown("""
<div class="top-black-banner">
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/1_CEMBU.png" alt="Logo CEMBU">
    </div>
    <div class="social-icons-container">
        <a href="https://www.instagram.com/cembuorg" target="_blank" class="social-link" title="Instagram">
            <svg class="social-icon-svg" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <a href="https://x.com/cembuce" target="_blank" class="social-link" title="X (Twitter)">
            <svg class="social-icon-svg" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
        <a href="https://www.linkedin.com/company/144976145/" target="_blank" class="social-link" title="LinkedIn">
            <svg class="social-icon-svg" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        </a>
        <a href="https://www.facebook.com/profile.php?id=61594481903042" target="_blank" class="social-link" title="Facebook">
            <svg class="social-icon-svg" viewBox="0 0 24 24"><path d="M9 8H6v4h3v12h5V12h3.642L18 8h-4V6.333C14 5.374 14.5 5 15.5 5H18V0h-3.808C10.592 0 9 1.583 9 4.615V8z"/></svg>
        </a>
        <a href="https://www.youtube.com/@cembuorg" target="_blank" class="social-link" title="YouTube">
            <svg class="social-icon-svg" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
    </div>
    <div class="cembu-logo-title">CEMBU</div>
    <div class="cembu-subtitle">Conocimiento territorial para el desarrollo soberano</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 4. MENÚ CON BOTONES
# ============================================================
if "seccion" not in st.session_state:
    st.session_state.seccion = "MENÚ"

opciones = ["MENÚ", "MATRIA", "OHD", "PROYS", "SERV_CONS", "PUBS_DIF", "CEMBU LAB", "CONTACTO"]

st.markdown('<div class="menu-bar-container">', unsafe_allow_html=True)
cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
for i, opcion in enumerate(opciones):
    with cols[i + 1]:
        tipo = "primary" if st.session_state.seccion == opcion else "secondary"
        if st.button(opcion, key=f"btn_{opcion}", type=tipo, use_container_width=True):
            st.session_state.seccion = opcion
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

pestana = st.session_state.seccion

# ============================================================
# URLs
# ============================================================
BASE_URL = "https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/"
LOGO_LAB = BASE_URL + "CEMBU_LAB_logo.png"
LOGO_MATRIA = BASE_URL + "2_MATRIA.png"
LOGO_OHD = BASE_URL + "3_OHD.png"
LOGO_PROYS = BASE_URL + "4_PROYS.png"
LOGO_SERV = BASE_URL + "5_SERV_CONS.png"
LOGO_PUBS = BASE_URL + "6_PUBS_DIF.png"

# URL CORREGIDA — el archivo debe llamarse OHD_Fundamentos_Teoricos.pdf
PDF_URL = "https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/docs/OHD_Fundamentos_Teoricos.pdf"

# ============================================================
# FUNCIÓN: bloque de contacto
# ============================================================
def bloque_contacto():
    html = '<div class="white-block" style="background: #0B0F19; color: #E2E8F0; margin-top: 20px;">'
    html += '<div style="font-family: Playfair Display, serif; font-size: 1.1rem; color: #EA580C; font-weight: 800; margin-bottom: 10px;">📬 Contacto</div>'
    html += '<div style="font-size: 0.92rem; line-height: 2;">'
    html += '<b>Darío Fabián García</b> — Director Ejecutivo<br>'
    html += '📧 <a href="mailto:dariofgarcia@yahoo.com" style="color:#25D366; text-decoration:none; font-weight:bold;">dariofgarcia@yahoo.com</a><br>'
    html += '📱 <a href="https://wa.me/5491149938695" target="_blank" style="color:#25D366; text-decoration:none; font-weight:bold;">(011) 15-4993-8695</a>'
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)

# ============================================================
# 5. CONTENIDO POR PESTAÑA
# ============================================================

# -------------------- MENÚ (HOME) --------------------
if pestana == "MENÚ":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.markdown('<div class="triangle-card card-a"><div class="tri-title-a">1. Decisión & Ejecución</div><div class="tri-desc">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="triangle-card card-b"><div class="tri-title-b">2. Análisis & Modelización</div><div class="tri-desc">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="triangle-card card-c"><div class="tri-title-c">3. Transformación Real</div><div class="tri-desc">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1.1, 1], gap="small")

    with col_left:
        st.markdown('<div class="white-block" style="padding-bottom: 8px;"><span class="badge badge-red">NOVEDADES & ACTIVIDADES</span><div class="block-title">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</div><div class="block-sub" style="margin-bottom: 8px;">Nuestras últimas actividades académicas y avances en análisis regional.</div></div>', unsafe_allow_html=True)
        carrusel_html = """
        <!DOCTYPE html><html><head><style>
            body { margin: 0; font-family: Inter, sans-serif; background: transparent; }
            .carousel-container { position: relative; width: 100%; height: 220px; overflow: hidden; border-radius: 6px; }
            .slide { position: absolute; width: 100%; height: 100%; opacity: 0; transition: opacity 1s ease-in-out; }
            .slide.active { opacity: 1; }
            .slide img { width: 100%; height: 100%; object-fit: cover; }
            .caption { position: absolute; bottom: 0; background: rgba(15, 23, 42, 0.85); color: #fff; width: 100%; padding: 8px 12px; font-size: 12px; box-sizing: border-box; }
            .dots-container { position: absolute; top: 10px; right: 12px; display: flex; gap: 6px; z-index: 10; }
            .dot { width: 10px; height: 10px; background-color: rgba(255,255,255,0.5); border-radius: 50%; display: inline-block; cursor: pointer; }
            .dot.active-dot { background-color: #EA580C; }
        </style></head><body>
        <div class="carousel-container">
            <div class="dots-container"><span class="dot active-dot" onclick="setSlide(0)"></span><span class="dot" onclick="setSlide(1)"></span></div>
            <div class="slide active"><img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=700&auto=format&fit=crop&q=60" alt="CLACSO"><div class="caption"><b>1 / 2 — CLACSO EN LA FILUNI:</b> Participación institucional en México.</div></div>
            <div class="slide"><img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?w=700&auto=format&fit=crop&q=60" alt="Monitor Territorial"><div class="caption"><b>2 / 2 — MONITOR TERRITORIAL:</b> Mapeo dinámico e infraestructura regional.</div></div>
        </div>
        <script>
            let currentSlide = 0; const slides = document.querySelectorAll('.slide'); const dots = document.querySelectorAll('.dot');
            function showSlide(index) { slides.forEach((s,i)=>{s.classList.remove('active');dots[i].classList.remove('active-dot');}); slides[index].classList.add('active'); dots[index].classList.add('active-dot'); }
            function nextSlide() { currentSlide = (currentSlide + 1) % slides.length; showSlide(currentSlide); }
            function setSlide(index) { currentSlide = index; showSlide(currentSlide); }
            setInterval(nextSlide, 3500);
        </script></body></html>
        """
        components.html(carrusel_html, height=230)

    with col_right:
        st.markdown('<div class="white-block"><div class="block-title">📍 Tablero de Control Territorial & Modelización</div><div class="block-sub">📌 Monitor Territorial: Región Metropolitana / AMBA</div></div>', unsafe_allow_html=True)
        m = folium.Map(location=[-34.6037, -58.3816], zoom_start=10, tiles="CartoDB positron")
        folium.Marker([-34.6037, -58.3816], popup="Sede Central CABA", tooltip="CEMBU AMBA", icon=folium.Icon(color="orange", icon="info-sign")).add_to(m)
        st_folium(m, width="100%", height=210, returned_objects=[])

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3, gap="small")
    with m1:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_LAB + '" alt="CEMBU LAB"><span class="badge badge-red">CEMBU LAB</span><div class="unit-title">Modelos & Algoritmos</div><div class="unit-desc">Plataforma de inteligencia territorial: base de datos y modelos predictivos.</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_MATRIA + '" alt="MATRIA"><span class="badge badge-teal">MATRIA</span><div class="unit-title">Matriz Productiva Popular</div><div class="unit-desc">La data al servicio de la matriz productiva popular.</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_OHD + '" alt="OHD"><span class="badge badge-purple">OHD MONETARIO</span><div class="unit-title">Hegemonía del Dólar</div><div class="unit-desc">Seguimiento crítico del sistema monetario global.</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    p1, p2 = st.columns(2, gap="small")
    with p1:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_PROYS + '" alt="PROYECTOS"><span class="badge badge-blue">PROYECTOS</span><div class="unit-title">Consultoría Territorial</div><div class="unit-desc">Líneas de base, monitoreo, evaluación y modelización predictiva.</div></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_SERV + '" alt="SERVICIOS"><span class="badge badge-red">SERVICIOS & CONSULTORÍA</span><div class="unit-title">Consultoría Electoral</div><div class="unit-desc">Segmentación electoral, historia del voto e identidades territoriales.</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1], gap="small")
    with c2:
        st.markdown('<div class="unit-card"><img class="unit-logo" src="' + LOGO_PUBS + '" alt="PUBLICACIONES"><span class="badge badge-teal">PUBLICACIONES & DIFUSIÓN</span><div class="unit-title">Producción Académica</div><div class="unit-desc">Papers, informes técnicos y materiales de divulgación.</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CEMBU LAB --------------------
elif pestana == "CEMBU LAB":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_LAB + '" alt="CEMBU LAB">'
    html += '<div><span class="badge badge-red">CEMBU LAB</span>'
    html += '<h1 class="section-title-big">Plataforma de Inteligencia Territorial</h1>'
    html += '<p class="section-subtitle">Base de datos y modelos predictivos para el desarrollo con soberanía</p></div></div>'
    html += '<p class="abstract-text"><strong>CEMBU Lab</strong> es la plataforma de inteligencia territorial del CEMBU, orientada a generar, procesar y modelizar datos para el diseño de políticas públicas de desarrollo territorial, con foco en la Provincia de Buenos Aires y CABA.</p>'
    html += '<div class="struct-block"><strong>Justificación:</strong> La mayoría de los centros de estudios y gobiernos locales no cuentan con una infraestructura de datos robusta ni capacidades de modelización predictiva, lo que genera políticas reactivas y discontinuidad del acumulado técnico.</div>'
    html += '<div class="struct-block"><strong>Estructura:</strong> Se organiza en tres capas: (1) Infraestructura de datos (33 fuentes, 5 niveles, 8 unidades de análisis, series 1960-2026). (2) Modelos predictivos (complejidad económica, ABM, simulación sectorial, predicción de demanda). (3) Dashboards y transferencia.</div>'
    html += '<div class="placeholder-box"><span class="ph-icon">📊</span><b>Próximamente: Dashboard Interactivo</b><br>Datos a nivel macro, meso y micro — Modelos predictivos — Series 1960-2026</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- MATRIA --------------------
elif pestana == "MATRIA":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_MATRIA + '" alt="MATRIA">'
    html += '<div><span class="badge badge-teal">MATRIA</span>'
    html += '<h1 class="section-title-big">La Data al Servicio de la Matriz Productiva Popular</h1>'
    html += '<p class="section-subtitle">Relevamiento territorial de encadenamientos productivos</p></div></div>'
    html += '<p class="abstract-text"><strong>MATRIA</strong> es el espacio del CEMBU dedicado al relevamiento y análisis de la matriz productiva popular, con foco en los encadenamientos productivos, las unidades de producción (UPS) y la construcción de una matriz insumo-producto desde el territorio.</p>'
    html += '<div class="struct-block"><strong>Ejes de trabajo:</strong> Relevamiento de Unidades de Producción (UPS), análisis de encadenamientos productivos, construcción de matriz insumo-producto territorial, identificación de cuellos de botella y oportunidades.</div>'
    html += '<div class="placeholder-box"><span class="ph-icon">🗺️</span><b>Próximamente: Mapa Productivo Interactivo</b><br>Relevamiento de UPS — Encadenamientos productivos — Matriz insumo-producto</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- OHD (con sub-tabs) --------------------
elif pestana == "OHD":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_OHD + '" alt="OHD">'
    html += '<div><span class="badge badge-purple">OHD</span>'
    html += '<h1 class="section-title-big">Observatorio de la Hegemonía del Dólar</h1>'
    html += '<p class="section-subtitle">Análisis teórico-histórico de la moneda, los regímenes de acumulación y la crisis sistémica</p></div></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

    subtab = st.radio(
        "Sub-sección OHD",
        ["🌍 Mundo Precapitalista", "💵 Hegemonía del Dólar (Siglo XX-XXI)"],
        horizontal=True,
        label_visibility="collapsed",
        key="ohd_subtab"
    )

    # ---------- SUB-SECCIÓN 1: MUNDO PRECAPITALISTA ----------
    if subtab == "🌍 Mundo Precapitalista":
        html = '<div class="white-block">'
        html += '<span class="badge badge-purple">ANTECEDENTES HISTÓRICOS</span>'
        html += '<h2 class="section-title-big" style="font-size:1.5rem;">Mundo Precapitalista: Auge y Declive de los Imperios</h2>'
        html += '<p class="section-subtitle">Marco teórico-metodológico e histórico · 550 a.C. – 2026 d.C.</p>'
        html += '<p class="abstract-text" style="margin-top:16px;">Esta sección reúne el marco teórico-metodológico e histórico del Observatorio. Analiza cómo las sociedades precapitalistas —desde el sistema-mundo esclavista hasta los grandes imperios tributarios de Eurasia, América y África— extrajeron, circularon y concentraron el excedente social a lo largo de más de 2.500 años.</p>'
        html += '<div class="struct-block"><strong>Eje 1 — La Ley de los Grandes Números:</strong> a mayor masa productiva (n), mayor capacidad del sistema para amortiguar perturbaciones. La moneda degradada es el correlato empírico de la ruptura de esta ley.</div>'
        html += '<div class="struct-block"><strong>Eje 2 — La dialéctica decisión-ejecución:</strong> contradicción inmanente entre la decisión centralizada (que busca la reproducción sistémica) y la ejecución fragmentada (que busca el interés particular).</div>'
        html += '<div class="struct-block"><strong>Eje 3 — La moneda como cristalización de las relaciones sociales:</strong> su historia es la historia de las formas de expropiación del trabajo y de la lucha de clases.</div>'
        html += '<p class="abstract-text">El resultado es un mapa orientativo de <strong>25 imperios y regímenes</strong> —desde Roma hasta los EE.UU. contemporáneos— que permite rastrear cómo el capitalismo, como universal concreto, ha operado su negación dialéctica sobre el sistema-mundo precapitalista.</p>'
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)

        # === LÍNEA DE TIEMPO (al 85% via contenedor CSS) ===
        # Streamlit no permite envolver un components.html en un div custom,
        # así que usamos st.columns para simular el ancho del 85%
        col_izq, col_centro, col_der = st.columns([0.075, 0.85, 0.075])
        with col_centro:
            st.markdown('<div style="background:#FFFFFF; border-radius:10px; padding:14px 14px 0 14px; box-shadow:0 2px 8px rgba(0,0,0,0.06);"><span class="badge badge-red">LÍNEA DE TIEMPO INTERACTIVA</span><h2 class="section-title-big" style="font-size:1.4rem;">Ciclos imperiales: auge y declive</h2><p class="section-subtitle">25 imperios y regímenes a lo largo de 2600 años. Pasá el cursor sobre cada tramo para ver el detalle.</p></div>', unsafe_allow_html=True)

            timeline_html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  :root{
    --ink:#F1EEE6;--panel:#E7E3D7;--panel-2:#22242B;--line:#D8D3C3;--line-soft:#E2DECF;
    --ivory:#2B2A24;--ivory-dim:#6E6957;--muted:#928C78;--brass:#A9791F;--brass-dim:#C8A85E;
    --serif: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif;
    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    --mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  }
  *{box-sizing:border-box;}
  body{margin:0;background:var(--ink);color:var(--ivory);font-family:var(--sans);}
  .tl-root{padding:16px 0 24px;}
  .tl-header{padding:0 18px 14px;border-bottom:1px solid var(--line);}
  .tl-controls{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin-bottom:12px;}
  .tl-search{background:var(--panel);border:1px solid var(--line);border-radius:3px;padding:5px 9px;color:var(--ivory);font-family:var(--sans);font-size:12px;width:180px;outline:none;}
  .tl-search::placeholder{color:var(--muted);}
  .tl-zoom{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:11px;color:var(--ivory-dim);}
  .tl-btn{background:var(--panel);border:1px solid var(--line);color:var(--ivory);width:22px;height:22px;border-radius:3px;cursor:pointer;font-family:var(--mono);font-size:12px;line-height:1;display:flex;align-items:center;justify-content:center;}
  .tl-btn:hover{border-color:var(--brass-dim);color:var(--brass);}
  .tl-btn.wide{width:auto;padding:0 8px;font-family:var(--sans);font-size:11px;}
  .tl-legend{display:flex;flex-wrap:wrap;gap:5px;}
  .tl-tag{display:flex;align-items:center;gap:5px;font-size:10px;color:var(--ivory-dim);background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:3px 8px 3px 6px;cursor:pointer;user-select:none;transition:opacity .15s;}
  .tl-tag:hover{border-color:var(--brass-dim);}
  .tl-tag.off{opacity:.35;}
  .tl-dot{width:7px;height:7px;border-radius:50%;flex:none;}
  .tl-scroll{overflow-x:auto;overflow-y:visible;padding:0 0 10px;}
  .tl-scroll::-webkit-scrollbar{height:8px;}
  .tl-scroll::-webkit-scrollbar-track{background:var(--ink);}
  .tl-scroll::-webkit-scrollbar-thumb{background:var(--line);border-radius:5px;}
  .tl-scroll::-webkit-scrollbar-thumb:hover{background:var(--brass-dim);}
  .tl-inner{position:relative;padding-left:20px;}
  .tl-axis-wrap{position:sticky;top:0;z-index:4;background:var(--ink);border-bottom:1px solid var(--line);}
  .tl-axis{position:relative;height:28px;margin-left:180px;}
  .tl-tick{position:absolute;top:0;bottom:0;border-left:1px solid var(--line-soft);}
  .tl-tick span{position:absolute;top:6px;left:3px;font-family:var(--mono);font-size:9px;color:var(--muted);white-space:nowrap;}
  .tl-tick.decade span{color:var(--ivory-dim);}
  .tl-rows{position:relative;margin-left:180px;}
  .tl-row{position:relative;height:32px;border-bottom:1px solid var(--line-soft);transition:opacity .15s;display:flex;align-items:stretch;}
  .tl-row.dim{opacity:.15;}
  .tl-row:hover{background:rgba(0,0,0,0.035);}
  .tl-row-label{position:sticky;left:0;z-index:2;flex:none;width:180px;margin-left:-180px;height:32px;display:flex;align-items:center;gap:5px;padding-right:8px;background:var(--ink);border-right:1px solid var(--line);}
  .tl-row-num{font-family:var(--mono);font-size:9px;color:var(--muted);width:16px;text-align:right;flex:none;}
  .tl-row-dot{width:6px;height:6px;border-radius:50%;flex:none;}
  .tl-row-name{font-size:10.5px;color:var(--ivory);line-height:1.2;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1 1 auto;min-width:0;}
  .tl-row-years{font-family:var(--mono);font-size:9px;color:var(--muted);flex:none;white-space:nowrap;}
  .tl-track{position:relative;height:32px;flex:none;}
  .tl-seg{position:absolute;top:6px;height:20px;border-radius:2px;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:default;}
  .tl-seg span{font-family:var(--mono);font-size:8.5px;letter-spacing:.04em;white-space:nowrap;padding:0 4px;color:#2B2A24;text-shadow:0 1px 0 rgba(255,255,255,.15);}
  .tl-seg.inicio{opacity:.6;}
  .tl-seg.apogeo{opacity:1;box-shadow:inset 0 0 0 1px rgba(255,255,255,0.45);}
  .tl-seg.apogeo span{color:#FFFFFF;font-weight:600;text-shadow:0 1px 1px rgba(0,0,0,.25);}
  .tl-seg.declive{opacity:.72;}
  .tl-seg.fin{opacity:.5;}
  .tl-today{position:absolute;top:0;bottom:0;width:1px;background:var(--brass);z-index:3;}
  .tl-today::before{content:'';position:absolute;top:-6px;left:-3px;width:7px;height:7px;border-radius:50%;background:var(--brass);}
  .tl-today-label{position:sticky;top:28px;transform:translateX(6px);font-family:var(--mono);font-size:9px;color:var(--brass);white-space:nowrap;display:inline-block;}
  .tl-tooltip{position:fixed;pointer-events:none;background:var(--panel-2);border:1px solid var(--brass-dim);border-radius:4px;padding:9px 12px;max-width:280px;font-size:11.5px;line-height:1.5;color:#EAE3D2;z-index:50;opacity:0;transition:opacity .1s;box-shadow:0 10px 24px rgba(0,0,0,.18);}
  .tl-tooltip.show{opacity:1;}
  .tl-tooltip .tt-title{font-family:var(--serif);font-size:12.5px;margin-bottom:3px;color:#EAE3D2;}
  .tl-tooltip .tt-range{font-family:var(--mono);color:#D8B972;font-size:10px;margin-bottom:5px;}
  .tl-tooltip .tt-desc{color:#A9A392;font-size:11px;}
</style>
</head>
<body>
<div class="tl-root">
  <div class="tl-header">
    <div class="tl-controls">
      <input class="tl-search" id="tlSearch" type="text" placeholder="Buscar imperio…">
      <div class="tl-zoom">
        <button class="tl-btn" id="tlZoomOut">–</button>
        <span id="tlZoomLabel">100%</span>
        <button class="tl-btn" id="tlZoomIn">+</button>
        <button class="tl-btn wide" id="tlGoToday">Ir a hoy</button>
        <button class="tl-btn wide" id="tlReset">Reiniciar</button>
      </div>
    </div>
    <div class="tl-legend" id="tlLegend"></div>
  </div>
  <div class="tl-scroll" id="tlScroll">
    <div class="tl-inner" id="tlInner">
      <div class="tl-axis-wrap"><div class="tl-axis" id="tlAxis"></div></div>
      <div class="tl-rows" id="tlRows"></div>
    </div>
  </div>
</div>
<div class="tl-tooltip" id="tlTooltip">
  <div class="tt-title" id="ttTitle"></div>
  <div class="tt-range" id="ttRange"></div>
  <div class="tt-desc" id="ttDesc"></div>
</div>
<script>
const MIN_YEAR=-550,MAX_YEAR=2050,TODAY=2026;
const REGIONS={
  europa:{label:"Europa y sucesores",color:"#5C8AC4"},
  islam:{label:"Mundo islámico",color:"#4FA986"},
  asiaOr:{label:"Asia oriental",color:"#D06A42"},
  sudeste:{label:"Sudeste asiático",color:"#DDB24D"},
  meso:{label:"Mesoamérica y Andes",color:"#9678C4"},
  africa:{label:"África",color:"#C99257"},
  estepa:{label:"Estepa euroasiática",color:"#8B8776"},
  surAsia:{label:"Sur de Asia",color:"#49A6AE"},
  moderno:{label:"Potencia global moderna",color:"#6C7BC4"},
};
const EMPIRES=[
 {n:"Imperio Romano (Occidente)",r:"europa",segs:[[-500,-100,"inicio","Inicio","República desde 500 a.C. / Imperio desde 27 a.C."],[-100,200,"apogeo","Apogeo","Siglos I a.C. - II d.C.: máxima expansión."],[200,300,"declive","Declive","Siglo III d.C.: crisis del siglo III."],[426,476,"fin","Fin","476 d.C.: caída de Roma."]]},
 {n:"Imperio Bizantino",r:"europa",segs:[[330,600,"inicio","Inicio","330 d.C.: fundación de Constantinopla."],[600,1000,"apogeo","Apogeo","Siglos VII-X."],[1000,1204,"declive","Declive","1054-1204: cisma, pronoia."],[1204,1453,"fin","Fin","1453: caída ante otomanos."]]},
 {n:"Califato Abbasí",r:"islam",segs:[[632,700,"inicio","Inicio","632 d.C.: muerte de Mahoma."],[700,900,"apogeo","Apogeo","750-950: dinar, red hidráulica."],[900,1258,"declive","Declive","Fragmentación por iqta'."],[1208,1258,"fin","Fin","1258: destrucción de Bagdad."]]},
 {n:"Imperio Otomano",r:"islam",segs:[[1299,1453,"inicio","Inicio","1299: fundación."],[1453,1571,"apogeo","Apogeo","Sistema timar."],[1571,1600,"declive","Declive","Derrota en Lepanto."],[1600,1922,"fin","Hasta 1922","Declive prolongado."]]},
 {n:"China (modo asiático)",r:"asiaOr",segs:[[-221,618,"inicio","Inicio","221 a.C.: unificación Qin."],[618,1279,"apogeo","Apogeo","Tang y Song."],[1279,1700,"declive","Ming-Qing","Consolidación imperial."],[1700,1912,"fin","Fin","Guerras del Opio."]]},
 {n:"India (Mughal)",r:"surAsia",segs:[[1526,1556,"inicio","Inicio","1526: fundación."],[1556,1707,"apogeo","Apogeo","Máxima extensión."],[1707,1765,"declive","Declive","Intervención británica."],[1765,1857,"fin","Fin","1857: fin formal."]]},
 {n:"Vietnam (Đại Việt)",r:"asiaOr",segs:[[968,1000,"inicio","Inicio","968 d.C.: fundación."],[1000,1400,"apogeo","Apogeo","Siglos XI-XIV."],[1400,1800,"declive","Declive","Siglos XV-XVIII."],[1800,1885,"fin","Fin","1885: colonización francesa."]]},
 {n:"Corea (Silla / Koryŏ)",r:"asiaOr",segs:[[668,700,"inicio","Inicio","668 d.C.: unificación Silla."],[700,1100,"apogeo","Apogeo","Siglos VIII-XI."],[1100,1392,"declive","Declive","Hasta fin de Koryŏ."],[1392,1910,"fin","Fin","1910: anexión japonesa."]]},
 {n:"Japón (Yamato / Heian)",r:"asiaOr",segs:[[300,600,"inicio","Inicio","300 d.C.: período Yamato."],[600,1000,"apogeo","Apogeo","Período Heian."],[1000,1185,"declive","Declive","Ascenso samurái."],[1135,1185,"fin","Fin","1185: fin régimen imperial."]]},
 {n:"Tailandia (Ayutthaya)",r:"sudeste",segs:[[1351,1400,"inicio","Inicio","1351: fundación."],[1400,1700,"apogeo","Apogeo","Siglos XV-XVII."],[1700,1767,"declive","Declive","Siglos XVII-XVIII."],[1717,1767,"fin","Fin","1767: saqueo birmano."]]},
 {n:"Birmania (Bagan)",r:"sudeste",segs:[[849,1000,"inicio","Inicio","849 d.C.: fundación."],[1000,1200,"apogeo","Apogeo","Siglos XI-XII."],[1200,1297,"declive","Declive","Siglos XII-XIII."],[1247,1297,"fin","Fin","1297: invasión mongola."]]},
 {n:"Indonesia (Majapahit)",r:"sudeste",segs:[[1293,1300,"inicio","Inicio","1293: fundación."],[1300,1450,"apogeo","Apogeo","Siglos XIV-XV."],[1450,1527,"declive","Declive","Siglo XV."],[1477,1527,"fin","Fin","1527: caída ante Demak."]]},
 {n:"Camboya (Angkor)",r:"sudeste",segs:[[802,900,"inicio","Inicio","802 d.C.: fundación."],[900,1200,"apogeo","Apogeo","Angkor Wat."],[1200,1432,"declive","Declive","Siglos XIII-XIV."],[1382,1432,"fin","Fin","1432: presión Theravada."]]},
 {n:"Imperio Azteca",r:"meso",segs:[[1428,1440,"inicio","Inicio","Triple Alianza."],[1440,1502,"apogeo","Apogeo","1440-1502."],[1502,1521,"fin","Declive / Fin","1521: conquista española."]]},
 {n:"Imperio Inca",r:"meso",segs:[[1438,1438,"inicio","Inicio","1438: expansión."],[1438,1525,"apogeo","Apogeo","1438-1525."],[1525,1533,"fin","Declive / Fin","1532-1533: conquista."]]},
 {n:"Civilización Maya",r:"meso",segs:[[250,250,"inicio","Inicio","250 d.C.: clásico."],[250,900,"apogeo","Apogeo","250-900 d.C."],[900,1647,"declive","Declive","Colapso ecológico."],[1647,1697,"fin","Fin","1697: presión española."]]},
 {n:"Ghana",r:"africa",segs:[[300,700,"inicio","Inicio","300 d.C.: formación."],[700,1100,"apogeo","Apogeo","700-1100."],[1100,1240,"declive","Declive","Siglos XI-XII."],[1190,1240,"fin","Fin","1240: caída ante Malí."]]},
 {n:"Malí",r:"africa",segs:[[1235,1312,"inicio","Inicio","1235: fundación."],[1312,1360,"apogeo","Apogeo","Mansa Musa."],[1360,1600,"fin","Declive","Presión tuareg."]]},
 {n:"Songhay",r:"africa",segs:[[1464,1493,"inicio","Inicio","1464: expansión."],[1493,1528,"apogeo","Apogeo","1493-1528."],[1528,1591,"declive","Declive","Siglo XVI."],[1541,1591,"fin","Fin","1591: invasión marroquí."]]},
 {n:"Etiopía",r:"africa",segs:[[1270,1270,"inicio","Inicio","1270: dinastía salomónica."],[1270,1529,"apogeo","Apogeo","1270-1529."],[1700,1900,"declive","Declive","Siglos XVIII-XIX."],[1900,1974,"fin","Fin","1974: caída monarquía."]]},
 {n:"Reino Zulú",r:"africa",segs:[[1816,1816,"inicio","Inicio","1816: Shaka."],[1816,1828,"apogeo","Apogeo","1816-1828."],[1828,1879,"fin","Declive / Fin","1879: derrota ante británicos."]]},
 {n:"Imperio Mongol",r:"estepa",segs:[[1206,1211,"inicio","Inicio","1206: Genghis Khan."],[1211,1294,"apogeo","Apogeo","1211-1294."],[1294,1368,"fin","Declive / Fin","1368: caída Yuan."]]},
 {n:"España Colonial",r:"europa",segs:[[1492,1521,"inicio","Inicio","1492: llegada a América."],[1521,1580,"apogeo","Apogeo","1521-1580."],[1580,1627,"declive","Declive","1590-1627."],[1627,1825,"fin","Hasta 1825","Declive prolongado."]]},
 {n:"Gran Bretaña",r:"europa",segs:[[1707,1815,"inicio","Inicio","1707: Acta de Unión."],[1815,1914,"apogeo","Apogeo","Patrón oro."],[1914,1944,"fin","Declive / Fin","Guerras mundiales."]]},
 {n:"Estados Unidos",r:"moderno",segs:[[1944,1945,"inicio","Inicio","1944: Bretton Woods."],[1945,1971,"apogeo","Apogeo","1945-1971."],[1971,2026,"fin","Declive (en curso)","1971-presente: financiarización."]]},
];
let pxPerYear=0.85;
const ZOOM_STEPS=[0.35,0.5,0.65,0.85,1.1,1.5,2.1,2.9];
let zoomIdx=3;
const activeRegions=new Set(Object.keys(REGIONS));
let searchTerm="";
function yToX(y){return (y-MIN_YEAR)*pxPerYear;}
function buildLegend(){
  const el=document.getElementById('tlLegend');el.innerHTML='';
  Object.entries(REGIONS).forEach(([key,reg])=>{
    const tag=document.createElement('div');tag.className='tl-tag';tag.dataset.region=key;
    tag.innerHTML=`<span class="tl-dot" style="background:${reg.color}"></span>${reg.label}`;
    tag.addEventListener('click',()=>{
      if(activeRegions.has(key)){if(activeRegions.size>1)activeRegions.delete(key);else Object.keys(REGIONS).forEach(k=>activeRegions.add(k));}
      else activeRegions.add(key);
      renderFilters();syncLegend();
    });
    el.appendChild(tag);
  });
}
function syncLegend(){document.querySelectorAll('.tl-tag').forEach(tag=>{tag.classList.toggle('off',!activeRegions.has(tag.dataset.region));});}
function buildAxis(){
  const axis=document.getElementById('tlAxis');axis.innerHTML='';
  const totalW=yToX(MAX_YEAR);axis.style.width=totalW+'px';
  for(let y=MIN_YEAR;y<=MAX_YEAR;y+=50){
    const tick=document.createElement('div');const isCentury=(y%100===0);
    tick.className='tl-tick'+(isCentury?' decade':'');tick.style.left=yToX(y)+'px';
    const label=y===0?'0':(y<0?`${Math.abs(y)} a.C.`:`${y}`);
    tick.innerHTML=`<span>${label}</span>`;axis.appendChild(tick);
  }
}
const tooltip=document.getElementById('tlTooltip');
const ttTitle=document.getElementById('ttTitle');
const ttRange=document.getElementById('ttRange');
const ttDesc=document.getElementById('ttDesc');
function fmtYear(y){return y<0?`${Math.abs(y)} a.C.`:`${y} d.C.`;}
function buildRows(){
  const rows=document.getElementById('tlRows');rows.innerHTML='';
  const totalW=yToX(MAX_YEAR);
  EMPIRES.forEach((emp,i)=>{
    const reg=REGIONS[emp.r];const row=document.createElement('div');
    row.className='tl-row';row.dataset.region=emp.r;row.dataset.name=emp.n.toLowerCase();
    const label=document.createElement('div');label.className='tl-row-label';
    const firstYear=emp.segs[0][0];const lastYear=emp.segs[emp.segs.length-1][1];
    const duration=lastYear-firstYear;
    label.innerHTML=`<span class="tl-row-num">${String(i+1).padStart(2,'0')}</span><span class="tl-row-dot" style="background:${reg.color}"></span><span class="tl-row-name" title="${emp.n}">${emp.n}</span><span class="tl-row-years">${duration} a.</span>`;
    row.appendChild(label);
    const track=document.createElement('div');track.className='tl-track';track.style.width=totalW+'px';
    emp.segs.forEach(([y0,y1,kind,shortLabel,desc])=>{
      const seg=document.createElement('div');seg.className='tl-seg '+kind;
      const x0=yToX(y0),x1=yToX(Math.max(y1,y0+1));
      seg.style.left=x0+'px';seg.style.width=Math.max(x1-x0,3)+'px';seg.style.background=reg.color;
      if(x1-x0>34){seg.innerHTML=`<span>${shortLabel}</span>`;}
      seg.addEventListener('mouseenter',()=>{
        ttTitle.textContent=`${emp.n} — ${shortLabel}`;
        ttRange.textContent=`${fmtYear(y0)} – ${fmtYear(y1)}`;
        ttDesc.textContent=desc;tooltip.classList.add('show');
      });
      seg.addEventListener('mousemove',(e)=>{
        tooltip.style.left=Math.min(e.clientX+14,window.innerWidth-300)+'px';
        tooltip.style.top=(e.clientY+14)+'px';
      });
      seg.addEventListener('mouseleave',()=>tooltip.classList.remove('show'));
      track.appendChild(seg);
    });
    row.appendChild(track);rows.appendChild(row);
  });
  const today=document.createElement('div');today.className='tl-today';
  today.style.left=yToX(TODAY)+'px';today.style.height=(EMPIRES.length*32)+'px';
  today.innerHTML=`<span class="tl-today-label">HOY · 2026</span>`;
  rows.appendChild(today);
}
function renderFilters(){
  document.querySelectorAll('.tl-row').forEach(row=>{
    const regionOk=activeRegions.has(row.dataset.region);
    const searchOk=!searchTerm||row.dataset.name.includes(searchTerm);
    row.classList.toggle('dim',!(regionOk&&searchOk));
  });
}
function renderAll(){
  buildAxis();buildRows();renderFilters();
  document.getElementById('tlZoomLabel').textContent=Math.round((pxPerYear/0.85)*100)+'%';
}
document.getElementById('tlSearch').addEventListener('input',(e)=>{searchTerm=e.target.value.trim().toLowerCase();renderFilters();});
function setZoom(newIdx,anchorYear){
  newIdx=Math.max(0,Math.min(ZOOM_STEPS.length-1,newIdx));
  if(newIdx===zoomIdx)return;
  const scrollEl=document.getElementById('tlScroll');const rect=scrollEl.getBoundingClientRect();
  const centerYear=anchorYear!==undefined?anchorYear:MIN_YEAR+(scrollEl.scrollLeft+rect.width/2-180)/pxPerYear;
  zoomIdx=newIdx;pxPerYear=ZOOM_STEPS[zoomIdx];renderAll();
  scrollEl.scrollLeft=yToX(centerYear)-rect.width/2+180;
}
document.getElementById('tlZoomIn').addEventListener('click',()=>setZoom(zoomIdx+1));
document.getElementById('tlZoomOut').addEventListener('click',()=>setZoom(zoomIdx-1));
document.getElementById('tlGoToday').addEventListener('click',()=>{
  const scrollEl=document.getElementById('tlScroll');const rect=scrollEl.getBoundingClientRect();
  scrollEl.scrollLeft=yToX(TODAY)-rect.width/2+180;
});
document.getElementById('tlReset').addEventListener('click',()=>{
  searchTerm='';document.getElementById('tlSearch').value='';
  Object.keys(REGIONS).forEach(k=>activeRegions.add(k));
  zoomIdx=3;pxPerYear=ZOOM_STEPS[zoomIdx];renderAll();syncLegend();
  document.getElementById('tlScroll').scrollLeft=0;
});
buildLegend();syncLegend();renderAll();
</script>
</body>
</html>
            """
            components.html(timeline_html, height=1350, scrolling=True)

        # === DESCARGA DESPUÉS DE LA LÍNEA DE TIEMPO (al 70% via columns) ===
        col_dl_i, col_dl_c, col_dl_d = st.columns([0.15, 0.70, 0.15])
        with col_dl_c:
            html_dl = '<div class="download-box" style="max-width:100%; margin:20px 0;">'
            html_dl += '<div class="dl-title">📄 Documento completo de trabajo</div>'
            html_dl += '<div class="dl-sub">Fundamentos teóricos e históricos de la acumulación, el mercado y la crisis sistémica — 60 páginas, con bibliografía completa.</div>'
            html_dl += '<a class="btn-download" href="' + PDF_URL + '" target="_blank">⬇️ Descargar PDF completo</a>'
            html_dl += '</div>'
            st.markdown(html_dl, unsafe_allow_html=True)

    # ---------- SUB-SECCIÓN 2: HEGEMONÍA DEL DÓLAR ----------
    else:
        html = '<div class="white-block">'
        html += '<span class="badge badge-purple">LÍNEA PRINCIPAL</span>'
        html += '<h2 class="section-title-big" style="font-size:1.5rem;">Hegemonía del Dólar y Crisis Sistémica</h2>'
        html += '<p class="section-subtitle">Análisis del régimen monetario contemporáneo (1944 – presente)</p>'
        html += '<p class="abstract-text" style="margin-top:16px;">El <strong>CEMBU OHD</strong> analiza la crisis actual del dólar no como una mera crisis financiera, sino como una <strong>crisis sistémica</strong> que combina causas endógenas (financiarización, deslocalización industrial, destrucción de la masa productiva) y exógenas (ascenso de China y los BRICS+).</p>'
        html += '<div class="struct-block"><strong>Bretton Woods (1944):</strong> el dólar como equivalente general del sistema capitalista global, convertible en oro a 35 USD/onza.</div>'
        html += '<div class="struct-block"><strong>Nixon Shock (1971):</strong> fin de la convertibilidad. El dólar se convierte en moneda Fiat (sin respaldo metálico), sostenida por poder militar y financiero.</div>'
        html += '<div class="struct-block"><strong>Régimen del Petrodólar (1971-presente):</strong> alianza EE.UU.-Arabia Saudita establece que el petróleo se comercia en dólares. La financiarización reemplaza a la producción industrial como motor de la acumulación.</div>'
        html += '<p class="abstract-text">La contradicción decisión-ejecución se reproduce hoy: la élite financiera toma decisiones que fragmentan la base productiva global y aceleran la crisis —repitiendo la misma lógica de la Pronoia, la Iqta\' y el Timar.</p>'
        html += '<div class="placeholder-box"><span class="ph-icon">🌐</span><b>Próximamente: Mapas y Monitor Monetario</b><br>Seguimiento de tasas Fed, BCE, BoJ — Flujos globales — Indicadores de desdolarización</div>'
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)

    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PROYS --------------------
elif pestana == "PROYS":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_PROYS + '" alt="PROYS">'
    html += '<div><span class="badge badge-blue">PROYS</span>'
    html += '<h1 class="section-title-big">Consultoría Territorial con Modelización Predictiva</h1>'
    html += '<p class="section-subtitle">Líneas de base, monitoreo, evaluación y modelización predictiva</p></div></div>'
    html += '<p class="abstract-text"><strong>CEMBU Proys.</strong> es el servicio de consultoría territorial del CEMBU, orientado a proveer a gobiernos locales, organizaciones sociales y universidades de herramientas técnicas para el diseño, monitoreo y evaluación de políticas públicas.</p>'
    html += '<div class="struct-block"><strong>Estructura — 4 líneas de servicio:</strong> (1) Líneas de base. (2) Sistemas de monitoreo. (3) Evaluación de impacto. (4) Modelización predictiva.</div>'
    html += '<div class="placeholder-box"><span class="ph-icon">📈</span><b>Próximamente: Tablero de Proyectos</b><br>Casos de éxito — Metodologías — Simulación de escenarios</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- SERV_CONS --------------------
elif pestana == "SERV_CONS":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_SERV + '" alt="SERVICIOS">'
    html += '<div><span class="badge badge-red">SERVICIOS & CONSULTORÍA</span>'
    html += '<h1 class="section-title-big">Consultoría Electoral y Territorial</h1>'
    html += '<p class="section-subtitle">Segmentación electoral, historia del voto e identidades territoriales</p></div></div>'
    html += '<p class="abstract-text"><strong>CEMBU Serv. Cons.</strong> es el servicio de consultoría electoral y territorial del CEMBU, orientado a proveer a partidos políticos, municipios y organizaciones sociales de información estratégica sobre el comportamiento electoral.</p>'
    html += '<div class="struct-block"><strong>Estructura — 5 líneas:</strong> (1) Radiografía del votante. (2) Consumos culturales. (3) Horizontes de expectativas. (4) Mapeo de valores. (5) Modelización predictiva electoral.</div>'
    html += '<div class="placeholder-box"><span class="ph-icon">🗳️</span><b>Próximamente: Análisis Electoral</b><br>Segmentación territorial — Mapa de identidades — Modelización de escenarios</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PUBS_DIF --------------------
elif pestana == "PUBS_DIF":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    html = '<div class="white-block">'
    html += '<div class="section-header">'
    html += '<img class="section-logo" src="' + LOGO_PUBS + '" alt="PUBLICACIONES">'
    html += '<div><span class="badge badge-teal">PUBLICACIONES & DIFUSIÓN</span>'
    html += '<h1 class="section-title-big">Producción Académica y Divulgación</h1>'
    html += '<p class="section-subtitle">Papers, informes técnicos y materiales de divulgación del conocimiento territorial</p></div></div>'
    html += '<p class="abstract-text">El área de <strong>Publicaciones y Difusión</strong> del CEMBU reúne la producción académica, los informes técnicos, los materiales de divulgación y las actividades de transferencia de conocimiento hacia la sociedad.</p>'
    html += '<div class="struct-block"><strong>Tipos de producción:</strong> Papers académicos, informes técnicos, working papers y materiales de divulgación.</div>'
    html += '<div class="placeholder-box"><span class="ph-icon">📚</span><b>Próximamente: Repositorio de Publicaciones</b><br>Papers — Informes técnicos — Notas de coyuntura</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CONTACTO --------------------
elif pestana == "CONTACTO":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown("""
<div class="white-block">
    <div class="block-title">📬 Contacto CEMBU</div>
    <div class="block-sub">Podés comunicarte con nuestro equipo por los siguientes medios:</div>
    <div style="margin-top: 14px; line-height: 2.2; font-size: 1rem;">
        👤 <b>Director Ejecutivo:</b> Darío Fabián García<br>
        📧 <b>Email:</b> <span class="footer-copy-box">dariofgarcia@yahoo.com</span><br>
        📱 <b>WhatsApp:</b> <a href="https://wa.me/5491149938695" target="_blank" class="footer-link">(011) 15-4993-8695</a><br>
        📞 <b>Teléfono:</b> (011) 15-4993-8695<br>
        📍 <b>Ubicación:</b> Ciudad Autónoma de Buenos Aires (CABA), Argentina
    </div>
    <div style="margin-top: 20px;">
        <a href="https://wa.me/5491149938695" target="_blank" class="btn-contacto btn-whatsapp">💬 Enviar WhatsApp</a>
        <a href="mailto:dariofgarcia@yahoo.com" class="btn-contacto btn-email">✉️ Enviar Email</a>
    </div>
</div>
""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 6. FOOTER
# ============================================================
st.markdown("""
<div class="cembu-footer">
    <div class="footer-grid">
        <div class="footer-col">
            <div class="footer-title">CEMBU</div>
            <div style="font-size:0.9rem; color:#8b949e; line-height:1.5;">
                Centro de Estudios Manuel Baldomero Ugarte.<br>
                Conocimiento territorial para el desarrollo soberano.
            </div>
        </div>
        <div class="footer-col">
            <div class="footer-title">Contacto Directo</div>
            <div class="footer-item">👤 <b>Director:</b> Darío Fabián García</div>
            <div class="footer-item">📧 <b>Email:</b> <span class="footer-copy-box">dariofgarcia@yahoo.com</span></div>
            <div class="footer-item">📱 <b>WhatsApp:</b> <a href="https://wa.me/5491149938695" target="_blank" class="footer-link">(011) 15-4993-8695</a></div>
        </div>
        <div class="footer-col">
            <div class="footer-title">Ubicación</div>
            <div class="footer-item">📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina</div>
        </div>
    </div>
    <div class="footer-bottom">© CEMBU - Todos los derechos reservados.</div>
</div>
""", unsafe_allow_html=True)
