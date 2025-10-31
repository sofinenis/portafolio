import streamlit as st

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

st.write("")  # Espacio visual

# ==============================
# DATOS DE LAS 15 TARJETAS
# ==============================
titles = [
    "Intro", "Traductor", "texto a voz", "Conversión de Voz a Texto", "OCR Imangen",
    "OCR Texto", "Analisis de sentimiento", "Analisis texto Esp", "Sistema Ciberfísico", "Asistente de Chat",
    "Traductor Automático", "Generador de Imágenes", "Clasificador de Datos", "Detección de Sentimientos", "Asistente de Código"
]

images = [
    "img/txt_to_audio2.png", "img/txt_to_audio.png", "img/OIG5.jpg", "img/OIG8.jpg", "img/data_analisis.png",
    "img/OIG3.jpg", "img/Chat_pdf.png", "img/OIG4.jpg", "img/OIG6.jpg", "img/OIG7.jpg",
    "img/OIG9.jpg", "img/OIG10.jpg", "img/OIG11.jpg", "img/OIG12.jpg", "img/OIG13.jpg"
]

links = [
    "https://primerappjloqbfg8ikzs4ca7ke.streamlit.app/", "https://traductoor.streamlit.app/", "https://czccmjdyybe6oau4svuczk.streamlit.app/",
    "a/", "a", "a/",
    "a", "a/", "a/",
    "a", "ar", "a", "a",
    "a", "a"
]

# ==============================
# CREAR TARJETAS (15 ELEMENTOS, 3 FILAS DE 5 COLUMNAS)
# ==============================
index = 0
for fila in range(3):
    col1, col2, col3, col4, col5 = st.columns(5)
    for col in [col1, col2, col3, col4, col5]:
        if index < len(titles):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <img src="{images[index]}" alt="{titles[index]}">
                        <h4>{titles[index]}</h4>
                        <a href="{links[index]}" target="_blank">Enlace</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            index += 1
