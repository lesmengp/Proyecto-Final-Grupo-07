<p align="center"><img src="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png"></p>

<h1 align="center">**`PROYECTO FINAL GRUPO Nº 7`</h1>

<h1 align="center">
  <span style="font-size: 25px;">Autores: Javier Castro, Luca Ramallo, Luis Ramírez, Lesmen García.</span> <br>
  <a href="https://github.com/lesmengp/Proyecto-Final-Grupo-07.git">GitHub: <span style="font-size: 20px;">Proyecto Yelp & Google Maps</span></a> <br> 
</h1>

<h1 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`</h1>

<p align="center">
<img src="src/Imagenes/Img01.png" height="300">
</p>

## ML:<br>
En esta sección encontraremos la aplicación de sistemas de IA & ML para el proyecto JL3.<br>

## Cosine Similarity:<br>
Contiene la aplicación, primero de un Cosine Similarity, cuyo objetivo es encontrar 10 negocios similares ya establecidos, a partir del estudio de las características de un negocio/establecimiento seleccionado como semilla y perteneciente al conjunto de datos (por ser esta una versión M.V.P) donde se toman más de 200 parámetros a configurar en características.<br>
<br>
Es decir, ¿A dónde apuntamos con esto?<br>
Al aplicar Cosine Similarity, en base a más de 200 parámetros, buscando entre todos los negocios ya existentes en las plataformas de Google Maps y Google Yelp, lo que buscamos es que el usuario pueda verificar si la idea de negocio de quien consulta el sistema ya existe en el mercado, en otras palabras, si ya se encuentra registrada en las plataformas y, en caso de que no exista, poder revisar las 10 primeras ideas de negocio ya existentes que más se asemejen a esta configuración particular de parámetros que posee el negocio semilla que le estamos preguntando al algoritmo.<br>
De esta manera, podríamos, sin tener la necesidad de invertir realmente en implementar una idea de negocio, analizar nuestra competencia más próxima, ver si existen opciones similares ya en el mercado y poder responder a la pregunta: ¿Cómo le está yendo con dicha idea de negocio?<br>

## Regresión Ridge:<br>
También, por ser versión M.V.P., contamos con un modelo Ridge a partir de una semilla establecida perteneciente al conjunto de datos para su prueba. El objetivo de la regresión aquí planteada es, en base a los parámetros de la semilla, calcular la respuesta a una métrica muy importante establecida para el desarrollo de este proyecto... EL VOLUMEN DE ESTRELLAS ✨.<br>
Ridge, en base a los parámetros, podrá pronosticar el volumen de estrellas que recaudará nuestra idea de negocio (aún no emplazada en la realidad) y poder tener así una muy buena idea de cómo nos irá con dicha inversión si realmente la llevamos a cabo....<br>
Ambos modelos están pensados para funcionar con nuevas ideas de negocio que no existan dentro del conjunto de datos y poder reducir la incertidumbre de quienes tienen pensado llevarlas a cabo, en base a: un análisis de la competencia ya existente y un pronóstico de cómo le irá particularmente a dicha idea con el volumen de estrellas..<br>
Cabe mencionar que podríamos ir reajustando los parámetros de nuestro negocio y repreguntar a los algoritmos para ver si mejora nuestro pronóstico o no. Siguiendo un ejemplo simple, supongamos que si a mi negocio le agrego Servicio de Wifi... ¿tendré más clientes? Y si agrego también Bike Parking? Así sucesivamente, cuantas veces queramos...<br>
Demo Streamlit:
En la sección inversionistas: https://pfmljl3.streamlit.app/

