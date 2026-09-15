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
            function showSlide(index) { slides
