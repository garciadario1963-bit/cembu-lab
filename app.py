import base64

# Si tenés el logo guardado localmente (ej: "logo.png"), usás esto:
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Reemplazá 'logo.png' por la ruta de tu imagen local o dejá la URL si es externa
try:
    logo_base64 = get_base64_image("logo.png") # Nombre de tu archivo de logo
    logo_src = f"data:image/png;base64,{logo_base64}"
except Exception:
    logo_src = "https://via.placeholder.com/180x60/0B0F19/EA580C?text=LOGO+CEMBU"

# 3. HEADER NEGRO CON LOGO Y REDES SOCIALES
header_html = """
<div class="top-black-banner">
    <div class="logo-container">
        <img src="{LOGO_PLACEHOLDER}" alt="Logo CEMBU">
    </div>

    <div class="social-icons-container">
        <a href="#" class="social-icon" title="Instagram">📷</a>
        <a href="#" class="social-icon" title="X (Twitter)">𝕏</a>
        <a href="#" class="social-icon" title="LinkedIn">in</a>
        <a href="#" class="social-icon" title="YouTube">▶</a>
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
""".replace("{LOGO_PLACEHOLDER}", logo_src)

st.markdown(header_html, unsafe_allow_html=True)
