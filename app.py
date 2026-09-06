import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILOS CSS
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
        padding: 24px 40px 14px 40px;
        text-align: center;
        border-bottom: 3px solid #EA580C;
    }

    .cembu-logo-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 900;
        color: #EA580C;
        letter-spacing: 2px;
        margin: 0 0 4px 0;
        line-height: 1;
    }

    .cembu-subtitle {
        font-size: 0.88rem;
        color: #CBD5E1;
        font-weight: 400;
        margin-bottom: 18px;
    }

    /* NAVEGACIÓN SUPERIOR */
    .top-nav-bar {
        display: flex;
        justify-content: center;
        gap: 32px;
        padding-top: 12px;
        border-top: 1px solid #1E293B;
    }

    .nav-item {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 600;
        text-decoration: none;
        cursor: pointer;
    }

    .nav-item.active {
        color: #EA580C;
        border-bottom: 2px solid #EA580C;
        padding-bottom: 4px;
    }

    /* CUERPO PRINCIPAL */
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

# 3. HEADER NEGRO SUPERIOR
st.markdown('''
<div class="top-black-banner">
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
''', unsafe_allow_html=True)

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

# B) Sección del Carrusel + Mapa
col_left, col_right = st.columns([1.1, 1], gap="small")

with col_left:
    st.markdown("""
        <div class="white-block" style="padding-bottom: 8px;">
            <span class="badge badge-red">NOVEDADES & ACTIVIDADES</span>
            <div class="block-title">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</div>
            <div class="block-sub" style="margin-bottom: 8px;">Nuestras últimas actividades académicas y avances en análisis regional.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # HTML + JS AUTOROTATIVO DEL CARRUSEL DE 2 IMÁGENES
    carrusel_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body { margin: 0; font-family: 'Inter', sans-serif; background: transparent; }
        .carousel-container {
            position: relative;
            width: 100%;
            height: 220px;
            overflow: hidden;
            border-radius: 6px;
        }
        .slide {
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }
        .slide.active {
            opacity: 1;
        }
        .slide img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .caption {
            position: absolute;
            bottom: 0;
            background: rgba(15, 23, 42, 0.85);
            color: #fff;
            width: 100%;
            padding: 8px 12px;
            font-size: 12px;
            box-sizing: border-box;
        }
        .dots-container {
            position: absolute;
            top: 10px;
            right: 12px;
            display: flex;
            gap: 6px;
            z-index: 10;
        }
        .dot {
            width: 10px;
            height: 10px;
            background-color: rgba(255,255,255,0.5);
            border-radius: 50%;
            display: inline-block;
            cursor: pointer;
        }
        .dot.active-dot {
            background-color: #EA580C;
        }
    </style>
    </head>
    <body>

    <div class="carousel-container">
        <div class="dots-container">
            <span class="dot active-dot" onclick="setSlide(0)"></span>
            <span class="dot" onclick="setSlide(1)"></span>
        </div>

        <!-- Slide 1: Evento CLACSO -->
        <div class="slide active">
            <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=700&auto=format&fit=crop&q=60" alt="CLACSO">
            <div class="caption"><b>1 / 2 — CLACSO EN LA FILUNI:</b> Participación institucional en México.</div>
        </div>

        <!-- Slide 2: Mapa / Cartografía -->
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

        // Rotación automática cada 3.5 segundos
        setInterval(nextSlide, 3500);
    </script>

    </body>
    </html>
    """
    components.html(carrusel_html, height=230)

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
    st.map(df_mapa, latitude='lat', longitude='lon', zoom=9, height=210)

st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

# C) Módulos inferiores
m1, m2, m3 = st.columns(3, gap="small")

with m1:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-red">CEMBU LAB</span>
            <div class="block-title">Modelos & Algoritmos</div>
            <div class="block-sub">Planificación del desarrollo mediante simulaciones de agentes y coyuntura.</div>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-teal">MATRIA</span>
            <div class="block-title">Unidades de Producción (UPS)</div>
            <div class="block-sub">Relevamiento territorial de encadenamientos productivos y matriz insumo-producto.</div>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="white-block">
            <span class="badge badge-purple">OHD MONETARIO</span>
            <div class="block-title">Tasas & Liquidez Global</div>
            <div class="block-sub">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores monetarios.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
