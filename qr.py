import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Buscador de Mesas Corporativo",
    page_icon="bluelogo.png", # Puedes poner un link a un favicon .png si prefieres
    layout="centered")

st.markdown("""
    <style>
    /* Cambiar la fuente general a una más corporativa */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Estilo para el título principal */
    .titulo-pro {
        font-size: 32px !important;
        font-weight: 700;
        color: #201f1e;
        margin-bottom: 0px;
    }
    /* Estilo para las instrucciones */
    .instrucciones {
        font-size: 16px !important;
        color: #605e5c;
    }
    /* Hacer que el botón se vea más como el de la imagen */
    .stButton>button {
        background-color: #0078d4;
        color: white;
        border-radius: 2px;
        border: none;
        padding: 0.5rem 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("bluelogo.png", use_column_width=True)
# Título de la web
st.title("Localizador de Mesas")
st.write("Ingresa tu ID de Empleado para saber en qué mesa estás.")

# Función para cargar y limpiar datos
@st.cache_data
def cargar_datos():
    # Asegúrate de que el nombre coincida con tu archivo Excel
    df = pd.read_excel('prueba.xlsx')
    # Limpiamos la columna Codigo
    df['Codigo'] = df['Codigo'].astype(str).str.strip().str.replace('.0', '', regex=False)
    return df

# Cargar el Excel
try:
    df = cargar_datos()

   nombre = resultado.iloc[0]['Persona']
    mesa = resultado.iloc[0]['Mesa']
    
    # 1. Tu lista de códigos (ajústalos aquí)
    codigos_laptop = ["821", "97392", "53532"] 
    
    # Pasamos el carnet a texto para que la comparación sea exacta
    carnet_actual = str(resultado.iloc[0]['Codigo']) 

    st.markdown("---")
    # Usamos la clase de CSS que creamos antes para el nombre
    st.markdown(f'<p class="titulo-pro">Hola, {nombre}</p>', unsafe_allow_html=True)

    # 2. La lógica que decide qué mensaje mostrar
    if carnet_actual in codigos_laptop:
        st.info(f"Tu mesa asignada es la **{mesa}** y recuerda que **debes traer tu computadora**.")
    else:
        st.info(f"Tu mesa asignada es la **{mesa}**.")

except Exception as e:

    st.error(f"Error al cargar la base de datos: {e}")












