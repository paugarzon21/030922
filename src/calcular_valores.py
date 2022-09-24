#1. Librerias
import numpy as np
import argparse


#2. Funciones

def calcular_suma(lista_numeros,verbose=1):
    """calcula la suma de los valores de una lista de numeros

    Args:
        lista_numeros (list): lista de numeros enteros

    Returns:
        int: suma
    """
    suma=np.sum(lista_numeros)
    if verbose==1:
        print('calcular_suma')
        print('suma',suma)
    else:
        pass

    return suma

def calcular_valores_centrales(lista_numeros,verbose=1):
    """ calcula los valores centrales de una lista de numeros

    Args:
        lista_numeros (list): lista de numeros enteros

    Returns:
        tuple: media, desviacion estandar
    """
    media=np.mean(lista_numeros)
    desviacion_estandar=np.std(lista_numeros)

    if verbose==1:
        print('calcular_valores_centrales')
        print('media', media)
        print('desviacion estandar', desviacion_estandar)
    else:
        pass

    return media, desviacion_estandar

def calcular_extremos(lista_numeros,verbose=1):
    """calcula el valor minimo y maximo de una lista de valores

    Args:
        lista_numeros (list): lista de numeros enteros

    Returns:
        tuple: minimo,maximo
    """
    minimo=np.min(lista_numeros)
    maximo=np.max(lista_numeros)
    if verbose==1:
        print('calcular_extremos')
        print('valor minimo', minimo)
        print('valor maximo', maximo)
    else:
        pass
    return minimo, maximo

def calcular_valores(lista_numeros,verbose=1):
    suma= calcular_suma(lista_numeros,verbose)
    media, desviacion_estandar= calcular_valores_centrales(lista_numeros,verbose)
    minimo, maximo=calcular_extremos(lista_numeros,verbose)
    return suma, media, desviacion_estandar, minimo, maximo

def main():   
    #El script se prepara para recibir argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", type=int, default=1, help="para decidir si imprime informacion")
    args= parser.parse_args() #activar argumentos

    verbose = args.verbose

    lista_numeros=[1, 5,8,3,45,93]
    suma, media, desviacion_estandar, minimo, maximo=calcular_valores(lista_numeros,verbose)
    print("DONE!!")

#3. main al final. Revisar que es__name__
if __name__=='__main__':
    main()