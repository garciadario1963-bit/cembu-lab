    /* ---------- BARRA DE NAVEGACIÓN NEGRA FULL-WIDTH ---------- */
    
    /* Contenedor padre del radio: fondo negro full-bleed real */
    div[data-testid="stRadio"] {
        background-color: #0B0F19;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        padding: 12px 0 14px 0;
        border-bottom: 3px solid #EA580C;
        box-sizing: border-box;
    }

    /* El grupo de radios en línea, centrado */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    /* Ocultar SOLO el círculo del radio, no el texto */
    div[data-testid="stRadio"] label > div:first-child {
        display: none !important;
    }

    /* Estilo base de cada opción del menú - LETRAS CLARAS */
    div[data-testid="stRadio"] label {
        background-color: transparent !important;
        color: #E2E8F0 !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        padding: 8px 18px !important;
        border-radius: 4px !important;
        cursor: pointer;
        transition: all 0.2s ease;
        border-bottom: 2px solid transparent;
        letter-spacing: 0.3px;
    }

    /* Hover */
    div[data-testid="stRadio"] label:hover {
        color: #FFFFFF !important;
        background-color: rgba(234, 88, 12, 0.12) !important;
    }

    /* Opción seleccionada */
    div[data-testid="stRadio"] label:has(input:checked) {
        color: #EA580C !important;
        border-bottom: 2px solid #EA580C !important;
    }

    /* Forzar que el texto dentro del label herede el color */
    div[data-testid="stRadio"] label p,
    div[data-testid="stRadio"] label span,
    div[data-testid="stRadio"] label div {
        color: inherit !important;
        font-size: inherit !important;
        margin: 0 !important;
    }

    /* Asegurar que el fondo del bloque de radio ocupe todo el ancho en Streamlit */
    div[data-testid="stRadio"] > div {
        width: 100% !important;
    }

    /* Quitar el fondo gris/blanco alrededor del st.radio */
    div[data-testid="stRadio"] + div,
    div[data-testid="stRadio"] ~ div:has(> div[data-testid="stVerticalBlock"]) {
        margin-top: 0 !important;
    }
