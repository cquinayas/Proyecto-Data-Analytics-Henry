import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import importlib
from PIL import Image

st.set_page_config(layout="wide")
df_coursera = pd.read_csv("coursera.csv")
df_edx = pd.read_csv("edx.csv")
df_udemy = pd.read_csv("udemy.csv")
nivel = {1:'Beginner',2:'Intermediate',3:'Advanced',4:'All'}
image = Image.open('mooc.png')
imagec = Image.open('coursera.png')
imagee = Image.open('edx.png')
imageu = Image.open('udemy.png')


rc = {
          'axes.facecolor':'#0e1117',
          'axes.edgecolor': '#0e1117',
          'axes.labelcolor': 'white',
          'figure.facecolor': '#0e1117',
          'patch.edgecolor': '#0e1117',
          'text.color': 'white',
          'xtick.color': 'white',
          'ytick.color': 'white',
          'grid.color': 'grey',
          'font.size' : 10,
          'axes.labelsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10}

 
plt.rcParams.update(rc)
#plt.xticks(rotation=66,horizontalalignment="right")
nombreDataset = st.sidebar.selectbox("**Seleccionar la plataforma educativa**",("Coursera", "EDX","Udemy"))
nombreFeature = st.sidebar.selectbox("**Seleccionar la característica a analizar**",('level', 'language', 'rating'))
specific_team_colors = st.sidebar.checkbox("Usar una paleta de colores")
#nivel = st.sidebar.select_slider('Seleccione el nivel educativo (1:Beginner,2:Intermediate,3:Advanced,4:All)', value = ["1","4"])
nivel= st.sidebar.select_slider(
    'Seleccione el nivel educativo',
    options=['Beginner', 'Intermediate', 'Advanced', 'All'])
    #value=('Beginner', 'All'))
language= st.sidebar.select_slider(
    'Seleccione el lenguaje',
    options=['English', 'Spanish'])
#st.write(nivel)
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
    st.markdown("### **Dashboard que permite analizar el nivel de ventas según precio, idioma, nivel y rating en las plataformas Coursera, EDX y Udemy**")
    st.markdown("**Puedes encontrar el repositorio en [cquinayas GitHub Repositorio](https://github.com/tdenzl/BuLiAn)**")

### DATA EXPLORER ###
row12_spacer1, row12_1, row12_spacer2 = st.columns((.2, 7.1, .2))
with row12_1:
    st.subheader('Indicadores claves para el negocio de los MOOCS')
    
m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
 # Como influye el nivel con las ventas totales
with m2:
    if nombreDataset == 'Coursera':
        ventas_totales = df_coursera['sales'].sum()
        st.metric(label ='Total ventas (Millones)',value = np.round((ventas_totales/1000000),2))
    if nombreDataset == 'EDX':
        ventas_totales = df_edx['sales'].sum()
        st.metric(label ='Total ventas (Millones)',value = np.round((ventas_totales/1000000),2)) 
    if nombreDataset == 'Udemy':
        ventas_totales = df_udemy['sales'].sum()
        st.metric(label ='Total ventas (Millones)',value = np.round((ventas_totales/1000000),2))   
with m3:
    if nombreDataset == 'Coursera':
        if nivel!= 'All':
            rating = df_coursera[df_coursera['level']==nivel]
            rating_sales = rating.groupby('level')['sales'].sum().round(2)
            st.metric(label ='Porcentaje de ventas segun el nivel',value = np.round((rating_sales/ventas_totales)*100,2))
    if nombreDataset == 'EDX':
        if nivel!= 'All':
            if nivel== 'Beginner':
                rating = df_edx[df_edx['level']=='Introductory']
            else:
                rating = df_edx[df_edx['level']==nivel]
            rating_sales = rating.groupby('level')['sales'].sum().round(2)
            st.metric(label ='Porcentaje de ventas segun el nivel',value = np.round((rating_sales/ventas_totales)*100,2))
    if nombreDataset == 'Udemy':
        if nivel== 'Advanced':
                rating = df_udemy[df_udemy['level']=='Expert']
        else: 
            rating = df_udemy[df_udemy['level']==nivel]   
        rating_sales = rating.groupby('level')['sales'].sum().round(2)
        st.metric(label ='Porcentaje de ventas segun el nivel',value = np.round((rating_sales/ventas_totales)*100,2))
# El idioma con las ventas totales 
with m4:
    if nombreDataset == 'Coursera':
        language = df_coursera[df_coursera['language']==language]
        language_sales = language.groupby('language')['sales'].sum().round(2)
        st.metric(label ='Porcentaje de ventas segun el idioma',value = np.round((language_sales/ventas_totales)*100,2))
    
    if nombreDataset == 'EDX':
        if language == 'Spanish':
            language = 'Español' 
        language = df_edx[df_edx['language']==language]
        language_sales = language.groupby('language')['sales'].sum().round(2)
        st.metric(label ='Porcentaje de ventas segun el idioma',value = np.round((language_sales/ventas_totales)*100,2))  
    if nombreDataset == 'Udemy':
        language = df_udemy[df_udemy['language']==language]
        language_sales = language.groupby('language')['sales'].sum().round(2)
        st.metric(label ='Porcentaje de ventas segun el idioma',value = np.round((language_sales/ventas_totales)*100,2)) 
       
### Features ###
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('Análisis relacionado con el :green[nivel, lenguage y ranting] 💎')
row5_spacer1, row5_1, row5_spacer2 = st.columns((.2, 7.1, .2))
with row5_1:  
    #plt.figure(figsize=(12,4.5)) 
    plt.rcParams["figure.figsize"] = (14, 3.5) 
    fig, ax = plt.subplots()
    if nombreDataset == 'Coursera':
        if specific_team_colors:
            ax = sns.countplot(data=df_coursera, x=nombreFeature)
        else:
            ax = sns.countplot(data=df_coursera, x=nombreFeature,color = "#b80606")
    if nombreDataset == 'EDX':
        if specific_team_colors:
            ax = sns.countplot(data=df_edx, x=nombreFeature)
        else:
            ax = sns.countplot(data=df_edx, x=nombreFeature,color = "#b80606")
    if nombreDataset == 'Udemy':
        if specific_team_colors:
            ax = sns.countplot(data=df_udemy, x=nombreFeature)
        else:
            ax = sns.countplot(data=df_udemy, x=nombreFeature,color = "#b80606")
    ax.set_title(f'Conteo por {nombreFeature} en la plataforma {nombreDataset}')
    plt.xticks(rotation=66,horizontalalignment="right")
    st.pyplot(fig)  
### Prices ###
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.subheader('Análisis relacionado con el :red[precio] 💰')
#row6_spacer1, row6_1, row6_spacer2, row6_2, row6_spacer3  = st.columns((.2, 4.4, .4, 4.4, .2)) 
row6_spacer1, row6_1, row6_spacer2, row6_2, row6_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2)) 
with row6_1:
    st.subheader('Precios promedios')
    if nombreDataset == 'Coursera':
        valor_prom_curso = df_coursera.groupby([nombreFeature])['price'].mean().round(2)
        st.dataframe(valor_prom_curso.sort_values(ascending=False),500)
    if nombreDataset == 'EDX':
        valor_prom_curso = df_edx.groupby([nombreFeature])['price'].mean().round(2)
        st.dataframe(valor_prom_curso.sort_values(ascending=False),500)    
    if nombreDataset == 'Udemy':
        valor_prom_curso = df_udemy.groupby([nombreFeature])['price'].mean().round(2)
        st.dataframe(valor_prom_curso.sort_values(ascending=False),500)    
