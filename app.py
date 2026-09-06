import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Centro de Estudios Manuel Baldomero Ugarte",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. ESTILOS CSS INSPIRADOS EN CLACSO (HEADER NEGRO + NAVEGACIÓN SUPERIOR)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 96% !important;
    }

    .stApp {
        background-color: #FFFFFF !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Ocultar sidebar por defecto para usar header limpio */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Header Negro Superior */
    .top-bar {
        background-color: #0F172A;
        color: #FFFFFF;
        padding: 10px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid #EA580C;
        margin-bottom: 12px;
    }

    .top-logo-area {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .top-logo-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: 1px;
        color: #FFFFFF;
    }

    .social-icons-group {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .social-icons-group a {
        color: #94A3B8;
        transition: color 0.2s ease;
        display: flex;
        align-items: center;
    }

    .social-icons-group a:hover {
        color: #EA580C;
    }

    /* Tarjetas del Triángulo */
    .triangle-item {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #EA580C;
        border-radius: 6px;
        padding: 10px 14px;
        height: 100%;
    }

    .triangle-letter {
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 800;
        font-size: 0.95rem;
        color: #EA580C;
        margin-bottom: 2px;
    }

    .triangle-desc {
        font-size: 0.8rem;
        color: #334155;
        line-height: 1.35;
    }

    .section-label {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.15rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 14px;
        margin-bottom: 8px;
        border-bottom: 2px solid #F1F5F9;
        padding-bottom: 4px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. HEADER SUPERIOR ESTILO CLACSO
# -----------------------------------------------------------------------------
url_whatsapp = "https://wa.me/"
url_x        = "https://x.com/"
url_linkedin = "https://linkedin.com/"
url_youtube  = "https://youtube.com/"
url_instagram = "https://instagram.com/"
url_tiktok    = "https://tiktok.com/"

st.markdown(f"""
    <div class="top-bar">
        <div class="social-icons-group">
            <a href="{url_tiktok}" target="_blank" title="TikTok">
                <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12.525 0h3.08c.012.66.07 1.32.19 1.97.26 1.48 1.05 2.81 2.21 3.75 1.13.91 2.54 1.43 4 1.48v3.18c-1.46-.05-2.88-.47-4.13-1.21a8.68 8.68 0 0 1-1.35-.98v7.83c0 1.23-.27 2.44-.8 3.53a8.1 8.1 0 0 1-2.23 2.76A8.2 8.2 0 0 1 8.28 24a8.15 8.15 0 0 1-5.83-2.42A8.28 8.28 0 0 1 0 15.75c0-2.21.86-4.29 2.42-5.84A8.23 8.23 0 0 1 8.28 7.5c.34 0 .68.02 1.02.07v3.27a4.95 4.95 0 0 0-.96-.09 5.02 5.02 0 0 0-3.56 1.47 5.03 5.03 0 0 0-1.47 3.55c0 1.34.52 2.6 1.47 3.55A5.01 5.01 0 0 0 8.28 20.8c1.34 0 2.6-.52 3.55-1.47.95-.95 1.47-2.21 1.47-3.55V0h-.78z"/></svg>
            </a>
            <a href="{url_x}" target="_blank" title="X">
                <svg width="15" height="15" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
            <a href="{url_instagram}" target="_blank" title="Instagram">
                <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            </a>
            <a href="{url_youtube}" target="_blank" title="YouTube">
                <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
            <a href="{url_linkedin}" target="_blank" title="LinkedIn">
                <svg width="15" height="15" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/></svg>
            </a>
            <a href="{url_whatsapp}" target="_blank" title="WhatsApp">
                <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984 0 1.758.459 3.474 1.33 4.982l-1.413 5.161 5.283-1.386a9.937 9.937 0 004.782 1.228h.005c5.507 0 9.991-4.479 9.991-9.986 0-2.668-1.038-5.176-2.925-7.063A9.927 9.927 0 0012.012 2z"/></svg>
            </a>
        </div>
        <div class="top-logo-area">
            <span class="top-logo-title">CEMBU</span>
            <span style="font-size: 0.75rem; color: #94A3B8; border-left: 1px solid #334155; padding-left: 10px;">
                Centro de Estudios Manuel Baldomero Ugarte
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. MENÚ DE NAVEGACIÓN HORIZONTAL (ESPACIO BLANCO SUPERIOR)
# -----------------------------------------------------------------------------
opcion_menu = st.radio(
    "Navegación:",
    [
        "🌐 Portada",
        "📊 CEMBU LAB (Coyuntura)",
        "🗺️ CEMBU MATRIA (Territorio)",
        "📈 CEMBU OHD (Monetario & Int.)",
        "📂 Microdatos (EPH/Censo)",
        "🏛️ Institucional"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# -----------------------------------------------------------------------------
# 5. CONTENIDO PORTADA PRINCIPAL
# -----------------------------------------------------------------------------
if opcion_menu == "🌐 Portada":
    
    # SECCIÓN ROTADOR + NOTICIAS DESTACADAS
    col_rotador, col_fijas = st.columns([1.8, 1], gap="medium")

    with col_rotador:
        st.caption("📰 **Novedades & Publicaciones Destacadas**")
        
        tab1, tab2, tab3 = st.tabs([
            "📌 Jornadas JMAP 2026",
            "🇨🇳 Proyecto UPS & China",
            "🏦 Monitor de Bancos Centrales"
        ])
        
        with tab1:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); padding: 24px; border-radius: 8px; color: white;">
                    <span style="background: #EA580C; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">DESTACADO</span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-top: 10px; margin-bottom: 8px;">Jornadas de Modelización & Políticas Públicas (JMAP 2026)</h3>
                    <p style="font-size: 0.88rem; color: #CBD5E1;">Presentación de herramientas predictivas, algoritmos de simulación y modelos socioeconómicos orientados a la transformación territorial.</p>
                </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #065F46 0%, #047857 100%); padding: 24px; border-radius: 8px; color: white;">
                    <span style="background: #10B981; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">TERRITORIO</span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-top: 10px; margin-bottom: 8px;">Unidades de Producción Soberana (UPS)</h3>
                    <p style="font-size: 0.88rem; color: #D1FAE5;">Modelos de articulación territorial e integración de encadenamientos productivos inspirados en zonas de desarrollo internacional.</p>
                </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #312E81 0%, #4338CA 100%); padding: 24px; border-radius: 8px; color: white;">
                    <span style="background: #6366F1; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">MONETARIO</span>
                    <h3 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-top: 10px; margin-bottom: 8px;">Índice de Coordinación de Bancos Centrales (ICH)</h3>
                    <p style="font-size: 0.88rem; color: #E0E7FF;">Seguimiento sistemático semanal de las minutas, declaraciones y decisiones de la Fed, el BCE y el BoJ.</p>
                </div>
            """, unsafe_allow_html=True)

    with col_fijas:
        st.caption("🏛️ **Estructura del Centro**")
        st.markdown("""
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 6px; margin-bottom: 8px;">
                <h5 style="margin: 0; color: #0F172A; font-family: 'Playfair Display', serif;">Modelización & Algoritmos</h5>
                <p style="margin: 4px 0 0 0; font-size: 0.78rem; color: #64748B;">Simulación de agentes y escenarios macroeconómicos.</p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 6px; margin-bottom: 8px;">
                <h5 style="margin: 0; color: #0F172A; font-family: 'Playfair Display', serif;">Análisis Territorial & UPS</h5>
                <p style="margin: 4px 0 0 0; font-size: 0.78rem; color: #64748B;">Relevamiento de redes productivas locales.</p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 6px;">
                <h5 style="margin: 0; color: #0F172A; font-family: 'Playfair Display', serif;">Observatorio Monetario Global</h5>
                <p style="margin: 4px 0 0 0; font-size: 0.78rem; color: #64748B;">Indicadores de coyuntura y liquidez internacional.</p>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN LAS TRES PUNTAS DEL TRIÁNGULO
    st.markdown('<div class="section-label">🔺 Las tres puntas del triángulo de articulación</div>', unsafe_allow_html=True)

    col_t1, col_t2, col_t3 = st.columns(3)

    with col_t1:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">A. Decisión & Ejecución</div>
                <div class="triangle-desc"><strong>Quienes deciden y ejecutan políticas públicas:</strong> ministerios, secretarías nacionales, provinciales y gobiernos locales.</div>
            </div>
        """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">B. Análisis & Modelización</div>
                <div class="triangle-desc"><strong>Quienes estudian la complejidad socioeconómica:</strong> centros de estudios, universidades e institutos de investigación.</div>
            </div>
        """, unsafe_allow_html=True)

    with col_t3:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">C. Transformación Real</div>
                <div class="triangle-desc"><strong>Quienes dinamizan el territorio:</strong> actores comunitarios, trabajadores y sectores productivos.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN TABLERO TERRITORIAL Y MODELOS
    st.markdown('<div class="section-label">🛰️ Tablero Territorial & Proyección de Modelos</div>', unsafe_allow_html=True)

    col_mapa, col_grafico = st.columns([1.1, 1], gap="medium")

    with col_mapa:
        st.caption("📌 **Monitor Territorial: Región Metropolitana / AMBA**")
        df_mapa = pd.DataFrame({
            'lat': [-34.6037, -34.6625, -34.5583, -34.7242, -34.9214, -34.6150, -34.4500, -34.7600],
            'lon': [-58.3816, -58.3647, -58.4622, -58.3800, -57.9545, -58.4333, -58.5500, -58.2100],
            'nodo': ['CABA Central', 'Avellaneda', 'San Martín', 'Quilmes', 'La Plata', 'Mataderos (UPS)', 'Tigre', 'Berazategui']
        })
        st.map(df_mapa, latitude='lat', longitude='lon', zoom=9, height=280)

    with col_grafico:
        st.caption("📈 **Proyección de Indicadores & Modelos**")
        df_model = pd.DataFrame({
            'Días': list(range(100)),
            'Alerta / Vulnerabilidad': [0.1 * (x**1.5) * (1 - x/100) for x in range(100)],
            'Cobertura / Intervención': [100 / (1 + 2.71**(-0.1 * (x - 50))) for x in range(100)],
            'Meta Poblacional': [100 - (100 / (1 + 2.71**(-0.1 * (x - 50)))) for x in range(100)]
        })

        fig_lines = go.Figure()
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Alerta / Vulnerabilidad'], name='Alerta / Vulnerabilidad', line=dict(color='#DC2626', width=2)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Cobertura / Intervención'], name='Cobertura / Intervención', line=dict(color='#16A34A', width=2)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Meta Poblacional'], name='Meta Poblacional', line=dict(color='#2563EB', width=1.8)))

        fig_lines.update_layout(
            margin={"r": 5, "t": 5, "l": 5, "b": 5},
            height=280,
            legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1, font=dict(size=10)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(248,250,252,1)'
        )
        st.plotly_chart(fig_lines, use_container_width=True)

# Resto de vistas según navegación
elif opcion_menu == "📊 CEMBU LAB (Coyuntura)":
    st.title("📊 CEMBU LAB - Modelización & Algoritmos")
elif opcion_menu == "🗺️ CEMBU MATRIA (Territorio)":
    st.title("🗺️ CEMBU MATRIA - Unidades de Producción Soberana (UPS)")
elif opcion_menu == "📈 CEMBU OHD (Monetario & Int.)":
    st.title("📈 CEMBU OHD - Sistema Financiero & Tasas")
elif opcion_menu == "📂 Microdatos (EPH/Censo)":
    st.title("📂 Base de Microdatos EPH / Censo")
elif opcion_menu == "🏛️ Institucional":
    st.title("🏛️ Institucional & Autoridades")
