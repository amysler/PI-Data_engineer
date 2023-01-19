<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER

## *Henry´s bootcamp* 


#### Problemática:
- **Simulación** de un equipo de data empresarial donde el área de análisis de datos le solicita al de **Data engineering**  que, utilizando un grupo de [datasets](https://github.com/amysler/Proyecto_individual_data_engineer-Henry_bootcamp-DTS06/tree/main/Datasets) provistos, realice las **transformaciones requeridas** y posteriormente **disponibilicen los datos** mediante la elaboración y ejecución de una **API**

#### Rol del desarrollador:
- Data engineer

<hr> 

### Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:

`EXTRACCIÓN DE DATOS`


1. Importación de la librería pandas para el manejo de dataframes
2. Ingesta de datos (Archivos .csv provistos por el cliente) en respectivos dataframes (Disney, Amazon, Hulu y Netflix)
3. Análisis exploratorio de los distintos datasets para conocer sus características principales
   
`TRANSFORMACIONES`

1. Generación del campo ID
2. Reemplazo valores nulos del campo Rating por "g"
3. Conversión de date_added al formato adecuado (AAAA-mm-dd)
4. Conversión de campos de texto a minuscula utilizando el metodo "applymap"
5. Separación de columna "duration" en dos ("duration_int" y "duration_type")
6.  En nueva columna "duration_type" unificar season y seasons en "season"
7.  Unificar 4 plataformas a través de la función “concat” en un dataframe único "general_df" facilitando el código de las consultas a desarrollar
8.  Cambio tipo de dato "duration_int" a integer
9.  Exportar CSV final (general_df) con todas las transformaciones
##### *Nota: La carga del CSV final se realiza directamente en el archivo main.py*
  
  <hr> 

### Desarrollo de las consultas solicitadas:

`CONSULTAS A REALIZAR`

1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
3. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
4. Película que más duró según año, plataforma y tipo de duración
5. Cantidad de series y películas por rating

Se desarrolla el código de las funciones que responden a las consultas solicitadas por el cliente

<hr>

### Proceso de disponibilización de los datos utilizando FastAPI (framework que permite construir APIs con Python) y Deta para realizar el deploy: 
1. Generación de archivo main.py (donde desarrollar el script) y otro requirements.txt (donde alojar los requerimientos para la API)
2. Importación de las librerías a utilizar
3. Declaración de la creación de la API 
4. Declaración de la ruta de acceso para la base de datos (general_df)
5. Creación de un directorio índex con mensaje de bienvenida a la interfaz
6. Desarrollo de las consultas con formato:
   
```ruby
@app.get("/tipo_de_consulta/")
def tipo_de_consulta(variable1:tipo_de_dato, variable"n":...):
  desarrollo_de_la_funcion
```

7. Creacion de una cuenta en [Deta](https://web.deta.sh/ "Creacion de usuario en deta")
8. Instalacion del Deta CLI en consola de forma local mediante comando "iwr https://get.deta.dev/cli.ps1 -useb | iex"
9. Comprobación de la correcta instalacion con "deta --help"
10. Login en deta a traves de la consola mediante comando "deta login"
11. Ubicado en el path de la carpeta donde se encuentra la API desarrollada se procede a la creacion de un micro mediante el comando "deta new"
12. Una vez creado el micro, se realizan las pruebas correspondientes a las consultas con el endpoint URL provisto por deta.

<hr>

### Instrucciones para la utilización de la herramienta: 
`Ingrese al siguiente URL: https://qlprmb.deta.dev`

Segun lo consulta que quiera solicitar, debera agregarle a continuación del URL la **consulta y variables** con el siguiente **formato**:
- Consulta 1: .../**get_word_count/?plataforma=netflix&keyword=love**
- Consulta 2: ...**/get_score_count/?plataform=netflix&score=85&year=2010**
- Consulta 3: ...**/get_second_score/?plataforma=amazon**
- Consulta 4: ...**/get_longest/?plataforma=netflix&duracion=min&anio=2016**
- Consulta 5: ...**/get_rating_count/?rate=18%2B**

Las variables pueden ser reemplazadas en el formato de consulta por el elemento deseado: 
- **Plataforma**: **netflix, disney, hulu, amazon**
- **Keyword**: puede ser reemplazado por cualquier termino deseado (la busqueda se realiza en el "titulo" de peliculas)
- **Score**: puntaje determinado de movie/serie
- **Year**: año de estreno de movie/serie
- **Duracion**: tipo de duracion en **min** o **season**
- **Rate**: rate de determinada pelicula utilizando **g** (general), **7+**, **13+**, **16+**, **18+** (*Nota: el simbola "+" debe ser reemplazado por "%2B" - Ejemplo: 18+ = 18%2B*)

<hr> 

#### Ejemplos de busquedas: 
- **Consulta 1:** https://qlprmb.deta.dev/get_word_count/?plataforma=netflix&keyword=love
- **Consulta 2:** https://qlprmb.deta.dev/get_score_count/?plataform=netflix&score=85&year=2010
- **Consulta 3:** https://qlprmb.deta.dev/get_second_score/?plataforma=amazon
- **Consulta 4:** https://qlprmb.deta.dev/get_longest/?plataforma=netflix&duracion=min&anio=2016
- **Consulta 5:** https://qlprmb.deta.dev/get_rating_count/?rate=18%2B

##### *Nota: Para conocer mas detalles tecnicos acerca de las funciones y sus respectivos parametros puede ingresar a https://qlprmb.deta.dev/docs*


#### [Link a video explicativo confeccionado para equipo de data analytics](https://www. "Proyecto Individual data engineer - Henry's bootcamp")

<hr> 

#### Tecnologías utilizadas:
- Visual studio code
- Python
- Deta cloud
- FastApi

  
<img src="https://visualstudio.microsoft.com/wp-content/uploads/2019/06/vs-code-responsive-01.svg" width="50"/><img src="https://www.python.org/static/community_logos/python-logo.png" width="150"/><img src="https://raw.githubusercontent.com/deta/.github/main/profile/deta_logo_dark.svg" width="250"/><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="150"/>