with row6_2: 
    plt.rcParams["figure.figsize"] = (6, 4.5)    
    fig, ax = plt.subplots()
    if nombreDataset == 'Coursera':
        if specific_team_colors:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_coursera)
        else:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_coursera,color = "#b80606")
    if nombreDataset == 'EDX':
        if specific_team_colors:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_edx)
        else:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_edx,color = "#b80606")
    if nombreDataset == 'Udemy':
        if specific_team_colors:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_udemy)
        else:
            ax = sns.barplot(x="price", y=nombreFeature, data=df_udemy, color = "#b80606")
    ax.set_title(f'Relación entre {nombreFeature} y el precio en la plataforma {nombreDataset}')
    plt.xticks(rotation=66,horizontalalignment="right")
    st.pyplot(fig)  

### Ventas ###
row7_spacer1, row7_1, row7_spacer2 = st.columns((.2, 7.1, .2))
with row7_1:
    st.subheader('Análisis relacionado con las :blue[ventas] 🥇')
#row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
row8_spacer1, row8_1, row8_spacer2, row8_2, row8_spacer3  = st.columns((.2, 5.3, .4, 4.4, .2)) 
with row8_1:
    #plt.rcParams["figure.figsize"] = (6, 3.5) 
    plt.rcParams["figure.figsize"] = (3, 3.5) 
    fig, ax = plt.subplots()
    if nombreDataset == 'Coursera':
        top_venta = pd.DataFrame(data=df_coursera.sort_values(by = 'sales' , ascending = False))[['title','sales']].head(5)
        if specific_team_colors:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title')
        else:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title', color = "#b80606")
    if nombreDataset == 'EDX':
        top_venta = pd.DataFrame(data=df_edx.sort_values(by = 'sales' , ascending = False))[['title','sales']].head(5)
        if specific_team_colors:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title')
        else:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title', color = "#b80606")
    if nombreDataset == 'Udemy':
        top_venta = pd.DataFrame(data=df_udemy.sort_values(by = 'sales' , ascending = False))[['title','sales']].head(5)
        if specific_team_colors:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title')
        else:
            ax = sns.barplot(data = top_venta , x = 'sales' , y = 'title', color = "#b80606")
    st.pyplot(fig)
with row8_2:
    if nombreDataset == 'Coursera':
        st.image(imagec)
    if nombreDataset == 'EDX':
        st.image(imagee)
    if nombreDataset == 'Udemy':
        st.image(imageu)
   
   
    
   
  