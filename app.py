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

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    .stApp > header { display: none !important; }
    section.main > div:first-child { padding-top: 0 !important; }
    #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }

    /* ---------- BANNER NEGRO SUPERIOR ---------- */
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

    /* ---------- BARRA DE MENÚ CON BOTONES ---------- */
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

    /* ---------- CONTENEDOR PRINCIPAL ---------- */
    .content-container { padding: 24px 40px 0 40px; }

    /* ---------- TARJETAS DEL TRIÁNGULO ---------- */
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

    /* ---------- BLOQUES BLANCOS ---------- */
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
    .block-sub {
        font-size: 0.78rem;
        color: #64748B;
        margin-bottom: 12px;
    }

    /* ---------- SECCIONES DE CONTENIDO ---------- */
    .section-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 10px;
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

    /* Párrafos del abstract */
    .abstract-text {
        font-size: 0.95rem;
        color: #334155;
        line-height: 1.7;
        margin-bottom: 14px;
    }
    .abstract-text strong { color: #0F172A; }

    /* Bloques de estructura */
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

    /* Caja de "contenido futuro" */
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

    /* ---------- BADGES ---------- */
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

    /* ---------- TARJETAS DE UNIDADES CON LOGO ---------- */
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
    .unit-desc {
        font-size: 0.78rem;
        color: #64748B;
        line-height: 1.4;
    }

    /* ---------- FOOTER ---------- */
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

    /* ---------- BOTONES CONTACTO ---------- */
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
# URLs de logos
# ============================================================
BASE_URL = "https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/"
LOGO_LAB = BASE_URL + "CEMBU_LAB_logo.png"
LOGO_MATRIA = BASE_URL + "2_MATRIA.png"
LOGO_OHD = BASE_URL + "3_OHD.png"
LOGO_PROYS = BASE_URL + "4_PROYS.png"
LOGO_SERV = BASE_URL + "5_SERV_CONS.png"
LOGO_PUBS = BASE_URL + "6_PUBS_DIF.png"

# ============================================================
# FUNCIÓN: bloque de contacto al final de cada sección
# ============================================================
def bloque_contacto():
    st.markdown("""
    <div class="white-block" style="background: #0B0F19; color: #E2E8F0; margin-top: 20px;">
        <div style="font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #EA580C; font-weight: 800; margin-bottom: 10px;">📬 Contacto</div>
        <div style="font-size: 0.92rem; line-height: 2;">
            <b>Darío Fabián García</b> — Director Ejecutivo<br>
            📧 <a href="mailto:dariofgarcia@yahoo.com" style="color:#25D366; text-decoration:none; font-weight:bold;">dariofgarcia@yahoo.com</a><br>
            📱 <a href="https://wa.me/5491149938695" target="_blank" style="color:#25D366; text-decoration:none; font-weight:bold;">(011) 15-4993-8695</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            body { margin: 0; font-family: 'Inter', sans-serif; background: transparent; }
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
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_LAB}" alt="CEMBU LAB"><span class="badge badge-red">CEMBU LAB</span><div class="unit-title">Modelos & Algoritmos</div><div class="unit-desc">Plataforma de inteligencia territorial: base de datos y modelos predictivos.</div></div>''', unsafe_allow_html=True)
    with m2:
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_MATRIA}" alt="MATRIA"><span class="badge badge-teal">MATRIA</span><div class="unit-title">Matriz Productiva Popular</div><div class="unit-desc">La data al servicio de la matriz productiva popular.</div></div>''', unsafe_allow_html=True)
    with m3:
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_OHD}" alt="OHD"><span class="badge badge-purple">OHD MONETARIO</span><div class="unit-title">Hegemonía del Dólar</div><div class="unit-desc">Seguimiento crítico del sistema monetario global.</div></div>''', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    p1, p2 = st.columns(2, gap="small")
    with p1:
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_PROYS}" alt="PROYECTOS"><span class="badge badge-blue">PROYECTOS</span><div class="unit-title">Consultoría Territorial</div><div class="unit-desc">Líneas de base, monitoreo, evaluación y modelización predictiva.</div></div>''', unsafe_allow_html=True)
    with p2:
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_SERV}" alt="SERVICIOS"><span class="badge badge-red">SERVICIOS & CONSULTORÍA</span><div class="unit-title">Consultoría Electoral</div><div class="unit-desc">Segmentación electoral, historia del voto e identidades territoriales.</div></div>''', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1], gap="small")
    with c2:
        st.markdown(f'''<div class="unit-card"><img class="unit-logo" src="{LOGO_PUBS}" alt="PUBLICACIONES"><span class="badge badge-teal">PUBLICACIONES & DIFUSIÓN</span><div class="unit-title">Producción Académica</div><div class="unit-desc">Papers, informes técnicos y materiales de divulgación.</div></div>''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CEMBU LAB --------------------
elif pestana == "CEMBU LAB":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_LAB}" alt="CEMBU LAB">
            <div>
                <span class="badge badge-red">CEMBU LAB</span>
                <h1 class="section-title-big">Plataforma de Inteligencia Territorial</h1>
                <p class="section-subtitle">Base de datos y modelos predictivos para el desarrollo con soberanía</p>
            </div>
        </div>

        <p class="abstract-text">
            <strong>CEMBU Lab</strong> es la plataforma de inteligencia territorial del CEMBU, orientada a generar, procesar y modelizar datos para el diseño de políticas públicas de desarrollo territorial, con foco en la Provincia de Buenos Aires y CABA.
        </p>

        <div class="struct-block">
            <strong>Justificación:</strong> La mayoría de los centros de estudios y gobiernos locales no cuentan con una infraestructura de datos robusta ni capacidades de modelización predictiva, lo que genera políticas reactivas y discontinuidad del acumulado técnico. CEMBU Lab se propone llenar ese vacío.
        </div>

        <div class="struct-block">
            <strong>Estructura:</strong> Se organiza en tres capas: <br>
            (1) <b>Infraestructura de datos</b> — 33 fuentes, 5 niveles, 8 unidades de análisis, series 1960-2026.<br>
            (2) <strong>Modelos predictivos</strong> — complejidad económica, ABM, simulación sectorial, predicción de demanda.<br>
            (3) <strong>Dashboards y transferencia</strong> — tableros interactivos, informes a medida, capacitación.
        </div>

        <div class="struct-block">
            <strong>Árbol de Problemas:</strong> Aborda la fragmentación de datos, la fragmentación de capacidades técnicas y la baja articulación entre academia y gobiernos locales.
        </div>

        <div class="struct-block">
            <strong>Características propias:</strong> Integración de fuentes, modelización avanzada, acceso abierto parcial y servicios a medida para gobiernos y organizaciones.
        </div>

        <div class="struct-block">
            <strong>Gobernanza:</strong> Dirección Técnica, Comité Científico (universidades asociadas) y usuarios externos. Blindaje mediante acuerdos de confidencialidad y licencias que garantizan neutralidad técnica.
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">📊</span>
            <b>Próximamente: Dashboard Interactivo</b><br>
            Datos a nivel macro, meso y micro — Modelos predictivos — Series 1960-2026
        </div>
    </div>
    ''', unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- MATRIA --------------------
elif pestana == "MATRIA":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_MATRIA}" alt="MATRIA">
            <div>
                <span class="badge badge-teal">MATRIA</span>
                <h1 class="section-title-big">La Data al Servicio de la Matriz Productiva Popular</h1>
                <p class="section-subtitle">Relevamiento territorial de encadenamientos productivos</p>
            </div>
        </div>

        <p class="abstract-text">
            <strong>MATRIA</strong> es el espacio del CEMBU dedicado al relevamiento y análisis de la matriz productiva popular, con foco en los encadenamientos productivos, las unidades de producción (UPS) y la construcción de una matriz insumo-producto desde el territorio.
        </p>

        <div class="struct-block">
            <strong>Ejes de trabajo:</strong> Relevamiento de Unidades de Producción (UPS), análisis de encadenamientos productivos, construcción de matriz insumo-producto territorial, identificación de cuellos de botella y oportunidades.
        </div>

        <div class="struct-block">
            <strong>Enfoque:</strong> Articulación entre actores territoriales, cooperativas, pequeñas unidades productivas y gobiernos locales para fortalecer la matriz productiva popular.
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">🗺️</span>
            <b>Próximamente: Mapa Productivo Interactivo</b><br>
            Relevamiento de UPS — Encadenamientos productivos — Matriz insumo-producto
        </div>
    </div>
    ''', unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- OHD --------------------
elif pestana == "OHD":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_OHD}" alt="OHD">
            <div>
                <span class="badge badge-purple">OHD</span>
                <h1 class="section-title-big">Observatorio de la Hegemonía del Dólar</h1>
                <p class="section-subtitle">Análisis teórico-histórico de la moneda, los regímenes de acumulación y la crisis sistémica</p>
            </div>
        </div>

        <p class="abstract-text">
            El <strong>CEMBU OHD</strong> es un observatorio del CEMBU dedicado al análisis teórico-histórico de la moneda, los regímenes de acumulación y la crisis sistémica, desde una perspectiva crítico-materialista y de sociología histórica comparada.
        </p>

        <div class="struct-block">
            <strong>Justificación:</strong> La hegemonía del dólar estadounidense está en crisis. La financiarización, la deslocalización industrial y el ascenso de China y los BRICS+ están desafiando el monopolio del dólar como moneda de reserva global. El CEMBU OHD se propone rastrear cómo la forma moneda, el mercado y la extracción del valor han mutado hasta la hegemonía contemporánea del dólar, y explorar las alternativas emergentes.
        </div>

        <div class="struct-block">
            <strong>Enfoque metodológico — 3 ejes analíticos:</strong><br>
            <b>1. Ley de los Grandes Números</b> como patrón de estabilización sistémica: a mayor masa de productores o aportantes, mayor capacidad del sistema para amortiguar perturbaciones.<br>
            <b>2. Dialéctica Decisión vs. Ejecución:</b> contradicción recurrente entre la decisión centralizada y la ejecución fragmentada.<br>
            <b>3. Moneda como cristalización de las relaciones sociales:</b> la historia de la moneda es la historia de las formas de expropiación del trabajo y de la lucha de clases.
        </div>

        <div class="struct-block">
            <strong>Contenido del documento base:</strong><br>
            • <b>Parte I:</b> Marco teórico-metodológico (ontología del sujeto histórico, ley de los grandes números, dialéctica decisión-ejecución).<br>
            • <b>Parte II:</b> Sistema-mundo precapitalista (imperios tributarios de Eurasia, Asia Oriental, América y África; feudalismo europeo como región marginal).<br>
            • <b>Parte III:</b> Transición al capitalismo y hegemonía del dólar (colonialismo atlántico, capitalismo industrial, régimen del petrodólar).<br>
            • <b>Parte IV:</b> Conclusiones teóricas y líneas de investigación futuras.
        </div>

        <div class="struct-block">
            <strong>Líneas de investigación futuras:</strong><br>
            1. La transición del patrón oro al sistema Fiat (1971).<br>
            2. La financiarización y la crisis de la deuda.<br>
            3. El desafío de los BRICS+ y las alternativas al dólar.<br>
            4. La moneda como cristalización de las nuevas relaciones de producción (economía de plataformas, trabajo precario, inteligencia artificial).
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">🌐</span>
            <b>Próximamente: Mapas y Monitor Monetario</b><br>
            Seguimiento de tasas Fed, BCE, BoJ — Flujos globales — Indicadores de desdolarización
        </div>
    </div>
    ''', unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PROYS --------------------
elif pestana == "PROYS":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_PROYS}" alt="PROYS">
            <div>
                <span class="badge badge-blue">PROYS</span>
                <h1 class="section-title-big">Consultoría Territorial con Modelización Predictiva</h1>
                <p class="section-subtitle">Líneas de base, monitoreo, evaluación y modelización predictiva</p>
            </div>
        </div>

        <p class="abstract-text">
            <strong>CEMBU Proys.</strong> es el servicio de consultoría territorial del CEMBU, orientado a proveer a gobiernos locales, organizaciones sociales y universidades de herramientas técnicas para el diseño, monitoreo y evaluación de políticas públicas y proyectos de desarrollo territorial.
        </p>

        <div class="struct-block">
            <strong>Justificación:</strong> La mayoría de los municipios y organizaciones sociales carecen de capacidades técnicas para medir el impacto de sus intervenciones y de herramientas predictivas para anticipar escenarios. Esto genera proyectos reactivos, discontinuidad en la gestión y dificultades para acceder a financiamiento.
        </div>

        <div class="struct-block">
            <strong>Estructura — 4 líneas de servicio:</strong><br>
            (1) <b>Líneas de base</b> — diagnósticos territoriales rigurosos.<br>
            (2) <b>Sistemas de monitoreo</b> — dashboards y tableros de control.<br>
            (3) <b>Evaluación de impacto</b> — ex-post y longitudinal.<br>
            (4) <b>Modelización predictiva</b> — simulación de escenarios.
        </div>

        <div class="struct-block">
            <strong>Árbol de Problemas:</strong> Aborda las limitaciones en la gestión de programas estatales, la baja conexión entre universidad y gobiernos locales, y la dependencia del presupuesto público sin sistemas de medición de resultados.
        </div>

        <div class="struct-block">
            <strong>Características propias:</strong> Enfoque integral (cubre todo el ciclo de un proyecto), basado en datos robustos del CEMBU Lab (33 fuentes, series 1960-2026), modelización predictiva aplicada, transferencia de capacidades a equipos locales, y facilitación del acceso a financiamiento internacional.
        </div>

        <div class="struct-block">
            <strong>Gobernanza:</strong> Dirección Técnica, Comité Científico (CEMBU + Universidades) y usuarios externos. Blindaje mediante acuerdos de confidencialidad y licencias que garantizan neutralidad técnica.
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">📈</span>
            <b>Próximamente: Tablero de Proyectos</b><br>
            Casos de éxito — Metodologías — Simulación de escenarios
        </div>
    </div>
    ''', unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- SERV_CONS --------------------
elif pestana == "SERV_CONS":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_SERV}" alt="SERVICIOS">
            <div>
                <span class="badge badge-red">SERVICIOS & CONSULTORÍA</span>
                <h1 class="section-title-big">Consultoría Electoral y Territorial</h1>
                <p class="section-subtitle">Segmentación electoral, historia del voto e identidades territoriales</p>
            </div>
        </div>

        <p class="abstract-text">
            <strong>CEMBU Serv. Cons.</strong> es el servicio de consultoría electoral y territorial del CEMBU, orientado a proveer a partidos políticos, municipios y organizaciones sociales de información estratégica sobre el comportamiento electoral, la segmentación poblacional y las identidades territoriales.
        </p>

        <div class="struct-block">
            <strong>Justificación:</strong> La mayoría de los actores políticos y territoriales carecen de información confiable, segmentada y dinámica sobre el electorado, lo que genera estrategias basadas en intuiciones o datos desactualizados.
        </div>

        <div class="struct-block">
            <strong>Estructura — 5 líneas de servicio:</strong><br>
            (1) <b>Radiografía del votante</b> — perfiles sociodemográficos, ideológicos, coyunturales.<br>
            (2) <b>Consumos culturales</b> como indicadores de identidad.<br>
            (3) <b>Horizontes de expectativas</b> y demandas ciudadanas.<br>
            (4) <b>Mapeo de valores</b> y sentido común.<br>
            (5) <b>Modelización predictiva electoral</b>.
        </div>

        <div class="struct-block">
            <strong>Árbol de Problemas:</strong> Aborda la fragmentación de datos electorales, la ausencia de capacidades técnicas, y la baja articulación entre academia y actores políticos.
        </div>

        <div class="struct-block">
            <strong>Características propias:</strong> Basado en datos robustos del CEMBU Lab, enfoque multidimensional, segmentación territorial, y alianza operativa con <b>Pulso Táctico</b> para trabajo de campo (encuestas, relevamientos). El CEMBU mantiene neutralidad institucional.
        </div>

        <div class="struct-block">
            <strong>Gobernanza:</strong> Dirección Técnica del CEMBU, aliado operativo (Pulso Táctico) y usuarios externos. Blindaje mediante acuerdos de confidencialidad.
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">🗳️</span>
            <b>Próximamente: Análisis Electoral</b><br>
            Segmentación territorial — Mapa de identidades — Modelización de escenarios
        </div>
    </div>
    ''', unsafe_allow_html=True)
    bloque_contacto()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PUBS_DIF --------------------
elif pestana == "PUBS_DIF":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="white-block">
        <div class="section-header">
            <img class="section-logo" src="{LOGO_PUBS}" alt="PUBLICACIONES">
            <div>
                <span class="badge badge-teal">PUBLICACIONES & DIFUSIÓN</span>
                <h1 class="section-title-big">Producción Académica y Divulgación</h1>
                <p class="section-subtitle">Papers, informes técnicos y materiales de divulgación del conocimiento territorial</p>
            </div>
        </div>

        <p class="abstract-text">
            El área de <strong>Publicaciones y Difusión</strong> del CEMBU reúne la producción académica, los informes técnicos, los materiales de divulgación y las actividades de transferencia de conocimiento hacia la sociedad.
        </p>

        <div class="struct-block">
            <strong>Tipos de producción:</strong><br>
            • <b>Papers académicos</b> — investigaciones originales con rigor metodológico.<br>
            • <b>Informes técnicos</b> — documentos aplicados para gobiernos y organizaciones.<br>
            • <b>Working papers</b> — avances de investigación y discusión.<br>
            • <b>Materiales de divulgación</b> — notas, artículos y contenidos para público general.
        </div>

        <div class="struct-block">
            <strong>Actividades:</strong> Participación en congresos, seminarios, mesas de debate, presentaciones en universidades nacionales e internacionales, y articulación con centros de estudios afines.
        </div>

        <div class="placeholder-box">
            <span class="ph-icon">📚</span>
            <b>Próximamente: Repositorio de Publicaciones</b><br>
            Papers — Informes técnicos — Notas de coyuntura — Materiales de divulgación
        </div>
    </div>
    ''', unsafe_allow_html=True)
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
