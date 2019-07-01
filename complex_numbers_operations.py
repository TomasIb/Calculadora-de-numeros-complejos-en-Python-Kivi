#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy #IMPORTACION DE LIBRERIA PARA ARREGLOS
import sys #IMPORTACION DE LIBRERIA DEL SISTEMA, USADA PARA LEER EL ARGUMENTO

def create_complex(x): #CREA NUMEROS COMPLEJOS EN BASE A UNA LISTA
    complex_num = []
    for a in x: #SE RECORRE LA TUPLA DE NUMEROS
        real_num = int(a[0]) #OBTIENE EL VALOR REAL DE LA TUPLA
        imaginary_num = int(a[2]) #OBTIENE EL VALOR IMAGINARIO
        complex_num.append(complex(real_num,imaginary_num)) # CREA EL NUMERO COMPLEJO Y LO GUARDA
    return complex_num #RETORNA EL NUMERO COMPLEJO


def __mul__(numbers,multiplicated_list): #MULTIPLICA LA LISTA DE NUMEROS COMPLEJOS A MULTIPLICAR
    multiplication_tuples = []

    for char in numbers: # SE RECORRE LA MULTIPLICACION

        if char =='*': #SI SE ENCUENTRA *, SE SEPARA
            splited = numbers.split('*')
            if (len(splited) > 2 and splited not in repeted): # SI NO SE HA LEIDO Y SI ES UNA TUPLA

                repeted.append(splited) # SE GUARDA EN LOS LEIDOS
                multiplication_tuples =  multiplication_tuples + splited #SE CONCATENA A LAS TUPLAS

            if(len(splited)<=2): # SI ES MEJOR A 2 NO SE GUARDA EN REPETIDOS
                multiplication_tuples = multiplication_tuples + splited

    complex_num = create_complex(multiplication_tuples) # SE OBTIENE EL NUMERO COMPLEJO DE LA TUPLA
    if(complex_num != []): # SI EXISTEN MULTIPLICACIONES
        multiplicated_list.append(numpy.prod(complex_num)) # REALIZA UNA MULTIPLICACION  DE TODOS LOS NUMEROS COMPLEJOS EN LA LISTA
    return multiplicated_list #RETORNA LA LISTA DE MULTIPLICACIONES


def __sum__(init_numbers): #RECIBE LA LISTA DE NUMEROS Y RETORNA LOS VALORES A SUMAR
    for s in init_numbers: #RECIBE LA LISTA CON SEPARACION DE SUMAS
        for a in s:
            if a in symbol_m: #SI SE ENCUENTRA UNA MULTIPLICACION
                init_numbers.remove(s) #SE REMUEVE
                break
    sum_list = create_complex(init_numbers) #SE CREA NUMEROS COMPLEJOS DE LOS QUE QUEDAN
    return sum_list # SE RETORNA LA LISTA DE NUMEROS COMPLEJOS A SUMAR


def print_result(multiplicated_list,sum_list,expresion): #RECIBE LA EXPRESION INICIAL, LOS VALORES MULTIPLICADOS Y LOS SUMADOS
    print ("Expresion: (",expresion," )")
    print("")
    print("Multiplicaciones: ",multiplicated_list) # IMPRIMER LA LISTA DE MULTIPLICACIONES
    print("Sumas: ",sum_list) #IMPRIME LA LISTA DE SUMAS
    print("")
    res = sum_list + multiplicated_list #SE CONCATENA LA LISTA DE VALORES A SUMAR CON LOS MULTIPLICADOS
    print ("Resultado: ",sum(res)) # SE SUMA TODO
    print("")

def get_multiplicated_list(init_numbers):#RECIBE LA LISTA INICIAL PARA GENERAR LAS MULTIPLICACIONES
        multiplicated_list = []
        for x in init_numbers: #SE RECORRE LA LISTA SEPARADA
            for char in x: #SE ANALIZAN LOS CARACTERES HASTA ENCONTRAR UNA *
                if char in symbol_m: # SI SE ENCUENTRA
                    multiplicated_list = __mul__(x,multiplicated_list) #SE ENVIA EL VALOR Y LA LISTA DE MULTIPLICACIONES
        return multiplicated_list # SE RETORNAN LAS MULTIPLICACIONES

def split_sum(argument): #RECIBE LA LECTURA INICIAL Y SEPARA LA SUMA
    for a in argument: #SE RECORRE EL ARGUMENTO INGRESADO
        init_numbers = argument.split('+') #SE SEPARAN LAS SUMAS
    return init_numbers #RETORNA LA LISTA


def split_block(argument):
    
    for a in argument:
        init_expression = argument.split('[')
        x_expression = init_expression + argument.split(']')
    
    
    init_expression = x_expression + init_expression
        
    return init_expression

if __name__ == "__main__":
    # try:

        expression = input("Ingrese la expresion: ")
        print(expression)
        

        repeted = [] # LISTA DE CONTROL DE REPETICIONES
       
        symbol_a = ['+'] #SIMBOLO DE SUMA
        symbol_r = ['-'] #SIMBOLO DE RESTA
        symbol_m = ['*'] #SIMBOLO DE MULTIPLICACION
        symbol_a = ['/'] #SIMBOLO DE DIVISION 

        #RECONOCER CORCHETES Y REALIZAR PRIMERO
        #RECONOCER MULTIPLICACIONES Y DIVISIONES Y RESOLVER 
        #REALIZAR SUMAS Y RESTAS

        
        res = split_block(expression)
        print(res)




        # multiplicated_list= get_multiplicated_list(init_numbers) #SE ENVIA EL ARREGLO Y SE TRABAJAN SOLO LAS MULTIPLICACIONES Y RETORNA UNA LISTA CON MULTIPLICACIONES
        # sum_list = __sum__( init_numbers) #SE REALIZA UNA SUMA DE LOS RESTANTES( SIN MULTIPLICACIONES)
        # print_result(multiplicated_list,sum_list,argument) #IMPRIME EL RESULTADO
    # except: #SI ALGO NO RESULTA BIEN NO SE ACEPTA
    #     print("No aceptado")
