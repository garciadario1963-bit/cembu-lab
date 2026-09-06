import streamlit as st
import pandas as pd
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,800;1,600&family=Inter:wght@400;600;700&display=swap');

    /* Fondo general gris claro */
    .stApp {
        background-color: #F1F5F9 !important;
        font-family: 'Inter', sans-serif;
    }
    
    .block-container {
        padding: 0 !important; /* Eliminamos padding para header full-width */
        max-width: 100% !important;
    }

    /* ---------------- HEADER NEGRO SUPERIOR (FULL WIDTH) ---------------- */
    .top-header-black {
        background-color: #0F172A;
        color: #FFFFFF;
        padding: 10px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #EA580C;
    }

    .header-left-group {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .banner-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.5rem;
        font-weight: 800;
        color: #FFFFFF;
        margin: 0;
        line-height: 1.2;
    }

    .header-logo-container {
        background-color: #FFFFFF;
        padding: 8px;
        border-radius: 4px;
        display: flex;
        align-items: center;
    }

    .banner-sub {
        font-size: 0.75rem;
        color: #94A3B8;
        max-width: 500px;
        margin-top: 2px;
    }

    .social-icons {
        display: flex;
        gap: 10px;
        align-items: center;
    }

    .header-triangle-svg {
        height: 60px;
        width: 100px;
    }

    /* ---------------- CONTENEDOR LATERAL BLANCO ---------------- */
    .left-nav-col {
        background-color: #FFFFFF;
        border-radius: 0 8px 8px 0;
        padding: 20px;
        box-shadow: 2px 0 6px rgba(0,0,0,0.03);
        height: calc(100vh - 82px); /* Altura restante tras el header */
        overflow-y: auto;
    }

    .nav-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 4px;
    }

    .nav-sub {
        font-size: 0.78rem;
        color: #64748B;
        margin-bottom: 16px;
    }

    /* ---------------- CONTENEDOR DE CONTENIDO DERECHO ---------------- */
    .main-content-col {
        padding: 20px 40px 20px 20px !important;
    }

    /* ---------------- TRES PUNTAS DEL TRIÁNGULO ---------------- */
    .triangle-card {
        background-color: #FFFFFF;
        border-left: 4px solid #EA580C;
        border-radius: 4px;
        padding: 8px 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        height: 100%;
    }

    .triangle-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 700;
        font-size: 0.88rem;
        color: #EA580C;
        margin-bottom: 2px;
    }

    .triangle-text {
        font-size: 0.73rem;
        color: #475569;
        line-height: 1.25;
    }

    /* ---------------- CONTENEDORES BLANCOS DE CONTENIDO ---------------- */
    .white-card-block {
        background-color: #FFFFFF !important;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .section-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.05rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 4px;
    }

    .section-subtitle {
        font-size: 0.78rem;
        color: #64748B;
        margin-bottom: 10px;
    }

    /* Ocultar elementos nativos */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none;} /* Oculta navegación nativa si existe */
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. HEADER NEGRO SUPERIOR (FULL WIDTH)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="top-header-black">
    <div class="header-left-group">
        <div class="header-logo-container">
            <h1 style="font-family:'Playfair Display', serif; color:#DC2626; margin:0; font-size:1.8rem; font-weight:800; line-height:1;">CEMBU</h1>
        </div>
        <div>
            <div class="banner-title">Coyuntura, Modelización & Territorio</div>
            <div class="banner-sub">Generación de conocimiento, algoritmos y herramientas predictivas para la planificación del desarrollo soberano.</div>
        </div>
    </div>
    <div style="display: flex; align-items: center; gap: 20px;">
        <div class="social-icons">
            <a href="#" style="color:#FFFFFF;"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98 1.281-.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a>
            <a href="#" style="color:#FFFFFF;"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
            <a href="#" style="color:#FFFFFF;"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/></svg></a>
            <a href="#" style="color:#FFFFFF;"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984 0 1.758.459 3.474 1.33 4.982l-1.413 5.161 5.283-1.386a9.937 9.937 0 004.782 1.228h.005c5.507 0 9.991-4.479 9.991-9.986 0-2.668-1.038-5.176-2.925-7.063A9.927 9.927 0 0012.012 2z"/></svg></a>
        </div>
        <svg class="header-triangle-svg" viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
            <line x1="30" y1="25" x2="170" y2="25" stroke="#EA580C" stroke-width="2" stroke-dasharray="3 3"/>
            <line x1="170" y1="25" x2="100" y2="100" stroke="#38BDF8" stroke-width="2"/>
            <line x1="100" y1="100" x2="30" y2="25" stroke="#818CF8" stroke-width="2"/>
            <circle cx="30" cy="25" r="9" fill="#EA580C" />
            <circle cx="170" cy="25" r="9" fill="#0284C7" />
            <circle cx="100" cy="100" r="9" fill="#6366F1" />
        </svg>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. CUERPO PRINCIPAL (LATERAL IZQUIERDO BLANCO + CONTENIDO DERECHO)
