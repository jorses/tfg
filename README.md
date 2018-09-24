# Trabajo de Fin de Grado
## Doble Grado en Ingeniería Informática y Matemáticas, Universidad Complutense de Madrid

### Primera parte : Explicación de Datasets Genéricos con Aprendizaje sobre Casos Específicos

El objetivo de la primera parte será implementar un programa capaz de analizar datasets pertenecientes a un
*ámbito de conocimiento* y presentar al usuario un informe con las principales características del mismo,
con un texto sencillo basado en plantillas y elementos gráficos (gráficos de barras, líneas temporales...) elegidos 
también por el programa.

La estructura modular abstracta del programa, creada para permitir una *aproximación general a cualquier ámbito de conocimiento* y almacenar información sobre los ámbitos, será la siguiente:

#### Almacenamiento de la información (Aprendizaje)

Tendremos un módulo encargado de *almacenar la información* de los dominios que conoce el programa, y para simplificar
estos serán reconocidos según los nombres de las columnas del dataset introducido.

Este módulo será cargado por el programa al empezar y le dará la *información sobre el dominio que sea relevante para
realizar el análisis*. Esto incluye la información extra que proporcione el usuario como relevante.

Cuando el usuario señale información como importante esta será guardada junto con la información referente a este
dominio y será cargada en posteriores ejecuciones. También dispondrá de un módulo básico para datasets de los que no posee información anterior y que permitirá realizar un primer análisis básico.

#### Análisis de datasets

Este módulo será el encargado de *realizar el análisis sobre el dataset* que corresponda,
recibiendo como entrada el dataset y el conocimiento sobre él del que se dispone, lo analizará y
generará los datos relevantes para realizar el informe, teniendo como salida
una *representación abstracta del informe*, seguramente en formato JSON o similar.

Este módulo tendrá en cuenta los tipos de las columnas, el conocimiento del dominio y las particularidades
del dataset y de los individuos frente a este para componer el modelo abstracto que mejor lo representará
para un usuario experto.

#### Generación de informes

El módulo recibirá la salida abstracta del módulo de análisis y se encargará de parsearlo a un formato
presentable como informe, montar las gráficas etc, pero no tomará ninguna decisión sino que simplemente 
maquillará el contenido del informe abstracto para que sea presentable, en función a si el usuario es experto
o no (aunque la base abstracta sea la misma, asumiendo que el conocimiento necesario para el usuario básico
estará contenido en el necesario para un usuario experto).

La parte de texto se realizará por plantillas para simplificar esta parte, y todos los aspectos como la elección
de los colores o el tipo de gráficas a usar estarán también determinados por la representación abstracta del análisis.

La elección del tipo de informe estará en principio determinada por un parámetro introducido al ejecutar el programa.

#### Main

Se creará un módulo que aglutinará todos y hará uso de ellos según un flujo específico de programa por concretar.

#### Interacción con el usuario

El usuario experto podrá señalar patrones interesantes que no han sido recogidos en el informe general.
Una primera aproximación es dejar señalar o bien individuos individuales que resultan interesantes,
o bien columnas que tienen unas características diferentes a las esperadas.

Cuando el usuario experto señale algo se le preguntará de una manera acotada qué razón le ha llevado a hacerlo
(por ejemplo, qué distribución esperaba en una columna numérica que no es la esperada o qué aspectos de ese
individuo en concreto resultan interesantes), y después se añadirá este conocimiento al conocimiento sobre
este tipo de datasets para tenerlo en cuenta en futuros informes.

También se podrán ver las características de un usuario en comparación con el resto si el usuario lo pide sin
guardar ningún tipo de información.


### Segunda Parte : Explicación del comportamiento de modelos de Machine Learning de Caja Negra

El objetivo de esta parte es poder generar informes similares a los de la primera pero especializados
para un tipo de dominio específico y para un tipo de análisis sobre ese dominio.

Todos los módulos anteriores funcionarán igual pero añadiremos uno nuevo, el de análisis de modelos,
y la información generada por este se añadirá al módulo de Almacenamiento de la Información dentro de su
dominio de conocimiento (caso específico) correspondiente, y se adaptará la Generación de Informes para
especializarla a estos casos.

En principio nos centraremos en explicar modelos predictivos tipo RandomForest, CatBoost o XgBoost enfocados
hacia una variable y que contengan un elemento temporal.

#### Análisis de modelos

Este módulo trabajará de manera análoga al análisis de datasets, de una forma aún por concretar, pero su objetivo
será trasladar a un modelo abstracto el resumen de funcionamiento del modelo, representando no por qué ha tomado las
decisiones que ha tomado sino centrándose en resumirlas y exponerlas de una forme que dote de sentido al modelo
para el usuario experto.

### Especificaciones técnicas

Se realizará la totalidad del trabajo en Python haciendo uso de las frameworks de Pandas y Sklearn, entre otras.
