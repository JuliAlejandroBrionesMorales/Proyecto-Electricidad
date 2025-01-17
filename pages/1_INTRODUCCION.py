# LIBRERIAS
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


# CSS PARA CAMBIAR COLOR DE FONDO
page_bg_color = '''
<style>
    .stApp {
        background-color: #E0E0E0; /* Gris más oscuro */
    }
    .title {
        color: #ffffff;
        text-align: center;
        font-size: 60px;
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        padding: 20px;
        border-radius: 10px;
    }
    .content-box {
        background-color: #ffffff; /* Fondo blanco para el contenido */
        border: 2px solid #d1d1d1; /* Borde gris claro */
        border-radius: 10px; /* Bordes redondeados */
        padding: 20px; /* Espaciado interno */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil */
        font-family: 'Arial', sans-serif; /* Fuente consistente */
    }
    .highlight {
        color: #FFA500; /* Color naranja para resaltar puntos clave */
        font-weight: bold;
    }
    .section-title {
        font-size: 24px; /* Tamaño de fuente para los títulos de sección */
        border-bottom: 2px solid #FFA500; /* Línea naranja debajo del título */
        padding-bottom: 10px; /* Espaciado debajo del título */
        margin-bottom: 20px; /* Espaciado debajo del título */
    }
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)


custom_title = '''
    <div class="title">
        INTRODUCCIÓN
    </div>
    '''
st.markdown(custom_title, unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
with col1:
    st.image('img_presentacion/2_introduccion.jpeg')
with col2:
    st.markdown('''
            <div class="content-box">
                <h2 class="section-title">Importancia de la Electricidad</h2>
                <p>La electricidad es una forma fundamental de energía que desempeña un papel crucial en nuestras vidas diarias. Es la base de la tecnología moderna y nos permite iluminar nuestros hogares, hacer funcionar nuestros dispositivos electrónicos y mantener nuestras ciudades en funcionamiento.</p>
                <div class="highlight">Confort y Convivencia:</div> Nos proporciona luz, calefacción, refrigeración y alimenta nuestros electrodomésticos y dispositivos, mejorando nuestra calidad de vida.
                <div class="highlight">Comunicación e Información:</div> Internet, teléfono y otros sistemas de comunicación dependen de la electricidad, manteniendo a las personas conectadas y accediendo a información.
                <div class="highlight">Desarrollo Económico:</div> La electricidad es fundamental para el funcionamiento de fábricas, empresas y servicios públicos, impulsando el crecimiento económico.
                <div class="highlight">Salud y Medicina:</div> Los hospitales y centros de salud dependen de la electricidad para operar equipos médicos vitales, como máquinas de rayos X, ventiladores y sistemas de monitoreo.
                <div class="highlight">Educación:</div> Las escuelas y universidades utilizan electricidad para alimentar computadoras, proyectores y otros equipos educativos, facilitando el aprendizaje y la enseñanza.
                <div class="highlight">Transporte:</div> Cada vez más vehículos eléctricos están siendo utilizados, reduciendo la dependencia de combustibles fósiles y disminuyendo la contaminación.<p>
            </div>
        ''', unsafe_allow_html=True)

 
