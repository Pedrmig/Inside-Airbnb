import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from streamlit_option_menu import option_menu
import joblib
train_model_forest = joblib.load('modelo_train.pkl')
train_model_new = joblib.load('modelo_train_new.pkl')
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
import streamlit.components.v1 as components


# ---------------------SITE CONFIG----------------------#
st.set_page_config(
    page_title="Airbnb: Hawaii",
    page_icon="🌅",
    layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["Home","Información","Precios",'Opiniones',"Power Bi", 'Predictor de Precios'],
        icons = ["house","book",'coin','table',"bar-chart","calculator"],
        menu_icon = "cast",
        default_index = 0,)

# creando el contenido de las páginas de acuerdo a la opción seleccionada

# PAGE 1-------------------------------------
if selected == "Home":
 
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1'>Análisis de datos del Airbnb Hawaii</h1>
    <p class='centered-text-pg1'>En cuanto al análisis de datos, pudimos identificar un problema usando los datos de Insideairbnb.com por lo que nos enfocamos en resolverlo y analizar el mercado de airbnb en Hawaii desde 2018.</p>
    <p class='centered-text-pg1'>Este conjunto de datos ofrece una oportunidad única para explorar y visualizar tendencias clave en el alquiler de propiedades.</p>
    <p class='centered-text-pg1'>Se han incorporado mapas interactivos de Folium, gráficos dinámicos y análisis de texto de los comentarios para una comprensión más profunda.</strong> para una comprensión más profunda.</p>
</div>
""", unsafe_allow_html=True)

    st.image('https://imgur.com/qrVfcpS.png', use_column_width=True)
    st.image('https://imgur.com/TWlePLO.jpg', use_column_width=True)
    st.markdown("<p class='images-text'>imagenes: https://w0.peakpx.com/wallpaper/963/58/HD-wallpaper-hawaiian-waves-waves-nature-beaches-hawaii.jpg</p>", unsafe_allow_html=True)
    st.markdown("<p class='images-text'>imagenes: https://www.adonde-y-cuando.es/site/images/illustration/hawai_642.jpg </p>", unsafe_allow_html=True)

# PAGE 2-------------------------------------
if selected == "Información":

    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1'>Información</h1>
    <p class='centered-text-pg1'>Las islas de Hawaii están ubicadas en el océano pacífico y forman parte de EEUU. Están formadas por 8 islas, pero nosotros vamos a centrarnos en las islas más pobladas y en aquellas en las que se permite el alquiler vacacional como son: Hawaii, Maui, Honolulu y Kauai.<p>
    <p class='centered-text-pg1'>Aquí puedes ver los diferentes alojamientos que se ofrecen en las diferentes islas y dónde están ubicados. Acércate en el mapa para ver con más detalle:</p>
</div>
""", unsafe_allow_html=True)
    
    with open("maps/map1.html", "r", encoding='utf-8') as f:     
        html_data = f.read()
        components.html(html_data, height=600)
    
    st.markdown("""
            ### Seleccione lo que más le interese:              
        """)

    # ---------------------TABS (pestañas)----------------------#
    tab1, tab2, tab3 = st.tabs(
        ['Acomodaciones','Potencialmente Ilegal','Volcanes']) 
    with tab1:
        
        ##  1. Acomodaciones

        st.markdown('### Acomodaciones')
        
        st.write('Las regulaciones sobre los tipos de alquileres a través de plataformas como Airbnb pueden tener un impacto significativo en el mercado de alquiler a corto plazo en Hawaii., donde se aplican regulaciones estrictas a corto plazo. La mayoría de las áreas residenciales están prohibidas para alquileres de menos de 30 días, a menos que el propietario tenga un permiso de (B&B) o una Unidad Transitoria (STU), pero estos permisos son limitados y están sujetos a ciertos requisitos.')
        
        st.write('Número de anuncios por vecindario')
        st.image('graficos/anuncios_por_vecindario.png', use_column_width=True)
        st.markdown("<p class='sub-figure'>En cuanto al número de anuncios por vecindario, destaca de forma considerable Primary Urban Center, seguido de Lahaina o Kihei-Makena.</p>", unsafe_allow_html=True)        
   
        st.write('Tipos de Propriedades')
        st.image('graficos/tipos_propriedades_hawaii.png', use_column_width=True)
        st.markdown("<p class='sub-figure'>En las diferentes islas, podemos encontrar distintos tipos de alojamientos, generalmente predominan los alquileres de condominios enteros, pero también podemos encontrar algunas más sorprendentes como casas en los árboles, casas pequeñas, yurts o estancias en granjas.</p>", unsafe_allow_html=True)
               
        st.write('Tipos de habitaciones')
        st.image('graficos/tipos_propriedades.png', use_column_width=True)
        st.markdown("<p class='sub-figure'>Los tipos de habitaciones disponibles en Airbnb generalmente se clasifican en 4: Casa o apartamento completo, habitación privada con áreas comunes, habitación de hotel y habitación compartida, aunque como podemos observar, generalmente los alquileres son de condominios enteros. </p>", unsafe_allow_html=True)

        st.write('Número de Viajeros')
        st.image('graficos/Acomodates.png', use_column_width=True)
        st.markdown("<p class='sub-figure'>texto nuevo.'</p>", unsafe_allow_html=True)

        st.write('Cantidad de anuncios por dia')
        with open("graficos/listings_available_by_date.html", "r", encoding='utf-8') as f:     
            html_data = f.read()
        components.html(html_data, height=450, width=950)
        st.markdown("<p class='sub-figure'>texto nuevo.'</p>", unsafe_allow_html=True)
        
    with tab2:
                
        ## 2. Government services

        st.markdown('### Analítica al servicio del gobierno')
        st.write('Hawaii tiene regulaciones diferentes de un condado a otro, y todas ellas están diseñadas para limitar el número de propiedades en alquiler. (https://www.hostaway.com/blog/airbnb-rules-in-hawaii/)')
            
        st.write('Encontrando Potenciales hoteles Ilegales')
        st.image('graficos/govserv1.png', use_column_width=False)
        
        st.write('Encontrando las cordenadas de los potenciales hoteles Ilegales')
        st.image('graficos/govserv2.png', use_column_width=True)
            
        st.write('Cantidad de Anuncions por Anfitrión')
        st.image('graficos/govserv3.png', use_column_width=True)

        st.write('Algunos Anfitriones son claramente profesionales')
        st.image('graficos/govserv4.png', use_column_width=True)
        
    
    with tab3:
            
        # 4. Vulcanes
        
        st.markdown("""
            ### Volcanes              
        """)
        st.write('Hawaii es un archipiélago de islas volcánicas en el Océano Pacífico. Las islas son el resultado de la actividad volcánica que comenzó hace millones de años.')
        st.write('La isla de Hawaii es el volcán más grande y activo del mundo.')
        st.write('Es un volcán en escudo, lo que significa que es un volcán grande y de forma redondeada.')
        st.write('Las islas de Hawaii cuentan actualmente con 5 volcanes (Mauna Loa, Kohala, Hulalai, Kilaue y Mauna Kea) 3 de ellos activos. Mauna Loa no entraba en erupción desde 1984, pero tuvo una erupción sin víctimas mortales en 2022.')
        st.image('https://static.temblor.net/wp-content/uploads/2018/05/hawaii-sp-7.jpg', use_column_width=True)


