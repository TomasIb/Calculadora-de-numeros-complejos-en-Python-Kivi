import numpy as np #IMPORTACION DE LIBRERIA PARA ARREGLOS
class ComplexCalculator():
    def __init__(self):
        self._expression = None
        self._tokens = []
        self._current = None
        self.caracters = ['+','-','*','/','(',')','[',']']
        self.ready_expression = []
        self.result = None
        

    def set_expression(self,parameter):
        if(parameter != ''):
            self._expression = parameter
        else:
            self.expression = None
        if(self.separate_chain()):
            return True
        else:
            return False
        
    def get_expression(self):
        return self._expression

    def is_balanced_parentheses(self):
        if(self._expression != None):
            open_parentheses=[]
            closed_parentheses=[]
            for char in self._expression: # VERIFICA SI ESTÁ BALANCEADO
                if(char == '[' or char == '('):
                    open_parentheses.append(char)
                elif(char == ']' or char == ')'):
                    closed_parentheses.append(char)
            if(len(open_parentheses) == len(closed_parentheses)):
                return True
            else:
                return False
        else:
            print('Error','Cadena Vacia') #Generar alerta
            return False

    def exp(self):
        self.result = self.term()
        while self._current in ('+', '-'):
            if self._current == '+':
                self.next()
                self.result += self.term()
            if self._current == '-':
                self.next()
                self.result -= self.term()
        return self.result

    def factor(self):
        self.result = None
        if np.iscomplex(self._current):
            self.result = complex(self._current)
            self.next()
        elif self._current is '(' or  self._current is '[':
            self.next()
            self.result = self.exp()
            self.next()
        return self.result

    def term(self):
        self.result = self.factor()
        while self._current in ('*', '/'):
            if self._current == '*':
                self.next()
                self.result *= self.term()
            if self._current == '/':
                self.next()
                self.result /= self.term()
        return self.result

    def join_complex(self):
        argument = self._tokens
        real = None
        imaginary = None
        negative = ['-']
        point_negative = ['-','.']
        for i in range(len(argument)):

            if(argument[i] is ','):
               
                if(any(ele in argument[i-1] for ele in point_negative) and i > 0):
                    real = float(argument[i-1])
                    try_character_index = i-2; 
                    if(try_character_index > 0):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):
                            print("error 1")
                            return False

                elif(argument[i-1].isdigit() or(any(ele in argument[i-1] for ele in negative))and i > 0 ):
                    real = int(argument[i-1])
                    try_character_index = i-2; 
                    if(try_character_index > 0):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):
                            print("error 2")
                            return False

                if(any(ele in argument[i+1] for ele in point_negative)  and  i < len(argument)):
                    imaginary = float(argument[i+1])
                    try_character_index = i+2; 
                    if(try_character_index < len(argument)):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):
                            print("error 3")
                            return False

                elif(argument[i+1].isdigit() or((any(ele in argument[i+1] for ele in negative)) )and i < len(argument)):
                    imaginary = int(argument[i+1])
                    try_character_index = i+2; 
                    if(try_character_index < len(argument)):
                        if(argument[try_character_index] not in self.caracters and try_character_index > 0 and try_character_index < len(argument)):
                            print("error 4")
                            return False
                
        
                self.ready_expression.append(complex(real,imaginary))

            elif(argument[i] in self.caracters):
                self.ready_expression.append(argument[i])
        
        self._tokens = self.ready_expression
        return True


    def separate_chain(self):
        for i in range(len(self._expression)):
            if (self._expression[i].isdigit() and i > 0 and  (self._tokens[-1].isdigit() or self._tokens[-1][-1] is '.')):
                self._tokens[-1] += self._expression[i]
                
            elif self._expression[i] is '.' and i > 0 and self._expression[i-1].isdigit():
                self._tokens[-1] += self._expression[i]
            
            elif self._expression[i].isdigit() and i > 0 and (self._tokens[-1][-1].isdigit()):
                self._tokens[-1] += self._expression[i]  

            elif self._expression[i-1] == '-' and i > 0 and self._expression[i] not in self.caracters:    
                self._tokens[-1]+= self._expression[i]
            
        

            else:
                self._tokens.append(self._expression[i])
        negative = ['-']
        for i in range(len(self._tokens)):
            
            if(any(ele in self._tokens[i] for ele in negative)):
                index_inf = i-1
                
                if(index_inf > 0):
                    if(self._tokens[index_inf] in self.caracters or self._tokens[index_inf] is ',' ):
                        continue
                    else:
                        self._tokens.insert(i,'+')
            
        print(self._tokens)
        return True
      
   
    def set_current(self):
        self._current = self._tokens[0]
        
        
       
    def next(self): 
        self._tokens = self._tokens[1:]
        self._current = self._tokens[0] if len(self._tokens) > 0 else None


    def calculate(self,parameter):
        try:
            if(self.set_expression(parameter)):
                if(self.is_balanced_parentheses()):
                    self.search_tokens = self._tokens
                    self.join_complex()
                    self.set_current() #SETEA EL CARACTER QUE SE ESTÁ LEYENDO
                    self.result = self.exp()
                    print ("result:",self.result)
                    if(self.result != None):
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
