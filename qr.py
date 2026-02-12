import streamlit as st
import pandas as pd
import base64

st.set_page_config(
    page_title="Buscador de Mesas Corporativo",
    page_icon="bluelogo.png", # Puedes poner un link a un favicon .png si prefieres
    layout="centered")
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(fondopagina):
    bin_str = get_base64(fondopagina)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    /* Esto crea el cuadro blanco semitransparente para que el texto sea legible */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.85); 
        padding: 3rem;
        border-radius: 20px;
        margin-top: 2rem;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('fondopagina')

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
    df = pd.read_excel("prueba.xlsx")
    
    # El buscador
    id_empleado = st.text_input("Ingresa tu ID de Empleado")

    if id_empleado:
        # Buscamos el ID (convertimos a string para evitar errores de tipo)
        resultado = df[df['Codigo'].astype(str) == id_empleado]

        if not resultado.empty:
            nombre = resultado.iloc[0]['Persona']
            mesa = resultado.iloc[0]['Mesa']
            
            # --- Lógica de la Laptop ---
            codigos_laptop = ["821", "97392", "53532"] # Pon aquí tus códigos reales
            
            st.markdown("---")
            st.markdown(f"### Hola, {nombre}")
            
            if id_empleado in codigos_laptop:
                st.info(f"Tu mesa asignada es la **{mesa}** y recuerda que **debes traer tu computadora**.")
            else:
                st.info(f"Tu mesa asignada es la **{mesa}**.")
        else:
            st.error("ID no encontrado. Por favor, verifica e intenta de nuevo.")

except Exception as e:
    st.error(f"Error al cargar la base de datos: {e}")


















