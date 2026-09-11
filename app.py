import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="CEMBU - Conocimiento territorial para el desarrollo soberano",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Meta tags para redes sociales (Open Graph)
st.markdown(
    """
    <head>
        <meta property="og:title" content="CEMBU - Conocimiento territorial para el desarrollo soberano" />
        <meta property="og:description" content="Plataforma de análisis socioeconómico, monitor territorial, microdatos y tableros de control para el desarrollo regional." />
        <meta property="og:image" content="https://raw.githubusercontent.com/garciadario1963-bit/cembu-lab/main/logo_cembu.png" />
        <meta property="og:type" content="website" />
    </head>
    """,
    unsafe_allow_html=True
)

# 2. INYECCIÓN DE ESTILOS CSS COMPLETOS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap');

/* Fondo general de la aplicación */
.stApp {
    background-color: #F8FAFC !important;
}

/* Ocultar padding por defecto de Streamlit arriba */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

/* Banner Superior Negro */
.top-black-banner {
    background-color: #0d0d0d !important;
    padding: 20px 40px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    border-bottom: 4px solid #C23B22 !important;
    margin-bottom: 20px !important;
    border-radius: 4px;
}

.logo-container {
    text-align: center;
    flex-grow: 1;
}

.brand-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 44px !important;
    font-weight: 900 !important;
    color: #E25822 !important;
    letter-spacing: 3px !important;
    margin: 0 !important;
    line-height: 1 !important;
}

.brand-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    color: #CCCCCC !important;
    font-weight: 500 !important;
    letter-spacing: 1px !important;
    margin-top: 6px !important;
}

.social-links {
    display: flex;
    gap: 15px;
    align-items: center;
}

.social-icon {
    color: #888888 !important;
    text-decoration: none !important;
    transition: color 0.3s ease;
}

.social-icon:hover {
    color: #E25822 !important;
}

/* Menú de Navegación */
.nav-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    background-color: #111111;
    padding: 12px;
    border-radius: 4px;
    margin-bottom: 30px;
}

.nav-link {
    color: #FFFFFF !important;
    text-decoration: none !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 6px 12px;
    border-bottom: 2px solid transparent;
}

.nav-link.active, .nav-link:hover {
    color: #E25822 !important;
    border-bottom: 2px solid #E25822 !important;
}

/* Tarjetas de los 3 Pilares */
.info-card {
    background: #FFFFFF !important;
    border-left: 5px solid #C23B22 !important;
    padding: 22px !important;
    border-radius: 6px !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.08) !important;
    min-height: 160px !important;
}

.card-number {
    font-family: 'Playfair Display', serif !important;
    font-size: 19px !important;
    font-weight: 800 !important;
    color: #C23B22 !important;
    margin-bottom: 8px !important;
}

.card-title {
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #0F172A !important;
    margin-bottom: 8px !important;
    line-height: 1.3 !important;
}

.card-desc {
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    color: #64748B !important;
    line-height: 1.4 !important;
}

/* Banners y Títulos de Secciones Inferiores */
.section-badge {
    background-color: #C23B22 !important;
    color: #FFFFFF !important;
    padding: 6px 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    display: inline-block !important;
    border-radius: 3px !important;
    margin-bottom: 12px !important;
}

.section-title-large {
    font-family: 'Playfair Display', serif !important;
    font-size: 24px !important;
    font-weight: 900 !important;
    color: #0F172A !important;
    margin-bottom: 8px !important;
    letter-spacing: 0.5px !important;
}

.section-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    color: #64748B !important;
}
</style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO NEGRO PRINCIPAL Y REDES SOCIALES
st.markdown("""
<div class="top-black-banner">
    <div style="width: 150px;"></div>
    <div class="logo-container">
        <h1 class="brand-title">CEMBU</h1>
        <div class="brand-subtitle">Conocimiento territorial para el desarrollo soberano</div>
    </div>
    <div class="social-links" style="width: 150px; justify-content: flex-end;">
        <a href="https://www.instagram.com/cembu_arg/" target="_blank" class="social-icon" title="Instagram">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <a href="https://x.com/cembu_arg" target="_blank" class="social-icon" title="X (Twitter)">
            <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
        <a href="https://www.linkedin.com/company/cembu-arg" target="_blank" class="social-icon" title="LinkedIn">
            <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        </a>
        <a href="https://facebook.com/cembu.arg" target="_blank" class="social-icon" title="Facebook">
            <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M9 8H6v4h3v12h5V12h3.642L18 8h-4V6.333C14 5.374 14.5 5 15.5 5H18V0h-3.808C10.592 0 9 1.583 9 4.615V8z"/></svg>
        </a>
        <a href="https://youtube.com/@cembu_arg" target="_blank" class="social-icon" title="YouTube">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
        <a href="mailto:contacto@cembu.com.ar" class="social-icon" title="Correo Electrónico">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M0 3v18h24v-18h-24zm21.518 2l-9.518 6.013-9.518-6.013h19.036zm-19.518 14v-11.817l10 6.32 10-6.32v11.817h-20z"/></svg>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. BARRA DE NAVEGACIÓN PRINCIPAL
st.markdown("""
<div class="nav-container">
    <a href="#" class="nav-link active">Tablero de Control</a>
    <a href="#" class="nav-link">CEMBU LAB</a>
    <a href="#" class="nav-link">CEMBU MATRIA</a>
    <a href="#" class="nav-link">CEMBU OHD</a>
    <a href="#" class="nav-link">Microdatos</a>
    <a href="mailto:contacto@cembu.com.ar" class="nav-link">Contacto</a>
</div>
""", unsafe_allow_html=True)

# 5. PILARES EN 3 COLUMNAS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="card-number">1. Decisión & Ejecución</div>
        <div class="card-title">Quienes deciden, crean y ejecutan las políticas públicas</div>
        <div class="card-desc">Ministerios, secretarías y organismos estatales.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="card-number">2. Análisis & Modelización</div>
        <div class="card-title">Quienes estudian las complejidades socioeconómicas</div>
        <div class="card-desc">Academias, centros de investigación e institutos.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="card-number">3. Transformación Real</div>
        <div class="card-title">Quienes protagonizan los avances sociales</div>
        <div class="card-desc">Actores territoriales, sindicatos y trabajadores.</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# 6. SECCIÓN INFERIOR
c_left, c_right = st.columns(2)

with c_left:
    st.markdown('<div class="section-badge">Novedades & Actividades</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-large">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Nuestras últimas actividades académicas y avances en análisis regional.</div>', unsafe_allow_html=True)

with c_right:
    st.markdown('<div class="section-badge">📍 Tablero de Control Territorial & Modelización</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle" style="font-weight: 600; color: #1E293B; margin-top: 10px;">📌 Monitor Territorial: Región Metropolitana / AMBA</div>', unsafe_allow_html=True)
