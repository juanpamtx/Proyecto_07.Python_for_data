# Proyecto de Análisis Exploratorio de Datos (EDA) - Marketing Bancario #

## **Descripción del proyecto** ##

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre una campaña de marketing de una entidad bancaria. El objetivo es identificar patrones y factores que influyen en la conversión de clientes (suscripción a un depósito a plazo).

El análisis incluye limpieza de datos, exploración de variables sociodemográficas, comportamiento de contacto y análisis de variables temporales.


## **Tecnologías aplicadas** ##

- **Python 3.13**
    - Jupyter Notebook: para todo el desarrollo
- **Pandas**: manipulación y limpieza de datos
- **NumPy**: operaciones numéricas
- **Matplotlib / Seaborn**: visualización de datos
- **Visual Studio Code**: entorno de trabajo


## **Limpieza y preparación de datos**##

Partimos de dos archivos: 

**1. bank-additional**

Es un archivo csv con 43000 filas y 24 columnas en el que se muestran las llamadas telefónicas a los clientes para saber si iban a contratar el producto (depósito a plazo bancario) o no. Hay ocasiones que se requería más de una llamada al mismo cliente. 

![Imagen información archivo: bank-additional](./Imágenes/bank-additional_informacion)

**2. customer-details**

Es un archivo excel con 20115 filas y 7 columnas en el que nos da información sobre las características demográficas y comportamiento de compra de los clientes. Presenta 3 hojas correspondientes a diferentes años.

![Imagen información archivo: customer-details](./Imágenes/customer-details_informacion)


Se realizaron las siguientes tareas:

- Eliminación de valores duplicados

- Tratamiento de valores desconocidos (unknown)

- Conversión de variables categóricas a formato adecuado

- Creación de variables derivadas:

    - y_bin: variable objetivo binaria (0 = no, 1 = sí)

    - Agrupaciones de edad, duración de llamada, campañas previas, etc.


## **Análisis Exploratorio de datos (EDA)** ##

**Perfil del cliente**

Se han analizado las siguientes variables: 
- Edad
- Ocupación
- Nivel educativo
- Estado civil

**Variables de contacto**

- Duración de la llamada
- Número de contactos durante la campaña
- Días desde el último contacto (pdays)

Se ha detectado que:
- Las llamadas más largas tienen mayor probabilidad de conversión
- Contactos recientes aumentan la tasa de éxito

**Variables temporales**

- Mes y año de contacto
- Estacionalidad en la conversión

**Consideraciones estadísticas**

Durante el análisis se detectó que una agregación incorrecta de la variable pdays podía inducir a conclusiones erróneas. Por ello, los grupos se construyeron a partir de la variable numérica original para evitar sesgos.


## **Resultados clave** ##

- La conversión aumenta con llamadas de mayor duración
- Clientes contactadas recientemente convierten más que los que no han sido contactados.
- Determinados perfiles (mayor educación y edad media) presentan mayor probabilidad de conversión.
- Un excesivo número de contactos reduce la probabilidad de éxito


## **Conclusiones** ##

El análisis muestra que la estrategia de marketing debe centrarse en:

- Contactar a clientes con frecuencia moderada

- Priorizar clientes con contacto reciente

- Optimizar la duración de las llamadas

- Segmentar por perfil sociodemográfico

Estos insights pueden mejorar significativamente la tasa de conversión de campañas futuras.