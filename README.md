Para el presente práctico se deben procesar los datos de Series de Televisión disponibles en una plaforma de streaming.

En primer lugar se cuenta con el archivo generos.txt en el que aparecen los géneros o temáticas de cada serie a razón de un género por línea. 

Y también se cuenta con el archivo series_aed.csv que es un archivo separado por pipes ("|") en el que se cuenta con una primera línea de cabecera y luego los datos con las siguientes columnas:

Poster_Link: link del poster de la serie en Amazon.
Series_Title: Título de la serie.
Runtime_of_Series: año desde - año hasta de la serie (puede estar en blanco el año desde).
Certificate: Categoría de la serie, puede estar en blanco.
Runtime_of_Episodes: tiempo promedio de los capítulos. Es un número seguido por la palabra "min".
Genre: Género de la serie.
IMDB_Rating: Es el rating que va de 1 a 9,7
Overwiew: Es un resumen de la serie.
Star1, Star2, Star3 y Star4: Son los actores y actrices de la serie.
No_of_Vote: La cantidad de votos recibida.
Se pide:

1) Procesar el archivo de texto generos.txt para crear un vector que contenga los nombres de los mismos (Únicamente los nombres y en el mismo orden en el que se encuentran en el archivo).

2) Procesar el archivo de texto series.csv para generar un vector de registros de series con el siguiente formato:

Poster_Link: link del poster de la serie en Amazon.
Series_Title: Título de la serie
Runtime_of_Series: año desde - año hasta de la serie, puede estar en blanco el año desde.
Certificate: Categoría de la serie, puede estar en blanco.
Runtime_of_Episodes: tiempo promedio de los capítulos.
Genre: Género de la serie
IMDB_Rating: Es el rating que va de 1 a 9,7
Overwiew: Es un resumen de la serie.
Star1, Star2, Star3 y Star4: NO LEVANTAR DEL ARCHIVO.
No_of_Vote: La cantidad de votos recibida.
Cumpliendo con las siguientes reglas:

a) En el vector, los registros de series deben quedar ordenados a medida que se agregan elementos, por el número de votos obtenidos, de mayor a menor.

b) No deben registrarse en el vector aquellas series que carezcan de duración, es decir que tengan el campo Runtime_of_Episodes en blanco.

c) Esa duración debe almacenarse como valor numérico entero, sin el "min" que aparece al final de cada una.

d) En lugar de guardar en el campo Genre la cadena que viene del archivo, se debe almacenar el código de ese género, que estaría representado por la posición o índice de ese género en el vector creado en el punto 1.

3) A partir del vector de series, mostrar aquellas series (a razón de una o dos líneas por cada una de ellas), que tengan una duración en minutos entre a y b siendo a y b valores que se deben ingresar por teclado. Al final del listado mostrar la duración promedio y ofrecer al usuario almacenar el listado en un nuevo archivo de texto con el formato del original, sin los campos omitidos.

4) Generar un vector de conteo en el que se pueda determinar la cantidad de series por cada uno de los géneros posibles, haciendo uso del vector de registros de series y del vector de géneros del punto 1. Mostrar los resultados visualizando el nombre del género en lugar del código representado.

5) Generar a partir del vector de conteo un archivo binario en el que se almacenen registros que contengan:

Número del género
Nombre del género
Cantidad
6) Mostrar el archivo generado en el punto 5.

7) Buscar si en el vector de series se encuentra una serie con el campo Series_Title igual a tit, siendo tit un valor que se carga por teclado. Si se encuentra incrementar su número de votos en uno. Si no se encuentra mostrar un mensaje.

 
