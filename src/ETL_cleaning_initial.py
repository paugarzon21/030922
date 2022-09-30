#pesudo codigo
#main()
#   data = get_data(filename)
#   data_1 = delete_duplicates(data)
#   data_2=delete_null_string(data_1, column)
#   data_3=convert_date_time(no nulls)
#   final_data=convert_num(date_time)
#   save_data(final_data)

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
    data=data.drop_duplicates()
    data.reset_index(inplace=True, drop=True)
    return data

def delete_nulls_string(data, col):
    data[col].fillna('SIN_DATO', inplace= True) #preguntar si se puede sin pedir columna. 
    return data

def delete_nulls_int(data, col):
    data[col].replace({'SIN_DATO': np.nan}, inplace= True)
    f= lambda x:np.nan if pd.isna(x) else int(x)
    data[col]=data[col].apply(f)
    return data

def standar_time(data, col):
    lista_fechas=list()
    for fecha in data[col]:
        try:
            new_fecha=parse(fecha)
        except Exception as e:
            new_fecha=pd.to_datetime(fecha, errors='coerce')
        lista_fechas.append(new_fecha)
    
    data[col+'CORREGIDO']=lista_fechas
    return data

def save_data(dataclean,filename):
    out_name = 'limpieza_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    dataclean.to_csv(out_path)

def main():
    file_name="llamadas123_julio_2022.csv"
    data = get_data(file_name)
    data= delete_duplicates(data)
    data=delete_nulls_string(data, col='UNIDAD')
    data=delete_nulls_int(data, col='EDAD')
    data=standar_time(data, col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL')
    data=standar_time(data, col='RECEPCION')
    save_data(data, file_name)

if __name__=='__main__':
    main()