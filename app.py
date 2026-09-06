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

# LOGO: Podés reemplazar esta URL por un link a tu logo o tu imagen en base64 cuando gustes
LOGO_URL = "https://img.icons8.com/color/96/000000/open-book.png"

# 2. ESTILOS CSS PERSONALIZADOS
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
        padding: 20px 40px 14px 40px;
        text-align: center;
        border-bottom: 3px solid #EA580C;
        position: relative;
        width: 100%;
        box-sizing: border-box;
    }

    /* LOGO ESQUINA SUPERIOR IZQUIERDA */
    .logo-container {
        position: absolute;
        top: 18px;
        left: 40px;
        display: flex;
        align-items: center;
    }

    .logo-container img {
        height: 50px;
        width: auto;
        object-fit: contain;
    }

    /* REDES SOCIALES ESQUINA SUPERIOR DERECHA */
    .social-icons-container {
        position: absolute;
        top: 20px;
        right: 40px;
        display: flex;
        gap: 16px;
        align-items: center;
    }

    .social-icon {
        color: #94A3B8;
        font-size: 1rem;
        text-decoration: none;
        transition: color 0.2s ease;
    }

    .social-icon:hover {
        color: #EA580C;
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

    .tri-desc { font-size: 0.75rem; color: #64748B; margin-top: 4px; line-height: 1.3;
