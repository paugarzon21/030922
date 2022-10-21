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
from pandas.io import gbq


#root_dir=Path('.').resolve()
bucket='gs://pgarzon_llamadas123'

def get_data(file_name):
    data_dir="raw"
    file_path=os.path.join(bucket, "data",data_dir, file_name) 
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
    data[col]=pd.to_datetime(data[col],errors='coerce')
    lista_fechas=list()
    for fecha in data[col]:
        new_fecha=pd.to_datetime(fecha, errors='coerce')
        lista_fechas.append(new_fecha)
    data[col+'CORREGIDO']=lista_fechas
    return data

def save_data(dataclean):
    #out_name = 'limpieza_' + filename
    out_name="limpieza_final.csv"
    out_path = os.path.join(bucket, 'data', 'processed', out_name)
    dataclean.to_csv(out_path)
    dataclean.to_gbq(destination_table="LLAMADAS123.QUERY_TO_DASH",
                    project_id="especializacionbigdata20222",
                    if_exists="replace")

def main():
    
    data_complete=pd.DataFrame()
    vector_file_name= ["llamadas123_julio_2022.csv", "llamadas123_agosto_2022.csv","llamadas123_junio_2022.csv","datos_llamadas123_mayo_2022.csv","datos_abiertos_enero_2022.csv","datos_abiertos_febrero_2022.csv","datos_abiertos_marzo_2022.csv","datos_abiertos_abril_2022.csv","llamadas_123_abril2021.csv","llamadas_123_agosto2021.csv","llamadas_123_-enero2021.csv","llamadas_123_febrero2021.csv","llamadas_123_julio2021.csv","llamadas_123_marzo2021.csv","llamadas_123_mayo2021.csv","llamadas_123_noviembre_2021.csv","llamadas_123_octubre_2021.csv","llamadas_123_septiembre2021.csv","llamadas123_agosto_2022.csv","llamadas123_junio_2022.csv"]
    for i in range (len(vector_file_name)):
        data = get_data(vector_file_name[i])
        data = delete_duplicates(data)
        data = delete_nulls_string(data, col='UNIDAD')
        data = delete_nulls_int(data, col='EDAD')
        data = standar_time(data, col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL')
        #data = standar_time(data, col='RECEPCION')
        data_complete=data_complete.append(data)
        
    save_data(data_complete)
  
if __name__=='__main__':
    main()
    