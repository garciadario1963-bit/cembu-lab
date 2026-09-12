import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium
import os

# ---------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="assets/1_CEMBU.png" if os.path.exists("assets/1_CEMBU.png") else "🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. ESTILOS CSS PERSONALIZADOS (Estética Código 1 + 3)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #F8FAFC !important;
        font-family: 'Inter', sans-serif;
    }
    
    .block-container {
        padding: 0 1rem 2rem 1rem !important;
        max-width: 95% !important;
    }

    /* BARRA NEGRA SUPERIOR DE ALTA ESTÉTICA */
    .top-black-banner {
        background-color: #0B0F19;
        color: #FFFFFF;
        padding: 24px 40px 18px 40px;
        text-align: center;
        border-bottom: 4px solid #EA580C;
        position: relative;
        width: 100%;
        border-radius: 0 0 8px 8px;
        box-sizing: border-box;
        margin-bottom: 15px;
    }

    /* CONTENEDOR DEL LOGO PRINCIPAL */
    .logo-container {
        position: absolute;
        top: 16px;
        left: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #FFFFFF;
        padding: 6px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(255,255,255,0.15);
    }

    /* REDES SOCIALES ESQUINA SUPERIOR DERECHA */
    .social-icons-container {
        position: absolute;
        top: 22px;
        right: 35px;
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

    .social-icon-svg {
        width: 18px;
        height: 18px;
        fill: currentColor;
    }

    .cembu-logo-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 900;
        color: #EA580C;
        letter-spacing: 2px;
        margin: 0 0 2px 0;
        line-height: 1;
    }

    .cembu-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        color: #CBD5E1;
        font-weight: 500;
        letter-spacing: 0.3px;
    }

    /* MENÚ HORIZONTAL RADIO CUSTOM */
    div[data-testid="stRadio"] > div {
        display: flex;
        justify-content: center;
        gap: 15px;
        background-color: #0B0F19;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    div[data-testid="stRadio"] label {
        color: #94A3B8 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        cursor: pointer;
    }

    /* TARJETAS DE PILARES Y MÓDULOS */
    .triangle-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        height: 100%;
        border-left: 4px solid #EA580C;
    }
    .card-a { border-left-color: #EA580C; }
    .card-b { border-left-color: #0284C7; }
    .card-c { border-left-color: #4F46E5; }

    .tri-title-a { font-family: 'Playfair Display', serif; color: #EA580C; font-weight: 700; font-size: 1.05rem; }
    .tri-title-b { font-family: 'Playfair Display', serif; color: #0284C7; font-weight: 700; font-size: 1.05rem; }
    .tri-title-c { font-family: 'Playfair Display', serif; color: #4F46E5; font-weight: 700; font-size: 1.05rem; }

    .tri-desc { font-size: 0.82rem; color: #64748B; margin-top: 6px; line-height: 1.4; }

    .white-block {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        height: 100%;
    }

    .block-title {
        font-family: 'Playfair Display', serif;
        font-weight: 800;
        font-size: 1.15rem;
        color: #0F172A;
    }

    .block-sub {
        font-size: 0.8rem;
        color: #64748B;
        margin-top: 4px;
        margin-bottom: 10px;
    }

    .badge {
        font-size: 0.65rem;
        font-weight: 700;
        color: #FFF;
        padding: 3px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 8px;
    }
    .badge-red { background-color: #DC2626; }
    .badge-teal { background-color: #0D9488; }
    .badge-purple { background-color: #7C3AED; }

    /* PIE DE PÁGINA (FOOTER INTEGRADOR) */
    .cembu-footer {
        background-color: #0B0F19;
        color: #CBD5E1;
        padding: 2.2rem 2rem 1.2rem 2rem;
        margin-top: 3rem;
        border-top: 4px solid #EA580C;
        border-radius: 8px 8px 0 0;
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
    .footer-title { color: #EA580C; font-weight: 800; font-size: 1.1rem; margin-bottom: 0.8rem; font-family: 'Playfair Display', serif; }
    .footer-item { margin-bottom: 0.6rem; font-size: 0.88rem; display: flex; align-items: center; gap: 0.5rem; }
    .footer-copy-box {
        background-color: #1E293B; border: 1px solid #334155; color: #38BDF8; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace;
    }
    .footer-bottom { text-align: center; border-top: 1px solid #1E293B; margin-top: 1.8rem; padding-top: 0.8rem; font-size: 0.8rem; color: #64748B; }
    .footer-link { color: #22C55E; text-decoration: none; font-weight: 600; }
    .footer-link:hover { text-decoration: underline; }

    /* Ocultar elementos nativos */
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. BANNER NEGRO SUPERIOR (Con Logo del Código 3 + SVG Fallback)
# ---------------------------------------------------------
logo_path_header = "assets/1_CEMBU.png"
if os.path.exists(logo_path_header):
    logo_html = f'<div class="logo-container"><img src="data:image/png;base64,{st.image(logo_path_header)}" width="60"/></div>'
    # Método alternativo estándar si no renderiza base64 en markdown puro:
    logo_component = f'<div class="logo-container"><img src="file/{logo_path_header}" width="60" style="border-radius:6px;"/></div>'
else:
    logo_component = """
    <div class="logo-container" style="background:transparent; padding:0;">
        <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M15 28C15 28 32 23 47 33V80C32 70 15 75 15 75V28Z" fill="#EA580C"/>
          <path d="M85 28C85 28 68 23 53 33V80C68 70 85 75 85 75V28Z" fill="#DC2626"/>
          <path d="M47 33C32 25 18 29 18 29V33C18 33 32 29 47 37V33Z" fill="#FFFFFF" opacity="0.9"/>
          <path d="M53 33C68 25 82 29 82 29V33C82 33 68 29 53 37V33Z" fill="#FFFFFF" opacity="0.9"/>
          <path d="M47 33V80C49 81 51 81 53 80V33C51 34 49 34 47 33Z" fill="#C2410C"/>
        </svg>
    </div>
    """

st.markdown(f"""
<div class="top-black-banner">
    {logo_component}
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

# ---------------------------------------------------------
# 4. MENÚ DE NAVEGACIÓN HORIZONTAL (Código 2)
# ---------------------------------------------------------
menu_opcion = st.radio(
    "",
    ["Tablero de Control", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True,
    label_visibility="collapsed"
)

# ---------------------------------------------------------
# 5. CONTENIDO DE LAS SECCIONES / PESTAÑAS
# ---------------------------------------------------------

if menu_opcion == "Tablero de Control":

    # A) Las 3 Tarjetas de Pilares
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.markdown('<div class="triangle-card card-a"><div class="tri-title-a">1. Decisión & Ejecución</div><div class="tri-desc">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="triangle-card card-b"><div class="tri-title-b">2. Análisis & Modelización</div><div class="tri-desc">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="triangle-card card-c"><div class="tri-title-c">3. Transformación Real</div><div class="tri-desc">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    # B) Carrusel Interactivo HTML + Mapa Folium Interactivo
    col_left, col_right = st.columns([1.1, 1], gap="medium")

    with col_left:
        st.markdown('<div class="white-block" style="padding-bottom: 8px;"><span class="badge badge-red">NOVEDADES & ACTIVIDADES</span><div class="block-title">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</div><div class="block-sub">Nuestras últimas actividades académicas y avances en análisis regional.</div></div>', unsafe_allow_html=True)
        
        carrusel_html = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body { margin: 0; font-family: 'Inter', sans-serif; background: transparent; }
            .carousel-container { position: relative; width: 100%; height: 260px; overflow: hidden; border-radius: 8px; }
            .slide { position: absolute; width: 100%; height: 100%; opacity: 0; transition: opacity 0.8s ease-in-out; }
            .slide.active { opacity: 1; }
            .slide img { width: 100%; height: 100%; object-fit: cover; }
            .caption { position: absolute; bottom: 0; background: rgba(11, 15, 25, 0.88); color: #fff; width: 100%; padding: 10px 14px; font-size: 13px; box-sizing: border-box; }
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
            setInterval(nextSlide, 4000);
        </script>
        </body>
        </html>
        """
        components.html(carrusel_html, height=270)

    with col_right:
        st.markdown('<div class="white-block" style="padding-bottom: 10px;"><div class="block-title">📍 Tablero de Control Territorial</div><div class="block-sub">Monitor Territorial: Región Metropolitana / AMBA</div></div>', unsafe_allow_html=True)
        
        m = folium.Map(location=[-34.6037, -58.3816], zoom_start=10, tiles="CartoDB positron")
        folium.Marker(
            [-34.6037, -58.3816], 
            popup="Sede Central CABA", 
            tooltip="CEMBU AMBA",
            icon=folium.Icon(color="orange", icon="info-sign")
        ).add_to(m)
        st_folium(m, width="100%", height=240)

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    # C) Módulos Inferiores con Logos Integrados (Código 3)
    m1, m2, m3 = st.columns(3, gap="small")

    with m1:
        st.markdown('<div class="white-block">', unsafe_allow_html=True)
        if os.path.exists("assets/CEMBU_LAB_logo.png"):
            st.image("assets/CEMBU_LAB_logo.png", width=70)
        else:
            st.markdown('<span class="badge badge-red">CEMBU LAB</span>', unsafe_allow_html=True)
        st.markdown('<div class="block-title">CEMBU LAB - Modelos & Algoritmos</div><div class="block-sub">Planificación del desarrollo mediante simulaciones de agentes y coyuntura.</div></div>', unsafe_allow_html=True)

    with m2:
        st.markdown('<div class="white-block">', unsafe_allow_html=True)
        if os.path.exists("assets/2_MATRIA.png"):
            st.image("assets/2_MATRIA.png", width=70)
        else:
            st.markdown('<span class="badge badge-teal">MATRIA</span>', unsafe_allow_html=True)
        st.markdown('<div class="block-title">MATRIA - Unidades de Producción (UPS)</div><div class="block-sub">Relevamiento territorial de encadenamientos productivos y matriz insumo-producto.</div></div>', unsafe_allow_html=True)

    with m3:
        st.markdown('<div class="white-block">', unsafe_allow_html=True)
        if os.path.exists("assets/3_OHD.png"):
            st.image("assets/3_OHD.png", width=70)
        else:
            st.markdown('<span class="badge badge-purple">OHD MONETARIO</span>', unsafe_allow_html=True)
        st.markdown('<div class="block-title">OHD MONETARIO - Tasas & Liquidez</div><div class="block-sub">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores monetarios.</div></div>', unsafe_allow_html=True)

elif menu_opcion == "CEMBU LAB":
    st.title("🔬 CEMBU LAB")
    if os.path.exists("assets/CEMBU_LAB_logo.png"):
        st.image("assets/CEMBU_LAB_logo.png", width=120)
    st.write("Laboratorio de innovación, datos y metodologías territoriales.")

elif menu_opcion == "CEMBU MATRIA":
    st.title("🌐 CEMBU MATRIA")
    if os.path.exists("assets/2_MATRIA.png"):
        st.image("assets/2_MATRIA.png", width=120)
    st.write("Observatorio de dinámicas productivas y desarrollo regional. Empresas sociales — Clusters, ZEE 360, Fondo de Hábitat.")

elif menu_opcion == "CEMBU OHD":
    st.title("📈 CEMBU OHD MONETARIO")
    if os.path.exists("assets/3_OHD.png"):
        st.image("assets/3_OHD.png", width=120)
    st.write("Observatorio monetario — Hegemonía del dólar y coyuntura macrofinanciera global.")

elif menu_opcion == "Microdatos":
    st.title("📊 Microdatos")
    st.write("Repositorio de bases de datos, microdatos e indicadores normalizados.")

elif menu_opcion == "Contacto":
    st.title("📬 Contacto Directo CEMBU")
    st.markdown("""
    Podés comunicarte con nuestro equipo directamente a través de los siguientes canales:
    
    * **Correo Electrónico:** `contacto@cembu.org`
    * **WhatsApp / Teléfono:** `11-4993-8695`
    * **Ubicación:** Ciudad Autónoma de Buenos Aires (CABA), Argentina
    """)
    st.markdown("""
    <a href="https://wa.me/5491149938695" target="_blank" style="background-color: #22C55E; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 10px;">
        💬 Enviar mensaje directo por WhatsApp
    </a>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. PIE DE PÁGINA FOOTER (Código 2 + 3 Integrado)
# ---------------------------------------------------------
st.markdown("""
<div class="cembu-footer">
    <div class="footer-grid">
        <div class="footer-col">
            <div class="footer-title">CEMBU</div>
            <div style="font-size:0.88rem; color:#94A3B8; line-height:1.5;">
                Centro de Estudios Multidisciplinarios Manuel Baldomero Ugarte.<br>
                Conocimiento territorial para el desarrollo soberano.
            </div>
        </div>
        <div class="footer-col">
            <div class="footer-title">Contacto Directo</div>
            <div class="footer-item">
                📧 <b>Email:</b> <span class="footer-copy-box">contacto@cembu.org</span>
            </div>
            <div class="footer-item">
                📱 <b>WhatsApp:</b> 
                <a href="https://wa.me/5491149938695" target="_blank" class="footer-link">
                    11-4993-8695
                </a>
            </div>
        </div>
        <div class="footer-col">
            <div class="footer-title">Ubicación</div>
            <div class="footer-item">
                📍 Ciudad Autónoma de Buenos Aires (CABA), Argentina
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        © CEMBU - Todos los derechos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
