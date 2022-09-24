#pesudo codigo
#main()
#   data = get_data(filename)
#   reporte = generate_report(data)
#   save_data(reporte)

from fileinput import filename
from pathlib import Path
import os
import pandas as pd 

root_dir=Path('.').resolve()

def get_data(file_name):
    data_dir="row"
    file_path=os.path.join(root_dir, "data",data_dir, file_name) 
    data=pd.read_csv(file_path,sep=";", encoding="latin-1")
    print('get_data')
    print('la tabla contiente', data.shape[0], 'filas',data.shape[1], 'columas' )
    return data

def generate_report(data):
    dict_reporte= dict()

    for col in data.columns: #¿porque data.columnas?
        valores_unicos=data[col].unique()
        n_valores_unicos=len(valores_unicos)
        dict_reporte[col]=n_valores_unicos
    
    reporte=pd.DataFrame.from_dict(dict_reporte, orient='index')
    reporte.rename({0:"conteo"}, inplace=True,axis=1)
    return reporte

def save_data(reporte,filename):
    out_name = 'reporte_'+ filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path)
    
def main():
    file_name="llamadas123_julio_2022.csv"
    data = get_data(file_name)
    reporte= generate_report(data)
    save_data(reporte, file_name)
    print("hola")


if __name__=='__main__':
    main()
