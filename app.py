import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CEMBU - Observatorio de Coyuntura, Modelización & Territorio",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. ESTILOS CSS CON TIPOGRAFÍA JMAP Y ESQUEMA DEL TRIÁNGULO
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,800;1,600&family=Inter:wght@400;600;700&display=swap');

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }

    .stApp {
        background-color: #F8FAFC !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Sidebar refinado */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    section[data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }
    
    /* Hero Banner con Diagrama Integrado */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-radius: 8px;
        padding: 16px 24px;
        color: #FFFFFF;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.18);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .hero-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.85rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.3px;
        margin-bottom: 4px;
        line-height: 1.15;
    }
    
    .hero-sub {
        font-size: 0.88rem;
        color: #94A3B8;
        font-weight: 400;
        margin-bottom: 0px;
        max-width: 650px;
    }
    
    /* Tarjetas del Triángulo */
    .triangle-item {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #EA580C;
        border-radius: 6px;
        padding: 8px 12px;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    
    .triangle-letter {
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 800;
        font-size: 0.95rem;
        color: #EA580C;
        margin-bottom: 2px;
    }
    
    .triangle-desc {
        font-size: 0.78rem;
        color: #334155;
        line-height: 1.3;
    }

    .section-label {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 1.1rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 6px;
        margin-bottom: 6px;
    }

    .social-link {
        color: #FFFFFF !important;
        margin-left: 12px;
        display: inline-flex;
        align-items: center;
        text-decoration: none !important;
        transition: opacity 0.2s ease;
    }
    .social-link:hover { opacity: 0.75; }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. NAVEGACIÓN LATERAL CON LOGO
# -----------------------------------------------------------------------------
with st.sidebar:
    posibles_logos = ["1_CEMBU.png", "logo_cembu.png", "logo.png", "logo_cembu.jpg"]
    logo_encontrado = None
    for nombre_logo in posibles_logos:
        if os.path.exists(nombre_logo):
            logo_encontrado = nombre_logo
            break

    if logo_encontrado:
        st.image(logo_encontrado, use_container_width=True)
    else:
        st.markdown("## 🏛️ **CEMBU**")
    
    st.markdown("### **Portal CEMBU**")
    st.caption("Conocimiento para la transformación social")
    
    opcion_menu = st.radio(
        "Navegación:",
        [
            "🌐 Tablero de Control & Territorio",
            "📊 CEMBU LAB (Coyuntura)",
            "🗺️ CEMBU MATRIA (Territorio)",
            "📈 CEMBU OHD (Monetario & Int.)",
            "📂 Base de Microdatos (EPH/Censo)",
            "🏛️ Institucional & Equipo"
        ]
    )
    st.divider()
    st.caption("📍 Buenos Aires, Argentina")


# -----------------------------------------------------------------------------
# 4. TABLERO PRINCIPAL / PORTADA
# -----------------------------------------------------------------------------
if "🌐 Tablero de Control" in opcion_menu or "📰 Portada" in opcion_menu:
    
    url_whatsapp = "https://wa.me/"
    url_x        = "https://x.com/"
    url_linkedin = "https://linkedin.com/"
    url_youtube  = "https://youtube.com/"
    
    # BARRA INSTITUCIONAL SUPERIOR
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #0F172A; color: #FFFFFF; padding: 6px 16px; border-radius: 6px; margin-bottom: 8px;">
            <div style="font-weight: 700; font-size: 0.82rem; letter-spacing: 0.4px;">
                🏛️ <strong>FAMILIA DE MARCAS CEMBU</strong> &nbsp;|&nbsp; Centro de Estudios Manuel Baldomero Ugarte
            </div>
            <div style="display: flex; align-items: center;">
                <a href="{url_whatsapp}" target="_blank" class="social-link" title="WhatsApp">
                    <svg width="16" height="16" fill="#25D366" viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984 0 1.758.459 3.474 1.33 4.982l-1.413 5.161 5.283-1.386a9.937 9.937 0 004.782 1.228h.005c5.507 0 9.991-4.479 9.991-9.986 0-2.668-1.038-5.176-2.925-7.063A9.927 9.927 0 0012.012 2z"/></svg>
                </a>
                <a href="{url_x}" target="_blank" class="social-link" title="X">
                    <svg width="15" height="15" fill="#FFFFFF" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="{url_linkedin}" target="_blank" class="social-link" title="LinkedIn">
                    <svg width="15" height="15" fill="#0A66C2" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/></svg>
                </a>
                <a href="{url_youtube}" target="_blank" class="social-link" title="YouTube">
                    <svg width="16" height="16" fill="#FF0000" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # BANNER HERO CON EL DIAGRAMA RENDERIZADO CORRECTAMENTE
    st.markdown("""
        <div class="hero-container">
            <div>
                <div class="hero-title">Observatorio de Coyuntura, Modelización & Territorio</div>
                <div class="hero-sub">Generación de conocimiento, algoritmos y herramientas predictivas para la planificación del desarrollo soberano.</div>
            </div>
            <div style="flex-shrink: 0; margin-left: 20px;">
                <svg width="180" height="100" viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <line x1="30" y1="25" x2="170" y2="25" stroke="#EA580C" stroke-width="2" stroke-dasharray="3 3"/>
                    <line x1="170" y1="25" x2="100" y2="100" stroke="#38BDF8" stroke-width="2"/>
                    <line x1="100" y1="100" x2="30" y2="25" stroke="#818CF8" stroke-width="2"/>
                    <circle cx="30" cy="25" r="9" fill="#EA580C" />
                    <text x="30" y="29" fill="#FFFFFF" font-size="10" font-weight="800" text-anchor="middle">A</text>
                    <text x="30" y="12" fill="#FDBA74" font-size="9" font-weight="700" text-anchor="middle">Decisión</text>
                    <circle cx="170" cy="25" r="9" fill="#0284C7" />
                    <text x="170" y="29" fill="#FFFFFF" font-size="10" font-weight="800" text-anchor="middle">B</text>
                    <text x="170" y="12" fill="#38BDF8" font-size="9" font-weight="700" text-anchor="middle">Análisis</text>
                    <circle cx="100" cy="100" r="9" fill="#6366F1" />
                    <text x="100" y="104" fill="#FFFFFF" font-size="10" font-weight="800" text-anchor="middle">C</text>
                    <text x="100" y="116" fill="#A5B4FC" font-size="9" font-weight="700" text-anchor="middle">Transformación</text>
                </svg>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # LAS TRES PUNTAS DEL TRIÁNGULO
    st.markdown('<div class="section-label">🔺 Las tres puntas del triángulo</div>', unsafe_allow_html=True)

    col_t1, col_t2, col_t3 = st.columns(3)

    with col_t1:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">A. Decisión & Ejecución</div>
                <div class="triangle-desc"><strong>Quienes deciden, crean y ejecutan las políticas públicas:</strong> ministros y secretarías nacionales, provinciales y municipales.</div>
            </div>
        """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">B. Análisis & Modelización</div>
                <div class="triangle-desc"><strong>Quienes estudian las complejidades socioeconómicas:</strong> Academias, universidades e institutos de investigación.</div>
            </div>
        """, unsafe_allow_html=True)

    with col_t3:
        st.markdown("""
            <div class="triangle-item">
                <div class="triangle-letter">C. Transformación Real</div>
                <div class="triangle-desc"><strong>Quienes protagonizan los avances sociales en lo real:</strong> actores territoriales, trabajadores y sectores productivos.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)

    # TABLERO DE CONTROL (MAPA + CURVAS)
    st.markdown('<div class="section-label">🛰️ Tablero de Control Territorial & Modelización</div>', unsafe_allow_html=True)

    col_mapa, col_grafico = st.columns([1.1, 1], gap="small")

    with col_mapa:
        st.caption("📌 **Monitor Territorial: Región Metropolitana / AMBA**")
        
        df_mapa = pd.DataFrame({
            'lat': [-34.6037, -34.6625, -34.5583, -34.7242, -34.9214, -34.6150, -34.4500, -34.7600],
            'lon': [-58.3816, -58.3647, -58.4622, -58.3800, -57.9545, -58.4333, -58.5500, -58.2100],
            'nodo': ['CABA Central', 'Avellaneda', 'General San Martín', 'Quilmes', 'La Plata', 'Mataderos (UPS)', 'Tigre', 'Berazategui']
        })

        st.map(df_mapa, latitude='lat', longitude='lon', zoom=9, height=270)

    with col_grafico:
        st.caption("📈 **Curvas Epidémicas / Proyección de Modelos**")
        
        df_model = pd.DataFrame({
            'Días': list(range(100)),
            'Afectados / Vulnerables': [0.1 * (x**1.5) * (1 - x/100) for x in range(100)],
            'Intervención / Cobertura': [100 / (1 + 2.71**(-0.1 * (x - 50))) for x in range(100)],
            'Población Objetivo': [100 - (100 / (1 + 2.71**(-0.1 * (x - 50)))) for x in range(100)]
        })

        fig_lines = go.Figure()
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Afectados / Vulnerables'], name='Afectados / Alerta', line=dict(color='#DC2626', width=2)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Intervención / Cobertura'], name='Intervención / Cobertura', line=dict(color='#16A34A', width=2)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Población Objetivo'], name='Población Objetivo', line=dict(color='#2563EB', width=1.8)))

        fig_lines.update_layout(
            margin={"r": 5, "t": 5, "l": 5, "b": 5},
            height=270,
            legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1, font=dict(size=10)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(248,250,252,1)'
        )
        st.plotly_chart(fig_lines, use_container_width=True)

    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

    # ACCESOS DIRECTOS DE SECCIONES
    col_inf1, col_inf2, col_inf3 = st.columns(3)
    
    with col_inf1:
        st.markdown("""
            <div style="background:#FFF; padding:12px; border-radius:6px; border:1px solid #E2E8F0;">
                <span style="background:#DC2626; color:#FFF; font-size:0.68rem; font-weight:700; padding:2px 6px; border-radius:3px;">CEMBU LAB</span>
                <h4 style="margin:6px 0 2px 0; font-size: 0.95rem; font-family:'Playfair Display', serif;">Modelos & Algoritmos</h4>
                <p style="font-size:0.78rem; color:#64748B; margin-bottom: 0;">Planificación del desarrollo mediante simulaciones de agentes.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Modelos LAB →", key="btn_lab", use_container_width=True)

    with col_inf2:
        st.markdown("""
            <div style="background:#FFF; padding:12px; border-radius:6px; border:1px solid #E2E8F0;">
                <span style="background:#0D9488; color:#FFF; font-size:0.68rem; font-weight:700; padding:2px 6px; border-radius:3px;">MATRIA</span>
                <h4 style="margin:6px 0 2px 0; font-size: 0.95rem; font-family:'Playfair Display', serif;">Unidades de Producción (UPS)</h4>
                <p style="font-size:0.78rem; color:#64748B; margin-bottom: 0;">Relevamiento territorial de encadenamientos productivos.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Territorio →", key="btn_matria", use_container_width=True)

    with col_inf3:
        st.markdown("""
            <div style="background:#FFF; padding:12px; border-radius:6px; border:1px solid #E2E8F0;">
                <span style="background:#7C3AED; color:#FFF; font-size:0.68rem; font-weight:700; padding:2px 6px; border-radius:3px;">OHD MONETARIO</span>
                <h4 style="margin:6px 0 2px 0; font-size: 0.95rem; font-family:'Playfair Display', serif;">Tasas & Liquidez Global</h4>
                <p style="font-size:0.78rem; color:#64748B; margin-bottom: 0;">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Monitor OHD →", key="btn_ohd", use_container_width=True)

# Resto de secciones
elif "📊 CEMBU LAB" in opcion_menu:
    st.title("📊 CEMBU LAB - Modelización & Algoritmos")
elif "🗺️ CEMBU MATRIA" in opcion_menu:
    st.title("🗺️ CEMBU MATRIA - Unidades de Producción Soberana")
elif "📈 CEMBU OHD" in opcion_menu:
    st.title("📈 CEMBU OHD - Sistema Financiero e Indicadores")
elif "📂 Base de Microdatos" in opcion_menu:
    st.title("📂 Base de Microdatos EPH / Censos")
elif "🏛️ Institucional" in opcion_menu:
    st.title("🏛️ Institucional & Equipo")