# PAGE 3----------------------------------
if selected == "Precios":
    st.markdown('### Precios')
    st.markdown('Abajo tenemos um mapa con el precio medio por vecindad, puede hacer zoom para ver más detalles:')
    
    with open("maps/map3.html", "r", encoding='utf-8') as f:     
        html_data = f.read()
    components.html(html_data, height=450)

    st.markdown('Precio promedio por vecindario')
    st.image('graficos/precio_medio_vecindario.png', use_column_width=True)
    
    st.markdown('Precio promedio por vecindario')
    with open("graficos/precio_vecindario.html", "r", encoding='utf-8') as f:     
        html_data = f.read()
    components.html(html_data, height=450, width=950)
        
    st.markdown('Precio promedio por dia para 2 personas') 
    with open("graficos/Average_Price_2_persons.html", "r", encoding='utf-8') as f:     
        html_data = f.read()
    components.html(html_data, height=450, width=950)
        
    st.markdown('Precio promedio por vecindario y tipo de habitación')
    with open("graficos/precio_habitacion_vecindario_box.html", "r", encoding='utf-8') as f:     
        html_data = f.read()
    components.html(html_data, height=450, width=950)
    
    st.markdown('Precio promedio por vecindario y tipo de habitación')
    st.image('graficos/precioxhabitacion_swarmplot.png', use_column_width=True)

# PAGE 4----------------------------------
if selected == "Opiniones":

    st.markdown("<p class='subtitles'>Puntaje Promedio de Revisión de Ubicación por Vecindario (con al menos 10 revisiones)</p>", unsafe_allow_html=True)
    st.image('graficos/review_score_price.png', use_column_width=True)
    
    st.markdown('Además de las reseñas escritas, los invitados pueden enviar una calificación de estrellas general y un conjunto de calificaciones de estrellas de categoría. Los huéspedes pueden dar calificaciones sobre:')
    st.markdown('* Experiencia general. ¿Cuál fue su experiencia en general?')
    st.markdown('* Limpieza. ¿Sentiste que tu espacio estaba limpio y ordenado?')
    st.markdown('* Precisión. ¿Con qué precisión su página de listado representó su espacio?')
    st.markdown('* Valor. ¿Sintió que su listado proporcionó un buen valor por el precio?')
    st.markdown('* Comunicación. ¿Qué tan bien se comunicó con su anfitrión antes y durante su estadía?')
    st.markdown('* Llegada. ¿Qué tan bien fue su registro?')
    st.markdown('* Ubicación. ¿Cómo te sentiste en el barrio?')
    st.markdown("<p class='subtitles'>A continuación puede ver la distribución de puntajes de todas esas categorías.'</p>", unsafe_allow_html=True)
    st.image('graficos/puntuaciones.png', use_column_width=True)

    st.markdown("<p class='subtitles'>Seguidamente, podemos ver que la parte más pequeña de los listados en Hawaii tienen un anfitrión que es Superanfitrión.</p>", unsafe_allow_html=True)
    st.image('graficos/list_superhost.png', use_column_width=True)   

    st.markdown("<p class='subtitles'>Palabras más comunes en los comentarios de los huéspedes</p>", unsafe_allow_html=True)
    st.image('graficos/wordcloud.png', use_column_width=True)


