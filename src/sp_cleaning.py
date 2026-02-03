import pandas as pd
import numpy as np
from pathlib import Path


"""
      Procedemos a realizar un archivo soporte con todas las funciones que necesitamos para realizar
      un análisis y transformación de los datos. 

      Iremos poniendo y explicando las funciones para así quedar todo claro.  

"""



def drop_columns(df, cols):
    """
    Elimina columnas que no aporten información y valor a los datos
    """
    
    existing_cols = [c for c in cols if c in df.columns]
    df.drop(columns=existing_cols, inplace=True)
   


def comas(df):
    """
    Convierte columnas a numéricas reemplazando ',' por '.'
    """
    
    for col in df.select_dtypes(include = 'O').columns:
        df[col] = df[col].str.replace(',','.')
        try:
            df[col] = df[col].astype('float64')
        except:
            pass


def minus(df):
    """
    Cambia a minúscula el texto de todas las columnas categóricas

    """
   
    for col in df.select_dtypes(include = 'O').columns:
        df[col] = df[col].str.lower()


def normalizar_texto(df):
    """
    Sustituye los espacios, guiones o puntos por guión bajo "_".

    """
   
    for col in df.select_dtypes(include = 'O').columns:
        df[col] = df[col].str.replace('-', '_')
        df[col] = df[col].str.replace('.', '_')



def convierte_datetime(df, col):
    """
    Convierte a dtype datetime. Como los meses están en español, hay que pasar
    primero un diccionario para traducir los meses y luego hacer el cambio
    """

    meses = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio': 'July',
        'agosto': 'August',
        'septiembre': 'September',
        'octubre': 'October',
        'noviembre': 'November',
        'diciembre': 'December'
    }

    # pasar a minúsculas y traducir meses
    df[col] = (
        df[col]
        .str.lower()
        .replace(meses, regex=True)
    )

    df[col] = pd.to_datetime(df[col], format='%d-%B-%Y')




def boolean (df, col):
    """
    Convierte a valores booleanos
    """
    
    df[col] = df[col].astype('boolean')



def boolean_to_str(df, col_origen, col_destino, mapa={1: 'yes', 0: "no"}):
    """
    Creamos una columna nueva str a partir de una columna booleana
    """
    
    df[col_destino] = df[col_origen].map(mapa)
    




        










