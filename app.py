import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")
df_coursera = pd.read_csv("coursera.csv")
df_edx = pd.read_csv("edx.csv")
df_udemy = pd.read_csv("udemy.csv")
image = Image.open('mooc.png')


####################
### INTRODUCTION ###
####################

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.image(image)
    #st.title('MOOC- Análisis de cursos masivos abiertos  online')
with row0_2:
    st.title('MOOC- Análisis de cursos masivos abiertos  online')
    st.text("")
    st.subheader('Streamlit App desarrollado por [César Quinayás](https://www.linkedin.com/in/cesar-augusto-quinayas-burgos-544084243/)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("### **Dashboard que permite analizar el nivel de ventas según precio, idioma, nivel y rating  en las plataformas Coursera, EDX y Udemy**")
    st.markdown("**Puedes encontrar el repositorio en [cquinayas GitHub Repositorio](https://github.com/cquinayas/Proyecto-Data-Analytics-Henry)**")

row7_spacer1, row7_1, row7_spacer2 = st.columns((.1, 3.2, .1))
with row7_1:
        st.markdown("## PROYECTO INDIVIDUAL No 3")
        st.markdown("* Segmentar el nivel de ventas según precio, idioma, nivel y rating de cada curso para analizar qué tanto influyen dichas variables en la demanda del producto vendido" )
        st.markdown("* WordCloud de las palabras clave que más se repiten dentro del título")
        st.markdown("* Establecer al menos 1 KPI producto del análisis y que el mismo se pueda visualizar en un dashboard")
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.markdown("")
    see_data = st.expander('Base de datos Coursera 👉')
    with see_data:
        df_coursera=df_coursera.drop('Unnamed: 0',axis=1)
        st.markdown("#### Coursera es una plataforma que ofrece cursos online de más de 275 universidades y empresas líderes de primer nivel")
        st.dataframe(data=df_coursera)
       
st.text('')
row5_spacer1, row5_1, row5_spacer2 = st.columns((.2, 7.1, .2))
with row5_1:
    st.markdown("")
    see_data = st.expander('Base de datos EDX 👉')
    with see_data:
        df_edx=df_edx.drop('Unnamed: 0',axis=1)
        st.markdown("#### EDX es un proveedor de Moocs con mas de 3600 cursos y 42 millones de usuarios")
        st.dataframe(data=df_edx)
        
st.text('')

row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    st.markdown("")
    see_data = st.expander('Base de datos Udemy 👉')
    with see_data:
        df_udemy=df_udemy.drop('Unnamed: 0',axis=1)
        st.markdown("#### Udemy es la tienda virtual de enseñanza y apredizaje con 44 millones de estudiantes, 183.000 cursos y 75 idiomas")
        st.dataframe(data=df_udemy)
        
st.text('')