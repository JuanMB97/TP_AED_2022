Una empresa de desarrollo de software de nuestra ciudad nos encarga un sistema para la gestión de Proyectos de Software. De cada proyecto se conoce:

Número de proyecto
Título
Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
Cantidad de líneas de código
Se pide desarrollar un programa en dos módulos: uno de ellos debe contener la definición de la clase del regisstro y las funciones básicas que permitan manejar un registro, y el otro debe contener el programa principal, que debe estar controlado por un menú de opciones para permitir hacer lo siguiente:

1) Cargar proyectos: La generación de n proyectos de software cargados en un arreglo de registros. Para ello se pueden generar los datos totalmente aleatorios o bien contar con proyectos completos precargados e ir seleccionando aleatoriamente entre los mismos. Cada vez que selecciona esta opción durante la ejecución se agregarán datos al arreglo, sin eliminar los que ya estaban cargados. El número del proyecto no debe repetirse dentro del arreglo.

2) Listar proyectos: Mostrar todos los proyectos contenidos en el arreglo, pero ordenados alfabéticamente por título. Cada proyecto debe ocupar un máximo de dos líneas en pantalla y en lugar de mostrarse el identificador del lenguaje se debe mostrar su nombre.

3) Actualizar proyecto: Buscar si existe un proyecto con número x, siendo x un valor que se ingrese por teclado. Si existe, se debe permitir modificar su cantidad de líneas de código y la fecha de actualización (recuerde que debe cumplir con el formato dd-mm-yyyy). Si no existe, debe indicar con un mensaje.

4) Resumen por lenguaje: Calcular la cantidad de líneas de código acumuladas por lenguaje. Mostrar los resultados teniendo en cuenta que se debe visualizar el nombre del lenguaje en lugar del código. 

5) Resumen por año:  Calcular la cantidad de proyectos por año de actualización, considerando los años entre 2000 y 2022 inlcuidos ambos. Mostrar los resultados sólo de los años que tengan algún proyecto de software.

6) Filtrar lenguaje: Mostrar los proyectos de software ordenados por número de proyecto de manera ascendente, del lenguaje ln, siendo ln un valor ingresado por teclado.

7) Productividad: A partir del resultado obtenido en el punto 5, determinar el año con mayor cantidad de proyectos actualizados, considerando mostrar todos los años si fuera más de uno con dicha cantidad.
