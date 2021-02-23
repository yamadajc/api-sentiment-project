# Api Sentiment Project





![portada](/images/portada.jpeg)


## Introducion:
En los últimos tiempos, los concursos de talentos se han convertido en un género notable de telerrealidad. Tanto famososo como anonimos de todas las edades han ocupando nuestras horas muertas con sus pasiones, penas y emociones. 

Toda esta generacion de sentimientos acaba registrada para siempre en plataformas y distintos medios de la informacion. Y esta informacion se puede cuantificar y medir.  

# Objetivos: 
Los objetivos de este proyecto consisitiran en generar una [API](https://es.wikipedia.org/wiki/Interfaz_de_programaci%C3%B3n_de_aplicaciones) usando [Flask](https://es.wikipedia.org/wiki/Flask) en la que los usuarios podran realizar consultas y agregar frases hechas por participates del "TalentShow" culinario mas duro de la television. 

Finalmente se realizara un analisis comparativo entre lo dicho en el programa y declaraciones hechas en una red social. De esta forma se podra catalogar las frases dichas por algunos de los personajes en función de la connotación positiva o negativa y si en funcion del medio cambian su percepcion o no. 


# Api

"ApiSiente" es una API que recopila frases de personajes televisivos de un talente culinario. Estas frases podran ser una transcripcion obtenidad directamente de la emision del show televisivo o bien de publicacion de una red social. 

Toda esta informacion se encuentra almacenada en una base de datos llamada "Aidos"  [MongoDB ](https://es.wikipedia.org/wiki/MongoDB) y se compone de tres colleciones (masterchef, character y twitter ). 

# Endpoints

Los enpoints especifican donde se encuentra la informacion y como se puede acceder a la misma. 

> Acceso a los distintos listados de las colleciones:  

/masterchef

/character

/twitter
~~~
http://127.0.0.1:5000/masterchef
~~~


> Agregar personajes, frase y tweet:
//new
~~~~
http://127.0.0.1:5000/character/new?name=Jeancha&role=participante
~~~~
- para insertar un nuevo personaje es obligatorio especificar el *name* 
-  para insertar una nueva frase  es obligatorio especificar el *name* y el *phrase*
-  para insertar un nuevo tweet es obligatorio especificar el *name* y el *tweet*


> obtencion detallada de personajes, frase y tweet:

//details
~~~~
"http://127.0.0.1:5000/masterchef/details?id=6031ccdcf1264eede86ab56d"
~~~~

Para mayor informacion consultar el note book **notebook-API-test**

# Analisis de connotación

El análisis de sentimientos, también conocido como minería de opinión, se trata de una tarea de clasificación masiva de documentos de manera automática, que se centra en catalogar los documentos en función de la connotación positiva o negativa del lenguaje ocupado en el mismo.

El proceso descrito a continuacion puede encotrarse en el notebook **sentiment-analysis.ipynb**

> Proceso 

1. Importacion de datos de la API *metodo get* 
2. Tokenizacion de los datos *RegexpTokenizer*
3. Traducion de los datos con *spanish_string.translate* 
4. Discriminacion de palabras superfluoas con *stopwords*
5. Catalogacion de sentimiento con *NLTK*

# Resultados 

Los resultados arrojados por el analisis indican una conotacion positiva para los personajes del estudio. Siendo mas positiva en todos los participantes menos para uno que reduce su puntuacion considerablemente en la red social.
![tabla](/images/tabla.png)


analisis en twitter
![twitter](/images/twitter.png)



analisis en tv
![tv](/images/tv.png)



