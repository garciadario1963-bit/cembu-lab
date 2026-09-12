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
# 2. ESTILOS CSS (FULL-BLEED + BANNER NEGRO CONTINUO)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    /* ---------- RESET Y FULL-BLEED ---------- */
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
    }

    .logo-container img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

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

    .social-link:hover {
        color: #EA580C;
        transform: translateY(-2px);
    }

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

    /* ---------- BARRA DE NAVEGACIÓN NEGRA FULL-WIDTH ---------- */
    div[data-testid="stRadio"] {
        background-color: #0B0F19;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        padding: 12px 0 14px 0;
        border-bottom: 3px solid #EA580C;
        box-sizing: border-box;
    }

    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    /* Ocultar SOLO el círculo del radio, no el texto */
    div[data-testid="stRadio"] label > div:first-child {
        display: none !important;
    }

    /* Estilo base de cada opción del menú - LETRAS CLARAS */
    div[data-testid="stRadio"] label {
        background-color: transparent !important;
        color: #E2E8F0 !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        padding: 8px 18px !important;
        border-radius: 4px !important;
        cursor: pointer;
        transition: all 0.2s ease;
        border-bottom: 2px solid transparent;
        letter-spacing: 0.3px;
    }

    div[data-testid="stRadio"] label:hover {
        color: #FFFFFF !important;
        background-color: rgba(234, 88, 12, 0.12) !important;
    }

    div[data-testid="stRadio"] label:has(input:checked) {
        color: #EA580C !important;
        border-bottom: 2px solid #EA580C !important;
    }

    div[data-testid="stRadio"] label p,
    div[data-testid="stRadio"] label span,
    div[data-testid="stRadio"] label div {
        color: inherit !important;
        font-size: inherit !important;
        margin: 0 !important;
    }

    div[data-testid="stRadio"] > div {
        width: 100% !important;
    }

    /* ---------- CONTENEDOR PRINCIPAL ---------- */
    .content-container {
        padding: 24px 40px 0 40px;
    }

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
        padding: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
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
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .unit-logo {
        max-width: 80px;
        max-height: 80px;
        object-fit: contain;
        margin-bottom: 10px;
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
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. HEADER NEGRO (con LOGO REAL del repo + redes sociales)
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
# 4. MENÚ HORIZONTAL (fondo negro full-width, letras claras)
# ============================================================
pestana = st.radio(
    "nav",
    ["Menú", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True,
    label_visibility="collapsed",
    key="main_nav"
)

# Truco: si elige "Menú", mostramos el Tablero de Control
if pestana == "Menú":
    pestana = "Tablero de Control"

# ============================================================
# 5. CONTENIDO POR PESTAÑA
# ============================================================

if pestana == "Tablero de Control":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # A) Tres puntas del triángulo
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.markdown('<div class="triangle-card card-a"><div class="tri-title-a">1. Decisión & Ejecución</div><div class="tri-desc">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="triangle-card card-b"><div class="tri-title-b">2. Análisis & Modelización</div><div class="tri-desc">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="triangle-card card-c"><div class="tri-title-c">3. Transformación Real</div><div class="tri-desc">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    # B) Carrusel + Mapa Folium
    col_left, col_right = st.columns([1.1, 1], gap="small")

    with col_left:
        st.markdown('<div class="white-block" style="padding-bottom: 8px;"><span class="badge badge-red">NOVEDADES & ACTIVIDADES</span><div class="block-title">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</div><div class="block-sub" style="margin-bottom: 8px;">Nuestras últimas actividades académicas y avances en análisis regional.</div></div>', unsafe_allow_html=True)

        carrusel_html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body { margin: 0; font-family: 'Inter', sans-serif; background: transparent; }
            .carousel-container { position: relative; width: 100%; height: 220px; overflow: hidden; border-radius: 6px; }
            .slide { position: absolute; width: 100%; height: 100%; opacity: 0; transition: opacity 1s ease-in-out; }
            .slide.active { opacity: 1; }
            .slide img { width: 100%; height: 100%; object-fit: cover; }
            .caption { position: absolute; bottom: 0; background: rgba(15, 23, 42, 0.85); color: #fff; width: 100%; padding: 8px 12px; font-size: 12px; box-sizing: border-box; }
            .dots-container { position: absolute; top: 10px; right: 12px; display: flex; gap: 6px; z-index: 10; }
            .dot { width: 10px; height: 10px; background-color: rgba(255,255,255,0.5); border-radius: 50%; display: inline-block; cursor: pointer; }
            .dot.active-dot { background-color: #EA580C; }
        </style>
        </head>
        <body>
        <div class="carousel-container">
            <div class="dots-container">
                <span class="dot active-dot" onclick="setSlide(0)"></span>
                <span class="dot" onclick="setSlide(1)"></span>
            </div>
            <div class="slide active">
                <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=700&auto=format&fit=crop&q=60" alt="CLACSO">
                <div class="caption"><b>1 / 2 — CLACSO EN LA FILUNI:</b> Participación institucional en México.</div>
            </div>
            <div class="slide">
                <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?w=700&auto=format&fit=crop&q=60" alt="Monitor Territorial">
                <div class="caption"><b>2 / 2 — MONITOR TERRITORIAL:</b> Mapeo dinámico e infraestructura regional.</div>
            </div>
        </div>
        <script>
            let currentSlide = 0;
            const slides = document.querySelectorAll('.slide');
            const dots = document.querySelectorAll('.dot');
            function showSlide(index) {
                slides.forEach((slide, i) => {
                    slide.classList.remove('active');
                    dots[i].classList.remove('active-dot');
                });
                slides[index].classList.add('active');
                dots[index].classList.add('active-dot');
            }
            function nextSlide() {
                currentSlide = (currentSlide + 1) % slides.length;
                showSlide(currentSlide);
            }
            function setSlide(index) {
                currentSlide = index;
                showSlide(currentSlide);
            }
            setInterval(nextSlide, 3500);
        </script>
        </body>
        </html>
        """
        components.html(carrusel_html, height=230)

    with col_right:
        st.markdown('<div class="white-block"><div class="block-title">📍 Tablero de Control Territorial & Modelización</div><div class="block-sub">📌 Monitor Territorial: Región Metropolitana / AMBA</div></div>', unsafe_allow_html=True)

        m = folium.Map(location=[-34.6037, -58.3816], zoom_start=10, tiles="CartoDB positron")
        folium.Marker(
            [-34.6037, -58.3816],
            popup="Sede Central CABA",
            tooltip="CEMBU AMBA",
            icon=folium.Icon(color="orange", icon="info-sign")
        ).add_to(m)
        st_folium(m, width="100%", height=210, returned_objects=[])

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    # C) Fila 1: CEMBU LAB, MATRIA, OHD
    m1, m2, m3 = st.columns(3, gap="small")

    with m1:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/CEMBU_LAB_logo.png" alt="CEMBU LAB">
            <span class="badge badge-red">CEMBU LAB</span>
            <div class="unit-title">Modelos & Algoritmos</div>
            <div class="unit-desc">Planificación del desarrollo mediante simulaciones de agentes y coyuntura.</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/2_MATRIA.png" alt="MATRIA">
            <span class="badge badge-teal">MATRIA</span>
            <div class="unit-title">Unidades de Producción (UPS)</div>
            <div class="unit-desc">Relevamiento territorial de encadenamientos productivos y matriz insumo-producto.</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/3_OHD.png" alt="OHD">
            <span class="badge badge-purple">OHD MONETARIO</span>
            <div class="unit-title">Tasas & Liquidez Global</div>
            <div class="unit-desc">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores monetarios.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    # D) Fila 2: PROYECTOS y SERVICIOS & CONSULTORÍA
    p1, p2 = st.columns(2, gap="small")

    with p1:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/4_PROYS.png" alt="PROYECTOS">
            <span class="badge badge-blue">PROYECTOS</span>
            <div class="unit-title">Proyectos Estratégicos</div>
            <div class="unit-desc">Diseño y ejecución de proyectos de desarrollo territorial y planificación estratégica.</div>
        </div>
        """, unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/5_SERV_CONS.png" alt="SERVICIOS Y CONSULTORÍA">
            <span class="badge badge-red">SERVICIOS & CONSULTORÍA</span>
            <div class="unit-title">Asistencia Técnica</div>
            <div class="unit-desc">Servicios profesionales de consultoría para organismos públicos y privados.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    # E) Fila 3: PUBLICACIONES Y DIFUSIÓN (centrada)
    c1, c2, c3 = st.columns([1, 2, 1], gap="small")
    with c2:
        st.markdown("""
        <div class="unit-card">
            <img class="unit-logo" src="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/assets/6_PUBS_DIF.png" alt="PUBLICACIONES">
            <span class="badge badge-teal">PUBLICACIONES & DIFUSIÓN</span>
            <div class="unit-title">Producción Académica</div>
            <div class="unit-desc">Papers, informes técnicos y materiales de divulgación del conocimiento territorial.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif pestana == "CEMBU LAB":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="white-block"><span class="badge badge-red">CEMBU LAB</span><div class="block-title">Laboratorio de Innovación y Métodos</div><div class="block-sub">Sección en desarrollo: modelos, algoritmos y simulaciones territoriales.</div></div></div>', unsafe_allow_html=True)

elif pestana == "CEMBU MATRIA":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="white-block"><span class="badge badge-teal">MATRIA</span><div class="block-title">Observatorio de Desarrollo Territorial</div><div class="block-sub">Sección en desarrollo: encadenamientos productivos y matriz insumo-producto.</div></div></div>', unsafe_allow_html=True)

elif pestana == "CEMBU OHD":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="white-block"><span class="badge badge-purple">OHD MONETARIO</span><div class="block-title">Análisis Macroeconómico y Financiero</div><div class="block-sub">Sección en desarrollo: tasas Fed, BCE, BoJ e indicadores monetarios globales.</div></div></div>', unsafe_allow_html=True)

elif pestana == "Microdatos":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="white-block"><div class="block-title">📊 Repositorio de Microdatos</div><div class="block-sub">Sección en desarrollo: bases de datos y series estadísticas.</div></div></div>', unsafe_allow_html=True)

elif pestana == "Contacto":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="white-block">
        <div class="block-title">📬 Contacto CEMBU</div>
        <div class="block-sub">Podés comunicarte con nuestro equipo por los siguientes medios:</div>
        <div style="margin-top: 14px; line-height: 2;">
            📧 <b>Email:</b> <span class="footer-copy-box">contacto@cembu.org</span><br>
            📱 <b>WhatsApp:</b> <a href="https://wa.me/5491149938695" target="_blank" class="footer-link">11-4993-8695</a><br>
            📞 <b>Teléfono:</b> 11-4993-8695<br>
            📍 <b>Ubicación:</b> Ciudad Autónoma de Buenos Aires (CABA), Argentina
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 6. FOOTER FULL-WIDTH
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
            <div class="footer-item">📧 <b>Email:</b> <span class="footer-copy-box">contacto@cembu.org</span></div>
            <div class="footer-item">📱 <b>WhatsApp:</b> <a href="https://wa.me/5491149938695" target="_blank" class="footer-link">11-4993-8695</a></div>
            <div class="footer-item">📞 <b>Teléfono:</b> 11-4993-8695</div>
        </div>
        <div class="footer-col">
            <div class="footer-title">Ubicación</div>
            <div class="footer-item">📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina</div>
        </div>
    </div>
    <div class="footer-bottom">© CEMBU - Todos los derechos reservados.</div>
</div>
""", unsafe_allow_html=True)
