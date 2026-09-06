import streamlit as st
import pandas as pd
import plotly.express as px
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
# 2. ESTILOS CSS AVANZADOS (DISEÑO HERO & TRIÁNGULO)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
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
    
    /* Hero Section Top */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-radius: 12px;
        padding: 24px 30px;
        color: #FFFFFF;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
        line-height: 1.15;
    }
    
    .hero-sub {
        font-size: 1.05rem;
        color: #94A3B8;
        font-weight: 400;
        margin-bottom: 0px;
    }
    
    /* Card del Triángulo Estratégico */
    .triangle-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #EA580C;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 25px;
    }
    
    .triangle-item {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .triangle-letter {
        font-weight: 800;
        font-size: 1.1rem;
        color: #EA580C;
        margin-bottom: 6px;
    }
    
    .triangle-desc {
        font-size: 0.9rem;
        color: #334155;
        line-height: 1.45;
    }

    /* Redes sociales en barra */
    .social-link {
        color: #FFFFFF !important;
        margin-left: 14px;
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
    
    # Redes Sociales Top Bar
    url_whatsapp = "https://wa.me/"
    url_x        = "https://x.com/"
    url_linkedin = "https://linkedin.com/"
    url_youtube  = "https://youtube.com/"
    
    # 1. ENCABEZADO DE MARCA & HERO
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #0F172A; color: #FFFFFF; padding: 12px 24px; border-radius: 10px; margin-bottom: 20px;">
            <div style="font-weight: 700; font-size: 0.95rem; letter-spacing: 0.5px;">
                🏛️ <strong>FAMILIA DE MARCAS CEMBU</strong> &nbsp;|&nbsp; Centro de Estudios Manuel Baldomero Ugarte
            </div>
            <div style="display: flex; align-items: center;">
                <a href="{url_whatsapp}" target="_blank" class="social-link" title="WhatsApp">
                    <svg width="20" height="20" fill="#25D366" viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984 0 1.758.459 3.474 1.33 4.982l-1.413 5.161 5.283-1.386a9.937 9.937 0 004.782 1.228h.005c5.507 0 9.991-4.479 9.991-9.986 0-2.668-1.038-5.176-2.925-7.063A9.927 9.927 0 0012.012 2z"/></svg>
                </a>
                <a href="{url_x}" target="_blank" class="social-link" title="X">
                    <svg width="18" height="18" fill="#FFFFFF" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="{url_linkedin}" target="_blank" class="social-link" title="LinkedIn">
                    <svg width="18" height="18" fill="#0A66C2" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.63 1.63 0 1 0 0 3.26 1.63 1.63 0 0 0 0-3.26z"/></svg>
                </a>
                <a href="{url_youtube}" target="_blank" class="social-link" title="YouTube">
                    <svg width="20" height="20" fill="#FF0000" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. SECCIÓN HERO (TÍTULO PRINCIPAL)
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Observatorio de Coyuntura, Modelización & Territorio</div>
            <div class="hero-sub">Generación de conocimiento, algoritmos y herramientas predictivas para la planificación del desarrollo soberano.</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. LAS TRES PUNTAS DEL TRIÁNGULO (ARTICULACIÓN ESTRATÉGICA)
    st.markdown("### 🔺 **Las tres puntas del triángulo**")
    st.caption("Marco conceptual de articulación para la gestión de políticas públicas y modelización territorial.")

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

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. TABLERO DE CONTROL DE IMPACTO (MAPA NATIVO + MODELIZACIÓN EN PARALELO)
    st.markdown("### 🛰️ **Tablero de Control Territorial & Modelización**")
    st.caption("Visor interactivo de indicadores socioeconómicos georeferenciados y trayectorias predictivas.")

    col_mapa, col_grafico = st.columns([1.2, 1], gap="medium")

    with col_mapa:
        st.markdown("**📌 Monitor Territorial: Región Metropolitana / AMBA**")
        
        # Datos geográficos del AMBA (Nodos territoriales y productivos)
        df_mapa = pd.DataFrame({
            'lat': [-34.6037, -34.6625, -34.5583, -34.7242, -34.9214, -34.6150, -34.4500, -34.7600],
            'lon': [-58.3816, -58.3647, -58.4622, -58.3800, -57.9545, -58.4333, -58.5500, -58.2100],
            'nodo': ['CABA Central', 'Avellaneda', 'General San Martín', 'Quilmes', 'La Plata', 'Mataderos (UPS)', 'Tigre', 'Berazategui']
        })

        # Visor de mapa nativo interactivo de Streamlit (Robusto y sin errores)
        st.map(df_mapa, latitude='lat', longitude='lon', zoom=9)

    with col_grafico:
        st.markdown("**📈 Curvas Epidémicas / Proyección de Modelos**")
        
        # Simulación de curvas socioeconómicas / epidemiológicas (Modelo SIR / Dinámico)
        df_model = pd.DataFrame({
            'Días': list(range(100)),
            'Afectados / Vulnerables': [0.1 * (x**1.5) * (1 - x/100) for x in range(100)],
            'Intervención / Cobertura': [100 / (1 + 2.71**(-0.1 * (x - 50))) for x in range(100)],
            'Población Objetivo': [100 - (100 / (1 + 2.71**(-0.1 * (x - 50)))) for x in range(100)]
        })

        fig_lines = go.Figure()
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Afectados / Vulnerables'], name='Afectados / Alerta', line=dict(color='#DC2626', width=2.5)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Intervención / Cobertura'], name='Intervención / Cobertura', line=dict(color='#16A34A', width=2.5)))
        fig_lines.add_trace(go.Scatter(x=df_model['Días'], y=df_model['Población Objetivo'], name='Población Objetivo', line=dict(color='#2563EB', width=2)))

        fig_lines.update_layout(
            margin={"r": 10, "t": 10, "l": 10, "b": 10},
            height=380,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(248,250,252,1)'
        )
        st.plotly_chart(fig_lines, use_container_width=True)

    st.divider()

    # 5. ACCESOS DIRECTOS A PUBLICACIONES & INFORMES
    col_inf1, col_inf2, col_inf3 = st.columns(3)
    
    with col_inf1:
        st.markdown("""
            <div style="background:#FFF; padding:16px; border-radius:8px; border:1px solid #E2E8F0;">
                <span style="background:#DC2626; color:#FFF; font-size:0.7rem; font-weight:700; padding:3px 8px; border-radius:4px;">CEMBU LAB</span>
                <h4 style="margin:8px 0 4px 0;">Modelos & Algoritmos</h4>
                <p style="font-size:0.85rem; color:#64748B;">Planificación del desarrollo mediante simulaciones de agentes y alta frecuencia.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Modelos LAB →", key="btn_lab", use_container_width=True)

    with col_inf2:
        st.markdown("""
            <div style="background:#FFF; padding:16px; border-radius:8px; border:1px solid #E2E8F0;">
                <span style="background:#0D9488; color:#FFF; font-size:0.7rem; font-weight:700; padding:3px 8px; border-radius:4px;">MATRIA</span>
                <h4 style="margin:8px 0 4px 0;">Unidades de Producción (UPS)</h4>
                <p style="font-size:0.85rem; color:#64748B;">Relevamiento territorial de encadenamientos productivos estratégicos.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Territorio →", key="btn_matria", use_container_width=True)

    with col_inf3:
        st.markdown("""
            <div style="background:#FFF; padding:16px; border-radius:8px; border:1px solid #E2E8F0;">
                <span style="background:#7C3AED; color:#FFF; font-size:0.7rem; font-weight:700; padding:3px 8px; border-radius:4px;">OHD MONETARIO</span>
                <h4 style="margin:8px 0 4px 0;">Tasas & Liquidez Global</h4>
                <p style="font-size:0.85rem; color:#64748B;">Seguimiento semanal de tasas Fed, BCE, BoJ e indicadores internacionales.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Ver Monitor OHD →", key="btn_ohd", use_container_width=True)

# Resto de secciones de navegación lateral
elif "📊 CEMBU LAB" in opcion_menu:
    st.title("📊 CEMBU LAB - Modelización & Algoritmos")
    st.info("Sección en desarrollo de modelos predictivos y algoritmos de simulación.")
elif "🗺️ CEMBU MATRIA" in opcion_menu:
    st.title("🗺️ CEMBU MATRIA - Unidades de Producción Soberana (UPS)")
    st.info("Relevamiento de encadenamientos productivos regionales.")
elif "📈 CEMBU OHD" in opcion_menu:
    st.title("📈 CEMBU OHD - Sistema Financiero e Indicadores")
    st.info("Monitoreo de política monetaria e indicadores de coyuntura.")
elif "📂 Base de Microdatos" in opcion_menu:
    st.title("📂 Base de Microdatos EPH / Censos")
    st.info("Acceso y consulta de microdatos socioeconómicos.")
elif "🏛️ Institucional" in opcion_menu:
    st.title("🏛️ Institucional & Equipo")
    st.info("Centro de Estudios Manuel Baldomero Ugarte.")
