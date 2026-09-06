import streamlit as st
import pandas as pd

# 1. Configuración de página
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilos CSS personalizados
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #F8FAFC !important;
        font-family: 'Inter', sans-serif;
    }
    
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* BARRA NEGRA SUPERIOR */
    .top-black-banner {
        background-color: #0B0F19;
        color: #FFFFFF;
        padding: 24px 40px 0px 40px;
        text-align: center;
        position: relative;
        border-bottom: 3px solid #EA580C;
    }

    .cembu-logo-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 900;
        color: #EA580C; /* Naranja CEMBU */
        letter-spacing: 2px;
        margin: 0 0 4px 0;
        line-height: 1;
    }

    .cembu-subtitle {
        font-size: 0.9rem;
        color: #E2E8F0;
        font-weight: 400;
        margin-bottom: 20px;
    }

    .social-icons-top {
        position: absolute;
        top: 24px;
        right: 40px;
        display: flex;
        gap: 12px;
        color: #94A3B8;
    }

    /* MENÚ DE NAVEGACIÓN SUPERIOR */
    .top-nav-bar {
        display: flex;
        justify-content: center;
        gap: 28px;
        padding-top: 10px;
        padding-bottom: 14px;
        border-top: 1px solid #1E293B;
    }

    .nav-item {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 600;
        text-decoration: none;
        padding-bottom: 4px;
        transition: all 0.2s;
    }

    .nav-item.active {
        color: #EA580C;
        border-bottom: 2px solid #EA580C;
    }

    /* CUERPO Y GRILLAS */
    .content-container {
        padding: 24px 40px;
    }

    /* TARJETAS DEL TRIÁNGULO */
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

    /* BLOQUES BLANCOS */
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

    /* BADGES */
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

    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 3. HEADER NEGRO CON NAVEGACIÓN INTEGRADA ARRIBA
st.markdown("""
<div class="top-black-banner">
    <div class="social-icons-top">
        <span>📷</span> <span>𝕏</span> <span>in</span> <span>▶</span>
    </div>
    <div class="cembu-logo-title">CEMBU</div>
    <div class="cembu-subtitle">Generación de conocimiento, algoritmos y herramientas predictivas para la planificación del desarrollo soberano.</div>
    
    <div class="top-nav-bar">
        <span class="nav-item active">Tablero de Control</span>
        <span class="nav-item">CEMBU LAB</span>
        <span class="nav-item">CEMBU MATRIA</span>
        <span class="nav-item">CEMBU OHD</span>
        <span class="nav-item">Microdatos</span>
        <span class="nav-item">Institucional</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# A) Tres puntas del triángulo
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.markdown("""
        <div class="triangle-card card-a">
            <div class="tri-title-a">1. Decisión & Ejecución</div>
            <div class="tri-desc">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="triangle-card card-b">
            <div class="tri-title-b">2. Análisis & Modelización</div>
            <div class="tri-desc">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="triangle-card card-c">
            <div class="tri-title-c">3. Transformación Real</div>
            <div class="tri-desc">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

# B) Carrusel y Mapa
col_left, col_right = st.columns([1.1, 1], gap="small")

with col_left:
    st.markdown("""
        <div class="white-block">
            <div class="block-title">CLACSO EN LA FILUNI</div>
            <div class="block-sub">Feria Internacional del Libro de las Universitarias - UNAM México</div>
            <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=700&auto=format&fit=crop&q=60" style="width:100%; border-radius:6px; height:210px; object-fit:cover;">
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class="white-block">
            <div class="block-title">📍 Tablero de Control Territorial & Modelización</div>
            <div class="block-sub">📌 Monitor Territorial: Región Metropolitana / AMBA</div>
        </div>
    """, unsafe_allow_html=True)
    
    df_mapa = pd.DataFrame({
        'lat': [-34.6037, -34.6625, -34.5583, -34.7242, -34.9214],
        'lon': [-58.3816, -58.3647, -58.4622, -58.3800, -57.9545]
    })
    st.map(df_mapa, latitude='lat', longitude='lon', zoom=9, height=200)

st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

# C) Tarjetas inferiores de módulos
m1, m2, m3 = st.columns(3, gap="small")

with m1:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-red">CEMBU LAB</span>
            <div class="block-title">Modelos & Algoritmos</div>
            <div class="block-sub">Planificación del desarrollo mediante simulaciones de agentes.</div>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-teal">MATRIA</span>
            <div class="block-title">Unidades de Producción (UPS)</div>
            <div class="block-sub">Relevamiento territorial de encadenamientos productivos.</div>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-purple">OHD MONETARIO</span>
            <div class="block-title">Tasas & Liquidez Global</div>
            <div class="block-sub">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
