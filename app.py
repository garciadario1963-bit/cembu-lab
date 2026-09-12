import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium

# 1. Configuración de la página
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Multidisciplinarios",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS generales y de componentes
st.markdown("""
<style>
    /* Estilos base */
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Header/Banner principal compacto */
    .cembu-header {
        background-color: #0d1117;
        padding: 1.2rem 1.5rem 1rem 1.5rem;
        border-bottom: 3px solid #ff4b4b;
        margin-bottom: 1rem;
        border-radius: 4px;
        position: relative;
    }
    
    .header-content {
        text-align: center;
    }

    .cembu-title {
        color: #ff4b4b;
        font-family: 'Georgia', serif;
        font-size: 2.6rem;
        font-weight: bold;
        letter-spacing: 2px;
        margin: 0;
        line-height: 1.1;
    }

    .cembu-subtitle {
        color: #e6e6e6;
        font-size: 1rem;
        margin-top: 0.4rem;
        font-weight: 300;
    }

    /* Barra de redes sociales integrada en la esquina derecha del banner */
    .social-bar-header {
        position: absolute;
        top: 15px;
        right: 20px;
        display: flex;
        gap: 12px;
    }

    .social-icon-h {
        color: #8b949e;
        text-decoration: none;
        transition: color 0.2s ease;
    }

    .social-icon-h:hover {
        color: #ff4b4b;
    }

    /* Tarjetas del Triángulo */
    .triangulo-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 4px solid #1f77b4;
    }
    .triangulo-card-1 { border-left-color: #d62728; }
    .triangulo-card-2 { border-left-color: #1f77b4; }
    .triangulo-card-3 { border-left-color: #9467bd; }
    
    .triangulo-num {
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0.4rem;
    }
    .triangulo-desc {
        color: #555555;
        font-size: 0.9rem;
        line-height: 1.4;
    }

    /* Pie de página (Footer) */
    .cembu-footer {
        background-color: #0d1117;
        color: #c9d1d9;
        padding: 2rem 1.5rem 1.2rem 1.5rem;
        margin-top: 3rem;
        border-top: 3px solid #ff4b4b;
        font-family: system-ui, -apple-system, sans-serif;
    }
    .footer-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
        gap: 2rem;
    }
    .footer-col {
        flex: 1;
        min-width: 240px;
    }
    .footer-title {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 1.05rem;
        margin-bottom: 0.8rem;
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
    .footer-link {
        color: #25d366;
        text-decoration: none;
        font-weight: bold;
    }
    .footer-link:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# 2. Header compacto con redes integradas
st.markdown("""
<div class="cembu-header">
    <div class="social-bar-header">
        <a href="https://instagram.com" target="_blank" class="social-icon-h" title="Instagram">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <a href="https://x.com" target="_blank" class="social-icon-h" title="X (Twitter)">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
        <a href="https://linkedin.com" target="_blank" class="social-icon-h" title="LinkedIn">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        </a>
        <a href="https://facebook.com" target="_blank" class="social-icon-h" title="Facebook">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M9 8H6v4h3v12h5V12h3.642L18 8h-4V6.333C14 5.374 14.5 5 15.5 5H18V0h-3.808C10.592 0 9 1.847 9 5.052V8z"/></svg>
        </a>
        <a href="https://youtube.com" target="_blank" class="social-icon-h" title="YouTube">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 4-8 4z"/></svg>
        </a>
    </div>
    <div class="header-content">
        <div class="cembu-title">CEMBU</div>
        <div class="cembu-subtitle">Conocimiento territorial para el desarrollo soberano</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Navegación Principal
pestana = st.radio(
    "",
    ["Tablero de Control", "CEMBU LAB", "CEMBU MATRIA", "CEMBU OHD", "Microdatos", "Contacto"],
    horizontal=True,
    label_visibility="collapsed"
)

# ---------------------------------------------------------
# CONTENIDO DE LAS PESTAÑAS
# ---------------------------------------------------------

if pestana == "Tablero de Control":
    st.markdown("### ")
    
    # A) Las 3 tarjetas del Triángulo
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="triangulo-card triangulo-card-1">
            <div class="triangulo-num" style="color: #d62728;">1. Decisión & Ejecución</div>
            <div class="triangulo-desc">Quienes deciden, crean y ejecutan las políticas públicas: ministerios y secretarías.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="triangulo-card triangulo-card-2">
            <div class="triangulo-num" style="color: #1f77b4;">2. Análisis & Modelización</div>
            <div class="triangulo-desc">Quienes estudian las complejidades socioeconómicas: academias e institutos.</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="triangulo-card triangulo-card-3">
            <div class="triangulo-num" style="color: #9467bd;">3. Transformación Real</div>
            <div class="triangulo-desc">Quienes protagonizan los avances sociales: actores territoriales y trabajadores.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # B) Fila principal: Carrusel y Mapa Interactivo Folium
    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown("#### 📌 Novedades & Actividades")
        carrusel_html = """
        <div style="background:#ffffff; padding:15px; border-radius:8px; border:1px solid #ddd; height:380px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <span style="background:#d62728; color:white; padding:3px 8px; border-radius:4px; font-size:0.8rem; font-weight:bold;">NOVEDADES & ACTIVIDADES</span>
                <h3 style="margin-top:10px; font-family:Georgia, serif;">CLACSO EN LA FILUNI & MONITOR TERRITORIAL</h3>
                <p style="color:#666; font-size:0.9rem;">Nuestras últimas actividades académicas y avances en análisis regional.</p>
                <div style="background:#f8f9fa; height:180px; border-radius:6px; display:flex; align-items:center; justify-content:center; color:#888; border: 1px dashed #ccc;">
                    [ Carrusel de imágenes FILUNI / Monitor ]
                </div>
            </div>
            <div style="text-align:right;">
                <span style="color:#aaa; font-size:0.8rem;">● ○ ○</span>
            </div>
        </div>
        """
        components.html(carrusel_html, height=400)

    with col_right:
        st.markdown("#### 📍 Tablero de Control Territorial & Modelización")
        st.caption("Monitor Territorial: Región Metropolitana / AMBA")
        
        # Generar mapa Folium interactivo
        m = folium.Map(location=[-34.6037, -58.3816], zoom_start=10, tiles="CartoDB positron")
        folium.Marker(
            [-34.6037, -58.3816], 
            popup="Sede Central CABA", 
            tooltip="CEMBU AMBA",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
        
        st_folium(m, width="100%", height=360)

    st.markdown("---")

    # C) Módulos inferiores
    m1, m2, m3 = st.columns(3)
    with m1:
        st.subheader("🔬 CEMBU LAB")
        st.write("Laboratorio de innovación, datos y metodologías territoriales.")
    with m2:
        st.subheader("🌐 MATRIA")
        st.write("Observatorio de dinámicas productivas y desarrollo regional.")
    with m3:
        st.subheader("📈 OHD MONETARIO")
        st.write("Seguimiento y análisis de coyuntura macrofinanciera.")

elif pestana == "CEMBU LAB":
    st.title("🔬 CEMBU LAB")
    st.write("Sección en desarrollo: Laboratorio de Innovación y Métodos.")

elif pestana == "CEMBU MATRIA":
    st.title("🌐 CEMBU MATRIA")
    st.write("Sección en desarrollo: Observatorio de Desarrollo Territorial.")

elif pestana == "CEMBU OHD":
    st.title("📈 CEMBU OHD MONETARIO")
    st.write("Sección en desarrollo: Análisis Macroeconómico y Financiero.")

elif pestana == "Microdatos":
    st.title("📊 Microdatos")
    st.write("Sección en desarrollo: Repositorio de bases de datos y series.")

elif pestana == "Contacto":
    st.title("📬 Contacto CEMBU")
    st.markdown("""
    Podés comunicarte con nuestro equipo directamente a través de los siguientes medios:
    
    * **Correo Electrónico:** `contacto@cembu.org` *(podés seleccionar el texto y copiarlo)*
    * **WhatsApp / Teléfono:** `11-4993-8695`
    * **Ubicación:** CABA, Argentina
    """)
    st.markdown("[👉 Hacer clic aquí para enviar mensaje directo por WhatsApp](https://wa.me/5491149938695)", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. PIE DE PÁGINA (FOOTER) - VISIBLE EN TODO EL SITIO
# ---------------------------------------------------------
st.markdown("""
<div class="cembu-footer">
    <div class="footer-grid">
        <div class="footer-col">
            <div class="footer-title">CEMBU</div>
            <div style="font-size:0.9rem; color:#8b949e; line-height:1.5;">
                Centro de Estudios Multidisciplinarios.<br>
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
