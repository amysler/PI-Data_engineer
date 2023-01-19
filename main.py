#Librerias a utilizar
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #Utilizado para generar el formato de texto de la pagina de inicio 
import pandas as pd

#Creacion de la APP
app = FastAPI(title = "Proyecto Data Engineer", description = "Henry's bootcamp data engineer proyect")

#Carga de base de datos con las transofrmaciones ya realizadas (Ver archivo ETL.ipynb)
general_df = pd.read_csv('Datasets/plataformas.csv')

#Creamos un directorio index con mensaje de bienvenida
@app.get("/", response_class=HTMLResponse)
async def index ():
    output = "¡Bienvenido a la interfaz de consultas del catálogo de películas y series de las plataformas Netflix, Amazon, Hulu y Disney! <br> Contamos con los siguiente 5 tipos de consultas: <br>Consulta 1: Cantidad de veces que aparece una keyword en el título de una películas/series en determinada plataforma <br>Consulta 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año <br>Consulta 3: Segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.<br>Consulta 4: Película que más duró según año, plataforma y tipo de duración<br>Consulta 5: Cantidad de series y películas para determinado rate<br><br>Para conocer el formato de busqueda, consulte el archivo README.md ubicado en el repositorio de GitHub"
    return output#f'Haga su consulta relacionada a las distitnas plataformas de Streaming'

#Se desarrollan las consutlas que fueron solicitadas por el cliente:

#Consulta 1: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/get_word_count/")
def get_word_count(plataforma:str, keyword:str):
    if plataforma == "amazon":
        df_gwc = general_df[general_df['ID'].str.contains("a")]
    elif plataforma == "dinsey":
        df_gwc = general_df[general_df['ID'].str.contains("d")]
    elif plataforma == "hulu":
        df_gwc = general_df[general_df['ID'].str.contains("h")]
    elif plataforma == "netflix":
        df_gwc = general_df[general_df['ID'].str.contains("n")]
    else:
        print("Try again")
    
    valor = df_gwc['title'].str.contains(keyword).value_counts()[True]

    return f'La palabra {keyword} aparece en {plataforma} {valor} veces'

#Ejemplo de consulta testeada localmente: http://127.0.0.1:8000/get_word_count/?plataforma=netflix&keyword=love
#Ejemplo de consulta testeada en deta:

#Consulta 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/")
async def get_score_count(plataform:str, score:int, year:int):
    df5 = general_df[(general_df["score"] > score ) & (general_df["release_year"] == year)]  #Filtro de busqueda por Score y Año
    if plataform == "netflix":
        df_gsc = df5[(df5["type"] == "movie") & (df5["ID"].str.findall("n"))]                #Genero un DF general con filtros especificos segun busqueda
    elif plataform == "amazon":
        df_gsc = df5[(df5["type"] == "movie") & (df5["ID"].str.findall("a"))]
    elif plataform == "hulu":
        df_gsc = df5[(df5["type"] == "movie") & (df5["ID"].str.findall("h"))]
    elif plataform == "disney":
        df_gsc = df5[(df5["type"] == "movie") & (df5["ID"].str.findall("d"))]
    else:
        print("Try again")

    return f'Peliculas de {plataform} del año {year} con puntaje {score}: {df_gsc.shape[0]}'

#Ejemplo de consulta testeada localmente: http://127.0.0.1:8000/get_score_count/?plataform=netflix&score=85&year=2010
#Ejemplo de consulta testeada en deta:

#Consulta 3: Segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/get_second_score/")
def get_second_score(plataforma:str):
    df_alfabetico = general_df[["title", "score", "type", "ID"]]                                    #Nuevo DF con columnas a utilizar 
    df_alfabetico = df_alfabetico[df_alfabetico["type"] =="movie"]                                  #Filtro para "pelicula"
    df_alfabetico = df_alfabetico.sort_values(["score", "title"], ascending = [False, True])        #Ordena por Score y Titulo
    if plataforma == "amazon":
        df_gss = df_alfabetico[df_alfabetico['ID'].str.contains("a")]
    elif plataforma == "hulu":
        df_gss = df_alfabetico[df_alfabetico['ID'].str.contains("h")]
    elif plataforma == "disney":
        df_gss = df_alfabetico[df_alfabetico['ID'].str.contains("d")]
    elif plataforma == "netflix":
        df_gss = df_alfabetico[df_alfabetico['ID'].str.contains("n")]
    else:
        print("No contamos con esta plataforma")

    segundo_titulo = df_gss.iloc[1, 0]
    segundo_score = df_gss.iloc[1, 1]

    return f'Segunda pelicula ordenada alfabeticamente por titulo con mayor score de la paltaforma {plataforma} es {segundo_titulo} con un score de {segundo_score}'

#Ejemplo de consulta testeada localmente: http://127.0.0.1:8000/get_second_score/?plataforma=amazon
#Ejemplo de consulta testeada en deta:




#Consulta 4: Película que más duró según año, plataforma y tipo de duración
@app.get("/get_longest/")
async def get_longest(plataforma:str, duracion:str, anio:int):
        if plataforma == "netflix":
                df1 = general_df[(general_df["type"] == "movie") & (general_df["release_year"] == anio) & (general_df["duration_type"] == duracion) & (general_df["ID"].str.findall("n"))]
        elif plataforma == "disney":
                df1 = general_df[(general_df["type"] == "movie") & (general_df["release_year"] == anio) & (general_df["duration_type"] == duracion) & (general_df["ID"].str.findall("d"))]
        elif plataforma == "hulu":
                df1 = general_df[(general_df["type"] == "movie") & (general_df["release_year"] == anio) & (general_df["duration_type"] == duracion) & (general_df["ID"].str.findall("h"))]
        elif plataforma == "amazon":
                df1 = general_df[(general_df["type"] == "movie") & (general_df["release_year"] == anio) & (general_df["duration_type"] == duracion) & (general_df["ID"].str.findall("a"))]
        else:
                print ("No contamos con la base de datos de dicha plataforma")
        
        df2 = df1[df1["duration_int"] == (df1["duration_int"].max())]
        #return (df2["title"])
        return f'Peliculas de {plataforma} del año {anio} con mayor duracion en {duracion}: {df2.iloc[0, 2]}'

#Ejemplo de consulta testeada localmnete: http://127.0.0.1:8000/get_longest/?plataforma=netflix&duracion=min&anio=2016
#Ejemplo de consulta testeada en deta:

#Consulta 5: Cantidad de series y películas por rate
@app.get("/get_rating_count/")
async def get_rating_count(rate:str):
    df1 = general_df[general_df["rating"] == rate]
    return f'Numero de series y peliculas con rating de {rate}: {df1.shape[0]}'

#Ejemplo de consulta testeada localmente: http://127.0.0.1:8000/get_rating_count/?rate=18%2B
#Ejemplo de consulta testeada en deta: