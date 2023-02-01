# Proyecto Individual 3 Data Analytics

* Segmentar el nivel de ventas según precio, idioma, nivel y rating de cada curso para analizar qué tanto influyen dichas variables en la demanda del producto vendido
* WordCloud de las palabras clave que más se repiten dentro del título
* Establecer al menos 1 KPI producto del análisis y que el mismo se pueda visualizar en un dashboard

# Desarrollo del proyecto
1. Análisis exploratorio de los datos (EDA)
- Data wrangling de los datasets
- Web Scraping para completar la tabla de Coursera
- Visualización en diagrama de barras de la frecuencia de los datos de las columnas level,language y rating
- Visualización de la relación entre el precio y el nivel, languaje y rating de los cursos
- Top 5 de los cursos con mayores ventas 
- Wordcloud de las palabras con mayor frecuencia en los títulos de los cursos

[EDA.ipynb](https://github.com/cquinayas/Proyecto-Data-Analytics-Henry/blob/main/EDA.ipynb)


2. Desarrollo de un dashboard en Streamlit
- Se presentan gráficos de barras de las variables categóricas (level, language, rating) donde se muestran la distribución de los datos
- Se presentan gráficos que muestran la relación entre el precio de los cursos y las variables categóricas
- Se muestra el top 5 de los cursos con mayores ventas
- Se muestra el wordcloud de las palabras que más se repiten en los títulos de los cursos 

<https://cquinayas-proyecto-data-analytics-henry-app-r5hfvx.streamlit.app/>

3. KPI
- Porcentajes de las ventas de acuerdo al nivel de los cursos con respecto al ventas totales. Este kpi entrega información de los cursos con mayor venta en un nivel determinado, considerando que estas plataformas tienen curso de nivel principiante, intermedio y avanzado
- Porcentaje de las ventas de acuerdo al idioma con respecto a las ventas totales. Este kpi entrega información de los cursos en los idiomas más demandados, permitiendo tomar decisiones sobre mercados potenciales geográficamente