# -----------------------------------------------------------------------------
col_nav, col_main = st.columns([1.2, 4.8], gap="small")

# --- COLUMNA LATERAL IZQUIERDA BLANCA ---
with col_nav:
    st.markdown("""
        <div class="left-nav-col">
            <div class="nav-title">Portal CEMBU</div>
            <div class="nav-sub">Conocimiento para la transformación social<br><i>Cembu.org.ar</i></div>
            <hr style="border-color:#E2E8F0; margin-bottom:12px;">
            <div style="font-size:0.82rem; font-weight:700; color:#0F172A; margin-bottom:8px;">Navegación principal:</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Integramos el control de radio dentro del estilo lateral blanco
    with st.container():
        seccion = st.radio(
            label="Navegación principal",
            options=[
                "🔴 Tablero de Control & Territorio",
                "⚪ CEMBU LAB (Coyuntura)",
                "⚪ CEMBU MATRIA (Territorio)",
                "⚪ CEMBU OHD (Monetario & Int.)",
                "⚪ Base de Microdatos (EPH/Censo)",
                "⚪ Institucional & Equipo"
            ],
            label_visibility="collapsed"
        )

# --- COLUMNA DE CONTENIDO DERECHO ---
with col_main:
    # Usamos un container para aplicar padding derecho general
    with st.container():
        
        # 1. TRES PUNTAS DEL TRIÁNGULO
        col_a, col_b, col_c = st.columns(3, gap="small")
        with col_a:
            st.markdown("""
                <div class="triangle-card">
                    <div class="triangle-title">A. Decisión & Ejecución</div>
                    <div class="triangle-text">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
                <div class="triangle-card">
                    <div class="triangle-title">B. Análisis & Modelización</div>
                    <div class="triangle-text">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div>
                </div>
            """, unsafe_allow_html=True)
        with col_c:
            st.markdown("""
                <div class="triangle-card">
                    <div class="triangle-title">C. Transformación Real</div>
                    <div class="triangle-text">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

        # 2. CARRUSEL + MAPA
        col_carrusel, col_mapa_box = st.columns([1.1, 1], gap="small")

        with col_carrusel:
            # Reemplazar con st.image o carrusel según prefieras
            st.markdown("""
                <div class="white-card-block">
                    <div class="section-title">CLACSO EN LA FILUNI</div>
                    <div class="section-subtitle">Feria Internacional del Libro de las Universitarias - UNAM México</div>
                    <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&auto=format&fit=crop&q=60" style="width:100%; border-radius:6px; height:200px; object-fit:cover;">
                </div>
            """, unsafe_allow_html=True)

        with col_mapa_box:
            st.markdown("""
                <div class="white-card-block">
                    <div class="section-title">📍 Tablero de Control Territorial & Modelización</div>
                    <div class="section-subtitle">📌 Monitor Territorial: Región Metropolitana / AMBA</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Mapa embebido dentro del espacio del contenedor blanco
            df_mapa = pd.DataFrame({
                'lat': [-34.6037, -34.6625, -34.5583, -34.7242, -34.9214],
                'lon': [-58.3816, -58.3647, -58.4622, -58.3800, -57.9545]
            })
            st.map(df_mapa, latitude='lat', longitude='lon', zoom=9, height=190)

        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

        # 3. MÓDULOS DE ACCESO DIRECTO INFERIORES
        col_m1, col_m2, col_m3 = st.columns(3, gap="small")
        
        with col_m1:
            st.markdown("""
                <div class="white-card-block">
                    <span style="background:#DC2626; color:#FFF; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px;">CEMBU LAB</span>
                    <div class="section-title" style="margin-top:6px;">Modelos & Algoritmos</div>
                    <p style="font-size:0.75rem; color:#64748B;">Planificación del desarrollo mediante simulaciones de agentes.</p>
                </div>
            """, unsafe_allow_html=True)

        with col_m2:
            st.markdown("""
                <div class="white-card-block">
                    <span style="background:#0D9488; color:#FFF; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px;">MATRIA</span>
                    <div class="section-title" style="margin-top:6px;">Unidades de Producción (UPS)</div>
                    <p style="font-size:0.75rem; color:#64748B;">Relevamiento territorial de encadenamientos productivos.</p>
                </div>
            """, unsafe_allow_html=True)

        with col_m3:
            st.markdown("""
                <div class="white-card-block">
                    <span style="background:#7C3AED; color:#FFF; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px;">OHD MONETARIO</span>
                    <div class="section-title" style="margin-top:6px;">Tasas & Liquidez Global</div>
                    <p style="font-size:0.75rem; color:#64748B;">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores.</p>
                </div>
            """, unsafe_allow_html=True)
