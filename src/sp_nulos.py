import pandas as pd
import numpy as np
from pathlib import Path

def copy_df(df):
    """
    Devuelve una copia profunda del dataframe
    """
    return df.copy(deep=True)


def resumen_nulos(df):
    """
    Devuelve porcentaje de nulos por columna
    """
    return df.isnull().mean().mul(100).round(2)


def tratar_pdays(
    df,
    col="pdays",
    nueva_col="pdays_clean",
    label_col="pdays_label"
):
    """
    - Sustituye 999 por NA
    - Mantiene columna numérica nullable (Int64)
    - Crea columna de texto opcional
    """

    df[nueva_col] = (
        df[col]
        .replace(999, pd.NA)
        .astype("Int64")
    )

    df[label_col] = np.where(
        df[nueva_col].isna(),
        "sin contacto previo",
        df[nueva_col].astype(str)
    )

    return df


def imputar_numericas(df, cols, metodo="median"):
    """
    Imputa columnas numéricas
    """
    for col in cols:
        if metodo == "median":
            df[col] = df[col].fillna(df[col].median())
        elif metodo == "mean":
            df[col] = df[col].fillna(df[col].mean())
    return df


def imputar_categoricas(df, cols, valor="unknown"):
    """
    Imputa columnas categóricas
    """
    for col in cols:
        df[col] = df[col].fillna(valor)
    return df

