import streamlit as st

# Configuración
st.set_page_config(
    page_title="Compresor de Imágenes · PixelForge",
    page_icon="🖼️",
    layout="wide"
)

# Leer el archivo HTML
with open("comprimidor.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Mostrar el HTML en un iframe
st.components.v1.html(
    html_content,
    height=950,
    scrolling=True
)