# PAGE 5----------------------------------
if selected == "Power Bi":
    st.markdown("""
            ## Este es un dashboard de PowerBI incrustado en una aplicación de Streamlit.
                Puedes interactuar con el dashboard directamente aquí.
        """)
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZmI2YmVjNmUtZjI3My00OTVmLWE1NGItNzY0ODNhNmJmM2M1IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""
            <iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
        """, unsafe_allow_html=True)

# PAGE 6----------------------------------
if selected == "Predictor de Precios": 

    # Función para predecir precio
    def predict_price(model, input_data):
        prediction = model.predict([input_data])
        return prediction[0]

    # Configurar Streamlit
    st.title("Previsión de Precios Airbnb")
    st.write("Introduce tus datos para predecir el precio:")

    # Botón de interruptor para cambiar entre modelos
    st.write("Selecciona el tipo de predicción:")
    switch_label = st.radio("", ("Nuevos Emprendimientos", "Viajeros"))

    # Elegir el modelo basado en la selección
    if switch_label == "Nuevos Emprendimientos":
        st.subheader("Página para Nuevos Emprendimientos")
        neighbourhoods = ['','Kauai', 'Honolulu', 'Maui', 'Hawaii']
        room_types = ['','Casa/Apartamento entero', 'Habitación privada', 'Habitación compartida', 'Habitación de hotel']
        availability = ['','10','30','60','120','240','365']

        # Colectar entrada del usuario
        neighbourhood = st.selectbox("Vecindario", neighbourhoods)
        minimum_nights = st.number_input("Mínimo de Noches permitidas de la estancia", min_value=0)
        room_type = st.selectbox("Tipo de Habitacion", room_types)
        availability_365 = st.selectbox("Disponibilidad en el Año", availability)

        # Mapeo de vecindarios a números
        neighbourhood_mapping = {name: idx for idx, name in enumerate(neighbourhoods)}
        neighbourhood_number = neighbourhood_mapping[neighbourhood]
        # Mapeo de tipos de habitación a números
        room_type_mapping = {name: idx for idx, name in enumerate(room_types)}
        room_type_number = room_type_mapping[room_type]

        # Preparar los datos de entrada
        input_data = [neighbourhood_number, room_type_number, minimum_nights, availability_365]

        # Predecir el precio basado en los datos de entrada
        if st.button("Predecir el Precio"):
            predicted_price = predict_price(train_model_new, input_data)
            st.write(f"El precio previsto es: ${predicted_price:.2f}")
    else:
        st.subheader("Página para Predicción de Existentes")
        # Lista de vecindarios
        neighbourhoods = ['','Kauai', 'Honolulu', 'Maui', 'Hawaii']
        room_types = ['','Casa/Apartamento entero', 'Habitación privada', 'Habitación compartida', 'Habitación de hotel']
        availability = ['','10','30','60','120','240','365']

        # Colectar entrada del usuario
        neighbourhood = st.selectbox("Vecindario", neighbourhoods)
        minimum_nights = st.number_input("Mínimo de Noches permitidas de la estancia", min_value=0)
        room_type = st.selectbox("Tipo de Habitacion", room_types)
        number_of_reviews = st.number_input("Número de Reviews totales recibidos", min_value=0)
        reviews_per_month = st.number_input("Reviews recibidos por Mes", min_value=0)
        availability_365 = st.selectbox("Disponibilidad en el Año", availability)

        # Mapeo de vecindarios a números
        neighbourhood_mapping = {name: idx for idx, name in enumerate(neighbourhoods)}
        neighbourhood_number = neighbourhood_mapping[neighbourhood]
        # Mapeo de tipos de habitación a números
        room_type_mapping = {name: idx for idx, name in enumerate(room_types)}
        room_type_number = room_type_mapping[room_type]

        # Preparar los datos de entrada
        input_data = [neighbourhood_number, room_type_number, minimum_nights, number_of_reviews, reviews_per_month, availability_365]

        # Predecir el precio basado en los datos de entrada
        if st.button("Predecir el Precio"):
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
        margin-top: 00px;
    }
    .subtitles {
        font-size: 25px;
        color: White;  
        margin-top: 10px;
    }
        .centered-title-pg1 {
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 20px;
        color: #fff;
        width: 90%; 
    }
    .justified-text-pg1 {
        text-align: justify;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        color: #ddd; 
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .centered-text-pg1 {
        text-align: center;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'Lato', sans-serif;
        color: #ddd; 
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .container {
        width: 100%;
        margin: 0 auto;
    }
    .sub-figure {
        text-align: left;
        color: white;
        font-size: 13px;
        margin-bottom: 45px; 
    }
    
</style>
"""
st.markdown(css, unsafe_allow_html=True)


