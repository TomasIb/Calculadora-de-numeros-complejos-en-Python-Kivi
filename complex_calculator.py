import numpy as np #IMPORTACION DE LIBRERIA PARA ARREGLOS
class ComplexCalculator():
    def __init__(self):
        self._expression = None #GUARDA EXPRESION INGRESADA 
        self._tokens = [] #GUARDA CARACTERES
        self._current = None #VALOR ACTUAL AL RECORRER
        self.caracters = ['+','-','*','/','(',')','[',']'] #CARACTERES ACEPTADOS
        self.ready_expression = [] #EXPRESION SETEADA PARA SER OPERADA
        self.result = None #RESULTADO
        
    def set_expression(self,parameter):
        if(parameter != ''):  #SI CARACTERES INGRESADOS SON VACIOS
            self._expression = parameter 
        else:
            self.expression = None 

        if(self.separate_chain()): #SE PUEDE SEPARAR LA CADENA?
            return True
        else:
            return False
        

    def is_balanced_parentheses(self):
        if(self._expression != None): 
            open_parentheses=[] #ARREGLO DE PARENTESIS ABRE
            closed_parentheses=[] #ARREGLO DE PARENTESIS CIERRA
            for char in self._expression: # VERIFICA SI ESTÁ BALANCEADO
                if(char == '[' or char == '('): # SI SE ENCUENTRA UN PARENTESIS ABRE SE GUARDA EN EL ARREGLO
                    open_parentheses.append(char)
                elif(char == ']' or char == ')'): # SI SE ENCUENTRA UN PARENTESIS CIERRA SE GUARDA EN EL ARREGLO
                    closed_parentheses.append(char)
            if(len(open_parentheses) == len(closed_parentheses)): #SI LOS TAMAÑOS SON IGUALES ESTAN BALANCEADOS
                return True
            else:
                return False
        else:
            return False

    def exp(self):
        self.result = self.term() #PRIMERO REALIZA LAS MULTIPLICACIONES Y DIVISIONES
        while self._current in ('+', '-'): 
            if self._current == '+':
                self.next() #BUSCA EL SIGUIENTE
                self.result += self.term() #OPERA SUMA
            if self._current == '-':
                self.next()
                self.result -= self.term() #OPERA RESTA
        return self.result

    def factor(self):
        self.result = None
        if np.iscomplex(self._current):
            self.result = complex(self._current) #OBTIENE EL NUMERO
            self.next() #OBTIENE EL SIGUIENTE
        elif self._current is '(' or  self._current is '[': #SI EL SIGUIENTE ES UN PARENTESIS ABRE, BUSCA AL SIGUIETNE Y OPERA
            self.next()
            self.result = self.exp() # PRIMERO BUSCA SI ES MULTIPLICAION Y DIVISION Y LUEGO BUSCA  SUMA Y RESTA
            self.next()
        return self.result

    def term(self):
        self.result = self.factor() #PRIMERO VERIFICA LOS PARENTESIS
        while self._current in ('*', '/'):
            if self._current == '*':
                self.next()
                self.result *= self.term() 
            if self._current == '/':
                self.next()
                self.result /= self.term()
        return self.result

    def create_complex(self):
        argument = self._tokens
        real = None
        imaginary = None
        negative = ['-']
        point = ['.']
        point_negative = ['-','.']
        for i in range(len(argument)):

            if(argument[i] is ','):

                if any(ele in argument[i-1] for ele in point): #VERIFICA QUE DESPUES DE UN PUNTO VENGA UN DIGITO
                    for a in argument[i-1]:
                        last = a
                    if last.isdigit():
                        continue
                    else:
                        return False
                    
                 
                elif any(ele in argument[i+1] for ele in point): #VERIFICA QUE DESPUES DE UN PUNTO VENGA UN DIGITO
                    for a in argument[i+1]:
                       last = a
                    if last.isdigit():
                        continue
                    else:
                        return False
                    
                    

                if(any(ele in argument[i-1] for ele in point_negative) and i > 0): #SI EL ANTERIOR DECIMAL NEGATIVO
                    real = float(argument[i-1]) #CASTEA Y ASIGNA LA PARTE REAL
                    try_character_index = i-2; 
                    if(try_character_index > 0):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)): #SI EL ANTERIOR AL ANTERIOR NO ES UN CARACTER ERROR
                            print("error 1")
                            return False

                elif(argument[i-1].isdigit() or(any(ele in argument[i-1] for ele in negative))and i > 0 ): #SI EL ANTERIOR ES UN ENTERO NEGATIVO O POSITIVO
                    real = int(argument[i-1]) #CASTEA Y ASIGNA LA PARTE REAL
                    try_character_index = i-2; 
                    if(try_character_index > 0):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):  #SI EL ANTERIOR AL ANTERIOR NO ES UN CARACTER ERROR
                            print("error 2")
                            return False

                if(any(ele in argument[i+1] for ele in point_negative)  and  i < len(argument)): #SI EL CONSECUENTE ES DECIMAL NEGATIVO O POSITIVO
                    imaginary = float(argument[i+1])#CASTEA Y ASIGNA LA PARTE IMAGINARIA
                    try_character_index = i+2; 
                    if(try_character_index < len(argument)):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):#SI EL CONSECUENTE A EL CONSECUENTE NO ES UN CARACTER ERROR
                            print("error 3")
                            return False

                elif(argument[i+1].isdigit() or((any(ele in argument[i+1] for ele in negative)) )and i < len(argument)): #SI EL CONSECUENTE ES UN ENTERO POSITIVO O NEGATIVO
                    imaginary = int(argument[i+1]) #CASTEA Y ASIGNA LA PARTE IMAGINARIA
                    try_character_index = i+2; 
                    if(try_character_index < len(argument)):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)): #SI EL CONSECUENTE A EL CONSECUENTE NO ES UN CARACTER ERROR
                            print("error 4")
                            return False
                
        
                self.ready_expression.append(complex(real,imaginary)) #CREA EL NUMERO COMPLEJO Y LO APILA

            elif(argument[i] in self.caracters): #SI ES UN CARACTER LO APILA
                self.ready_expression.append(argument[i])
        
        self._tokens = self.ready_expression #SE ACTUALIZA EL ARREGLO PRINCIPAL
        return True 


    def separate_chain(self):
        for i in range(len(self._expression)): #SE RECORRE LA EXPRESION EN BUSCA DE LAS COMBINACIONES POSIBLES
            if (self._expression[i].isdigit() and i > 0 and  (self._tokens[-1].isdigit() or self._tokens[-1][-1] is '.')): #SI ANTES DE UN DIGITO VIENE UN DIGITO O UN PUNTO
                self._tokens[-1] += self._expression[i] #SE CONCATENA
                
            elif self._expression[i] is '.' and i > 0 and self._expression[i-1].isdigit(): #DESPUES DE UN DIGITO HAY UN PUNTO
                self._tokens[-1] += self._expression[i]
            
            elif self._expression[i].isdigit() and i > 0 and (self._tokens[-1][-1].isdigit()):  #DESPUES DE UN DIGITO UN DIGITO
                self._tokens[-1] += self._expression[i]  

            elif self._expression[i-1] == '-' and i > 0 and self._expression[i] not in self.caracters:    #HAY UN MENOS ATRAS DEL ACTUAL Y NO ES UN CARACTER
                self._tokens[-1]+= self._expression[i] 

            else:
                self._tokens.append(self._expression[i])

        
        negative = ['-']
        
        for i in range(len(self._tokens)): #INSERTA UN + SI ES QUE HAY UN NEGATIVO ANTES , Y HACE - EL NUMERO SIGUIENTE Y REALIZA UNA SUMA EN CASO DE QUE EXISTA UN +- 
            
            if(any(ele in self._tokens[i] for ele in negative)):
                index_inf = i-1
                index_sup = i+1
                if(index_inf > 0 and index_sup < len(self._tokens)):
                    if(self._tokens[index_inf] in self.caracters or self._tokens[index_inf] is ',' ):
                        continue
                   
                    if(self._tokens[index_sup] is '+'):
                        self._tokens = self._tokens[:i] + self._tokens[index_sup:] #OBTIENE TODOS LOS CARACTERES MENOS EL SIGNO -
                        self._tokens[index_sup] = '-'+self._tokens[index_sup] #LO AGREGA AL NUMERO SIGUIENTE
                        break #TERMINA
                    else:
                        self._tokens.insert(i,'+') # SI NO INSERTA UN +
        return True
      
   
    def set_current(self):
        self._current = self._tokens[0] #SETEA EL PRIMER ELEMENTO
        
    def next(self): 
        self._tokens = self._tokens[1:] #SACA EL ULTIMO ELEMENTO DE LA PILA
        self._current = self._tokens[0] if len(self._tokens) > 0 else None # OBTIENE EL PRIMER ELEMENTO


    def calculate(self,parameter):
        try:
            if(self.set_expression(parameter)): #SI SE PUEDE SETEAR LA EXPRESION INGRESADA
                if(self.is_balanced_parentheses()): #Y LOS PARENTESIS ESTAN BALANCEADOS
                    self.create_complex() #CREA NUMEROS COMPLEJOS
                    self.set_current() #SETEA EL CARACTER QUE SE ESTÁ LEYENDO EN LA OPERACION
                    self.result = self.exp() #OPERA LA CADENA
                    print ("result:",self.result)
                    if(self.result != None): #SI EXISTE RESULTADO
                        return self.result,self.ready_expression
                    else:
                        return False,False
                else:
                    return False,False
            else:
                return False,False
            
        except:
            return False,False

            
        


if __name__ == "__main__":
    calculator = ComplexCalculator()
#input 2,2+3,4*[2,9/3,9+[3,4/(2,2)]]
