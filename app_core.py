import numpy
import multiprocessing
from multiprocessing import Pool,Process
def calcular_factorial(n):
    print('Calculando factorial..')
    resultado=1
    for i in range(1,n+1):
        resultado=resultado*i
    print('Resultado factorial: ',resultado)
def calcular_multiplicacion(lista):
    print('Calculando multiplicacion')
    resultado=1
    for i in lista:
        resultado=resultado*i
    print('Resultado factorial: ',resultado)
def main():
    proceso1=multiprocessing.Process(calcular_factorial(10))
    proceso2=multiprocessing.Process(calcular_multiplicacion([2,4,6,10,5]))
    proceso1.start()
    proceso2.start()
    proceso1.join()
    proceso2.join()
    print('Tareas completadas')
main()
