"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(columns= df.columns[0], inplace=True)

    for i in ['tipo_de_emprendimiento' , "barrio" ,'comuna_ciudadano']:
        df[i] = df[i].fillna(df[i].mode())

   #

    variables_categ = ['sexo','tipo_de_emprendimiento','idea_negocio','barrio', df.columns[-1]]
    for i in variables_categ:
        df[i] = df[i].str.lower()

    variables_num = ['estrato','comuna_ciudadano','monto_del_credito']
    for i in variables_num:
        df[i] = pd.to_numeric (df[i],errors= 'coerce')

    df['monto_del_credito'] = df['monto_del_credito'].fillna(df['monto_del_credito'].mean())

    df.drop_duplicates(keep = 'last', inplace= True)
 

    return df

  
