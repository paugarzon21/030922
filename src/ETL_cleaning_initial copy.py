#pesudo codigo
#main()
#   data = get_data(filename)
#   data_1 = delete_duplicates(data)
#   data_2=delete_null(no_duplicates, column)
#   data_3=convert_date_time(no nulls)
#   final_data=convert_num=(date_time)

from pathlib import Path
import os
import pandas as pd
import numpy as np
from dateutil.parser import parse


root_dir=Path('.').resolve()

def get_data(file_name):
    data_dir="row"
    file_path=os.path.join(root_dir, "data",data_dir, file_name) 
    data=pd.read_csv(file_path,sep=";", encoding="latin-1")
    return data

def delete_duplicates(data):
    data_1=data.drop_duplicates()
    data_1.reset_index(inplace=True, drop=True)
    return data_1

def delete_nulls_string(data_1, col):
    data_1[col].fillna('SIN_DATO', inplace= True)
    return data_1

def delete_nulls_int(data_2, col):
    data_2[col].replace({'SIN_DATO': np.nan}, inplace= True)
    f= lambda x:np.nan if pd.isna(x) else int(x)
    data_2[col]=data_2[col].apply(f)
    return data_2

def standar_time(data_3, col):
    lista_fechas=list()
    for fecha in data_3[col]:
        try:
            new_fecha=parse(fecha)
        except Exception as e:
            new_fecha=pd.to_datetime(fecha, errors='coerce')
        lista_fechas.append(new_fecha)
    
    data_3[col+'CORREGIDO']=lista_fechas
    return data_3

def main():
    file_name="llamadas123_julio_2022.csv"
    data = get_data(file_name)
    data_1= delete_duplicates(data)
    col1='UNIDAD'
    data_2=delete_nulls_string(data_1, col1)
    col2='EDAD'
    data_3=delete_nulls_int(data_2, col2)
    col3='FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
    data_4=standar_time(data_3, col3)
    col4='RECEPCION'
    data_5=standar_time(data_4, col4)
    print(type(data_5))
    print(data_5['EDAD'])


if __name__=='__main__':
    main()