import streamlit as st

st.set_page_config(page_title="Galería de Ejercicios - Flores", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #fff7e6;
        color: #3e2f1c;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: #d18b00;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .card {
        background-color: #fff8f0;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(200, 150, 50, 0.3);
        padding: 10px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0px 6px 15px rgba(180, 130, 20, 0.4);
    }
    img {
        border-radius: 10px;
        margin-bottom: 8px;
        border: 2px solid #f3d673;
    }
    h4 {
        color: #d8a100;
        margin-bottom: 5px;
    }
    code {
        background-color: #fff0d1;
        padding: 5px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌻 Galería de Ejercicios - Tema de Flores 🌻</div>', unsafe_allow_html=True)

# Lista de imágenes desde GitHub (puedes cambiar los nombres si tus archivos son png/jpg diferentes)
images = [
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/1.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/2.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/3.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/4.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/5.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/6.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/7.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/8.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/9.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/10.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/11.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/12.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/13.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/14.jpg",
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/15.jpg"
    "https://raw.githubusercontent.com/sofinenis/portafolio/main/girasol.jpg"
]

titles = [f"Ejercicio {i+1}" for i in range(15)]
codes = [f"Código {i+1}" for i in range(15)]

cols_per_row = 5
for i in range(0, len(images), cols_per_row):
    cols = st.columns(cols_per_row)
    for idx, col in enumerate(cols):
        if i + idx < len(images):
            with col:
                st.markdown(f"""
                    <div class="card">
                        <img src="{images[i+idx]}" width="100%" />
                        <h4>{titles[i+idx]}</h4>
                        <code>{codes[i+idx]}</code>
                    </div>
                """, unsafe_allow_html=True)
