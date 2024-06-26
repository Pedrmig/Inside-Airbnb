import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import importlib.util
import streamlit_option_menu
from streamlit_option_menu import option_menu
import joblib
train_model_forest = joblib.load('modelo_train.pkl')

# ---------------------SITE CONFIG----------------------#
st.set_page_config(
    page_title="Airbnb: Hawaii",
    page_icon="🌅",
    layout="centered", 
     
)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home","Datos","Análisis","Power Bi",'Reviews', 'Predictor de Precios'],
        icons = ["house","book","bar-chart",'table',"filter","calculator"],
        menu_icon = "cast",
        default_index = 0,)
    
    if selected == "Home":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Análisis del conjunto de datos del Airbnb Hawaii.</h2>', unsafe_allow_html=True)
        
    if selected == "Datos":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Se ha usado Python y Jupiter Notebook para el análisis.</h2>', unsafe_allow_html=True)
        st.markdown('<h2 class="header-black">Librerías utilizadas: Pandas, Numpy, Matplotlib, Seaborn, Sklearn, IPython, Streamlit.</h2>', unsafe_allow_html=True)
        
    if selected == "Análisis":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Análisis de datos del Airbnb Hawaii y representación visual de los resultados.</h2>', unsafe_allow_html=True)
    
    if selected == "Power Bi":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Panel de Analísis en Power BI.</h2>', unsafe_allow_html=True)
        
    if selected == "Reviews":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Filtros por principales Reviews.</h2>', unsafe_allow_html=True)
        
    if selected == "Predictor de Precios":
        st.title(f"{selected}")
        st.markdown('<h2 class="header-black">Predictor de Precios Basado en el Dataset.</h2>', unsafe_allow_html=True)
        

# creando el contenido de las páginas de acuerdo a la opción seleccionada
if selected == "Home":
    st.markdown("<h1 class='centered-text'>Análisis de datos del Airbnb Hawaii</h1>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Insideairbnb.com es un sitio web en el que se publican conjuntos de datos extraídos de la web de 'instantáneas' de ciudades. He descargado los archivos de Hawaii de la situación del 6 de diciembre de 2018.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>Pensé que era un conjunto de datos divertido para asumir. Además de la disputa de datos básicos y las tramas.</p>", unsafe_allow_html=True)
    st.markdown("<p class='justified-text'>También he agregado <strong>mapas interactivos de Folium, gráficos interactivos de tramas y extracción de texto de los comentarios de revisión.</strong></p>", unsafe_allow_html=True)
    st.image('https://imgur.com/qrVfcpS.png', use_column_width=True)
    st.image('https://imgur.com/TWlePLO.jpg', use_column_width=True)
    st.markdown("<p class='images-text'>imagenes: https://w0.peakpx.com/wallpaper/963/58/HD-wallpaper-hawaiian-waves-waves-nature-beaches-hawaii.jpg</p>", unsafe_allow_html=True)
    st.markdown("<p class='images-text'>imagenes: https://www.adonde-y-cuando.es/site/images/illustration/hawai_642.jpg </p>", unsafe_allow_html=True)























if selected == "Predictor de Precios": 

    # Função para prever preço
    def predict_price(model, input_data):
        prediction = model.predict([input_data])
        return prediction[0]

    # Configurar o Streamlit
    st.title("Prevision de Preços do Airbnb")
    st.write("Insira los datos para prever ell precio:")

    # Coletar entrada do usuário
    neighbourhood = st.number_input("Vecindario", min_value=0)
    minimum_nights = st.number_input("Minimo de Notches", min_value=0)
    room_type = st.number_input("Tipo de Cuarto", min_value=0)
    number_of_reviews = st.number_input("Numero de Reviews", min_value=0)
    reviews_per_month = st.number_input("Reviews por Mes", min_value=0)
    availability_365 = st.number_input("Avaliable en el Año", min_value=0)

    # Preparar os dados de entrada
    input_data = [neighbourhood, room_type, minimum_nights, number_of_reviews, reviews_per_month, availability_365]

    # Prever o preço com base nos dados de entrada
    if st.button("Prever Precio"):
        predicted_price = predict_price(train_model_forest, input_data)
        st.write(f"El precio previsto es: ${predicted_price:.2f}")


# Adicionar CSS al app Streamlit
css = """
<style>
    [data-testid="stSidebar"] {
        background-image: url(https://imgur.com/6VyJtZt.png);
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .header-black {
        color: black;
    }
        .centered-text {
        text-align: center;
        color: white;
        font-size: 40px;
        margin-bottom: 40px; 
    }
    .justified-text {
        text-align: justify;
        margin-bottom: 40px;
    }
    .images-text {
        font-size: 9px;
        color: grey;  
        margin-top: 10px;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)