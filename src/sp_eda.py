import pandas as pd


def eda_preliminar(df1):

    """ Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame.
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas
    - Distribución de valores para columnas categóricas.

    Parameters:
    df1 (pd.DataFrame): DataFrame a analizar.

    Returns:
    None

    """
    
    display(df1.sample(5))

    print('--------')

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df1.shape[0]} filas y {df1.shape[1]} columnas')

    print('--------')
    
    print('INFO')

    display(df1.info())

    print('--------')
    
    print('NULOS')

    display(df1.isnull().mean()*100)

    print('--------')
    
    print('DUPLICADOS')

    print(f'Tenemos un total de {df1.duplicated().sum()} duplicados')

    print('--------')

    print('FRECUENCIAS CATEGÓRICAS')
     
    for col in df1.select_dtypes(include= 'object').columns:
        print(col.upper())
        print(df1[col].value_counts())
        print('--------')