import streamlit as st
from pathlib import Path

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(page_title="🌻 Aplicaciones IA - Tema Floral", page_icon="🌼", layout="wide")

# ==============================
# ESTILOS - TEMA FLORAL GIRASOL
# ==============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff8dc 0%, #fff3b0 50%, #f9f7ef 100%);
    color: #4a3000;
    font-family: 'Trebuchet MS', sans-serif;
}
h1, h2, h3 {
    color: #5a3e00 !important;
    text-align: center;
    font-weight: bold;
}
p {
    color: #6a4a00;
    text-align: center;
}
.card {
    border: 3px solid #f6c700;
    border-radius: 20px;
    padding: 15px;
    background-color: #fff9e6;
    text-align: center;
    box-shadow: 0 4px 10px rgba(200,150,0,0.2);
    transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out;
}
.card:hover {
    transform: scale(1.04);
    box-shadow: 0 6px 14px rgba(230,180,0,0.3);
    background-color: #fff4d6;
}
.card img {
    border-radius: 12px;
    width: 100%;
    height: 180px;
    object-fit: cover;
    border: 2px solid #ffd700;
}
.card h4 {
    margin-top: 10px;
    color: #5c4000;
}
.card a {
    color: #d97706 !important;
    font-weight: bold;
    text-decoration: none;
}
.card a:hover {
    color: #b45309 !important;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# TÍTULO PRINCIPAL
# ==============================
st.markdown("""
<div style="border:3px solid #f6c700; border-radius:15px; padding:20px; background-color:#fffbea; text-align:center;">
    <h1>🌻 Aplicaciones Creativas con Inteligencia Artificial 🌻</h1>
    <p>Explora 15 herramientas de IA inspiradas en la naturaleza, la creatividad y los girasoles 🌼</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==============================
# CONFIGURAR RUTA DE IMÁGENES
# ==============================
img_dir = Path(__file__).parent / "images"  # asegúrate que exista la carpeta "images" junto al .py

titles = [
    "Intro", "Traductor", "Texto a voz", "Reconocimiento de imagen", "Análisis de sentimiento",
    "Análisis de texto ESP", "Análisis texto ING", "Reconocimiento de objetos", "Reconocimiento de gestos", "Chat PDF",
    "Interpretación de imagen", "Interfaz táctil", "Bocetos", "Lector MQTT", "Control por Voz"
]

images = [
    "girasol.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg",
    "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg",
    "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg"
]

links = [
    "https://primerappjloqbfg8ikzs4ca7ke.streamlit.app/", "https://traductoor.streamlit.app/", "https://czccmjdyybe6oau4svuczk.streamlit.app/",
    "https://imagenaudiocoso.streamlit.app/", "https://anlisisdetexto.streamlit.app/", "https://tdfesppp.streamlit.app/",
    "https://textancis.streamlit.app/", "https://yolovv5.streamlit.app/", "https://tmreconocimiento.streamlit.app/",
    "https://tableronumero.streamlit.app/", "https://dibujo.streamlit.app/", "https://recepmqttsofi.streamlit.app/", 
    "https://ctrlvoicee.streamlit.app/", "https://textancis.streamlit.app/", "https://primerappjloqbfg8ikzs4ca7ke.streamlit.app/"
]

# ==============================
# MOSTRAR LAS 15 TARJETAS (5 columnas × 3 filas)
# ==============================
index = 0
for fila in range(3):
    cols = st.columns(5)
    for col in cols:
        if index < len(titles):
            img_path = img_dir / images[index]
            with col:
                if img_path.exists():
                    st.markdown(
                        f"""
                        <div class="card">
                            <img src="data:image/jpg;base64,{(img_path.read_bytes()).hex()}" alt="{titles[index]}">
                            <h4>{titles[index]}</h4>
                            <a href="{links[index]}" target="_blank">Enlace</a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.warning(f"⚠ No se encontró la imagen: {images[index]}")
            index += 1
