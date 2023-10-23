<p align=center ><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **`PROYECTO FINAL GRUPO Nº 7`** </h1>

<h1 align="center">
  <span style="font-size: 25px;">@utores:  Javier Castro, Luca Ramallo, Luis Ramirez, Lesmen Garcia.</span> <br>
  <a href="https://github.com/lesmengp/Proyecto-Final-Grupo-07.git">GitHub: <span style="font-size: 20px;">Proyecto Yelp & Google Maps</span></a> <br> 
</h1>

# <h1 align=center>**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<p align="center">
<img src="src/Imagenes/Img01.png", height=300>
</p>

## ML:<Br>
-  En esta seccion encontraremos la aplicacion de sistemas de IA & ML para el proyecto JL3.<Br>


## Cosine Similarity:<Br>

- Contiene la aplicacion, 1ro de un Cosine Similarity, cuyo objetivo es: encontrar 10 negocios similares ya establecidos, a partir del estudio de las caracteristicas de  un negocio / establecimiento, seleccionado como semilla y perteneciente al set de datos (por ser esta una version M.V.P) donde se toman más de 200 parámetros a setear en caracteristicas. <Br>
<Br>

Es decir, ¿A donde apuntamos con esto?..<Br>

Al aplicar Cosine Similarity, en base a mas de 200 parametros, buscando entre todos los negocios ya existentes en las plataformams de Google Maps y Google Yelp, Lo que buscamos es que el usuario pueda verificar: si la idea de negocio de quien consulta el sistema, ya existe en el mercado, en otras palabras si ya se encuentra registrada en las plataformas y en caso de que no exista, poder revisar las 10 primeras ideas de negocio ya existentes que más se asemejen a esta configuracion particular de parametros que pose el negocio semilla que le estamos preguntando al algoritmo.<Br>
De esta manera, Podriamos: SIN tener la necesidad de invertir realmente en emplazar realmente una idea de negocio, analizar nuestra competencia más próxima, ver si existen opciones similares ya en el mercado y poder responder a la pregunta: ¿Cómo le esta yendo con dicha idea de negocio?<Br>


## Regresion Ridge:<Br>

- Tambien, por ser version M.V.P. contamos con un modelo Ridge a partir de una semilla establecida perteneciente al set de datos para su prueba. El Objetivo de la regresion aqui planteada es: en base a los parametros de la semilla, calcular la respuesta a una metrica muy importante establecida para el desarrollo de este proyecto... EL VOLÚMEN DE ESTRELLAS ✨.<Br>

Ridge, en base a los parametros, podra pronosticar el volumen de estrellas que recaudará nuestra idea de negocio (aún no emplazada en la realidaad) y poder tener asi, una muy buena idea de como nos va a ir con dicha inversion si realmente la llevamos a cabo....<Br>


Ambos modelos estan pensados para fucnionar con nuevas ideas de negocio, que no existan dentro del set de datos y poder reducir la incertidumbre de quienes tienen pensado llevarlas a cabo, en base a: un analisis de la competencia ya existente y un pronostico de como le irá particularmente a dicha idea con el volumen de estrellas..<Br>

Cabe mensionar, que podriamos ir re ajustando los parametros de nuestro negocio y repreguntar a los algoritmos, para ver si mejora nuestro pronostico o no. Siguiendo un ejemplo simple, supongamos que si a mi negocio le agrego Servicio de Wifi... tendre mas clientes? y si agrego tambien Bike Parking ? asi susecivamente cuantas veces querramos...<Br>

Demo Streamlit:
En la seccion inversionistas:
https://pfmljl3.streamlit.app/


