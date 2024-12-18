import numpy as np
from numbers import Number

class Stack:
    def __init__(self):
        self.ls = []
    def __len__(self):
        return len(self.ls)
    def __str__(self):
        return str(self.ls)
    def pop(self):
        return self.ls.pop()
    def push(self, numero):
        return self.ls.append(numero)
    def top(self):
        return self.ls[-1]
    def index(self, i):
        return self.ls[int(i)]
    def empty(self):
        while(self.ls != []):
            self.ls.pop()
        return self.ls

class ForthVirtualMachine:
    def __init__(self):
        self.d_stack = Stack() # inicia pilha de dados
        self.r_stack = Stack() # inicia pilha de retorno

    # Retorna as stacks
    def stacks(self):
        return self.d_stack, self.r_stack

    # Empilha em D o resultado da soma
    def plus(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(a + b)
            return True
        except IndexError:
            return False

    # Empilha em D o resultado da subtração
    def minus(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(a - b)
            return True
        except IndexError:
            return False

    # Empilha em D o resultado da multiplicação
    def mult(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(a * b)
            return True
        except IndexError:
            return False

    # Empilha em D o resultado da divisão
    def div(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(a / b)
            return True
        except IndexError:
            return False

    # Empilha em D o resto da divisão
    def resto(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(a % b)
            return True
        except IndexError:
            return False

    # Empilha em D o resultado da raiz quadrada
    def raizq(self):
        D, R = self.stacks()
        try:
            a = D.pop()
            D.push(np.sqrt(a))
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador relacional and
    def opand(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a and b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador relacional or
    def opor(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a or b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador =
    def opeq(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a == b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador !=
    def opneq(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a != b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador >
    def gt(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a > b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador <
    def st(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a < b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False

    # Empilha 0 ou -1 em D de acordo com operador >=
    def goet(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a >= b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False
    
    # Empilha 0 ou -1 em D de acordo com operador <=
    def soet(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            if a <= b:
                D.push(-1)
            else:
                D.push(0)
            return True
        except IndexError:
            return False
    
    # true Empilha -1 em D
    def true(self):
        D, R = self.stacks()
        D.push(-1)
        return True

    # false Empilha 0 em D
    def false(self):
        D, R = self.stacks()
        D.push(0)
        return True
            
    # pick Copia n-esimo valor pro topo de D (2 PICK com a b c -- a b c a)
    def pick(self):
        D, R = self.stacks()
        try:
            D.push( D.index(-(D.pop()+1)) )
            return True
        except IndexError:
            return False

    # dup Duplica valor no topo de D (a -- a)
    def dup(self):
        D, R = self.stacks()
        try:
            D.push(D.top())
            return True
        except IndexError:
            return False

    # over Copia número abaixo do topo de D para o topo (a b –- a b a)
    def over(self):
        D, R = self.stacks()
        try:
            D.push( D.index(-2) )
            return True
        except IndexError:
            return False

    # swap Troca valores no topo de D (a b -- b a)
    def swap(self):
        D, R = self.stacks()
        try:
            b = D.pop()
            a = D.pop()
            D.push(b)
            D.push(a)
            return True
        except IndexError:
            return False

    # rot Rotaciona top-3 valores na pilha D (a b c d -- a d b c)
    def rot(self):
        D, R = self.stacks()
        try:
            d = D.pop()
            c = D.pop()
            b = D.pop()
            D.push(d)
            D.push(b)
            D.push(c)
            return True
        except IndexError:
            return False
    
    # drop Desempilha valor no topo da pilha D
    def drop(self):
        D, R = self.stacks()
        try:
            D.pop()
            return True
        except IndexError:
            return False

    # >r Move topo de D para pilha de resultados R
    def dtor(self):
        D, R = self.stacks()
        try:
            a = D.pop()
            R.push(a)
            return True
        except IndexError:
            return False

    # r> Move topo de R para pilha de dados D
    def rtod(self):
        D, R = self.stacks()
        try:
            a = R.pop()
            D.push(a)
            return True
        except IndexError:
            return False

    # r@ Copia topo de R para pilha de dados D
    def rat(self):
        D, R = self.stacks()
        try:
            a = R.top()
            D.push(a)
            return True
        except IndexError:
            return False

    # rand Empilha valor aleatório entre 0 e o valor no topo da pilha D
    def rand(self):
        D, R = self.stacks()
        try:
            rng = np.random.randint(0, D.pop())
            D.push(float(rng))
            return True
        except IndexError:
            return False

    # clear Limpa as pilhas
    def clear(self):
        D, R = self.stacks()
        D.empty()
        R.empty()
        return True

    # cr Salta uma linha (mesmo que imprimir ‘\n’ no C/C++)
    def cr(self):
        print('\n')
        return True

class LikeForthInterpreter(object):
    def __init__(self):
        self.fvm = ForthVirtualMachine()
        self.words = dict([
            ('.', self.dot), ('.s', self.dots), ('.d', self.dotd), ('acceptn', self.acceptn), ('+', self.fvm.plus), ('-', self.fvm.minus), ('*', self.fvm.mult),
            ('/', self.fvm.div), ('%', self.fvm.resto), ('sqrt', self.fvm.raizq), ('and', self.fvm.opand), ('or', self.fvm.opor), ('eq', self.fvm.opeq),
            ('neq', self.fvm.opneq), ('>', self.fvm.gt), ('<', self.fvm.st), ('>=', self.fvm.goet), ('<=', self.fvm.soet), ('true', self.fvm.true), ('false', self.fvm.false),
            ('pick', self.fvm.pick), ('dup', self.fvm.dup), ('over', self.fvm.over), ('swap', self.fvm.swap), ('rot', self.fvm.rot), ('drop', self.fvm.drop),
            ('>r', self.fvm.dtor), ('r>', self.fvm.rtod), ('r@', self.fvm.rat), ('rand', self.fvm.rand), ('clear', self.fvm.clear), ('cr', self.fvm.cr)
        ])

    # Remove o elemento do topo de D e o exibe na tela
    def dot(self):
        D, R = self.fvm.stacks()
        a = D.pop()
        if(a == int(a)):
            print( int(a), end=' ')
        else:
            print( a, end=' ')
        return True
    
    # Exibe as pilhas na tela
    def dots(self):
        D, R = self.fvm.stacks()
        print(f"D <{len(D)}> {str(D)} ")
        print(f"R <{len(R)}> {str(R)} ")
        return True

    # Exibe palavras criadas pelo usuário na tela
    def dotd(self):
        for w in self.words:
            if not callable(self.words[w]):
                print('%s: %s'%(w, list(self.words[w])))
        return True

    # Lê um número real do teclado e o insere na pilha D
    def acceptn(self):
        D, R = self.fvm.stacks()
        try:
            r = float(input())
            D.push(r)
            return True
        except ValueError:
            return False

    # Registra novas palavras criadas pelo usuário
    def fcompile(self, tokens):
        keyword = tokens[0]
        try:
            semicolon_pos = tokens.index(';')
        except ValueError:
            return False
        body = tokens[1:semicolon_pos]
        self.words[keyword] = body
        return tokens[semicolon_pos + 1:]

    # Verifica se a entrada foi reconhecida
    def interpret(self, tokens):
        if not tokens:
            return True
            
        if tokens[0] == ':': #Se for necessário registrar uma nova palavra
            rem = self.fcompile(tokens[1:])
            if rem == False:
                return False
            else:
                return self.interpret(rem)

        if tokens[0] in ['>', '>=', '<', '<=', 'eq', 'neq']:
            if (len(tokens) > 1) and (tokens[1] == 'if'): #Executa Seq1 se Cond é verdadeira (senão executa Seq2). Else é opcional
                D, R = self.fvm.stacks()
                try:
                    cond = [0, D.pop(), tokens[0]]
                    then_pos = tokens.index('then')
                    else_pos = 0
                    seq1 = []
                    seq2 = []
                    j = 1
                    while(j < then_pos):
                        if(tokens[j] == 'else'):
                            else_pos = j
                            j = then_pos
                        else:
                            seq1 += [tokens[j]]
                            j += 1
                    if else_pos > 0:
                        while(else_pos < then_pos):
                            seq2 += [tokens[else_pos]]
                            else_pos += 1
                    self.interpret(cond[1:])
                    var = D.pop()
                    if(var == -1):
                        self.interpret(seq1[1:])
                    elif (var == 0) and (else_pos > 0):
                        self.interpret(seq2[1:])
                    return self.interpret(tokens[(then_pos+1):])
                except ValueError:
                    return False
                
        if tokens[0] in self.words: #Se a palavra já estiver resgistrada
            fun = self.words[tokens[0]]
            if callable(fun):
                if fun():
                    return self.interpret(tokens[1:])
                else:
                    return False
            else:
                return self.interpret(list(fun) + tokens[1:])

        if tokens[0] == '."': # Exibe s1 s2 ... sn na tela
            try:
                n = tokens.index('."') + 1
                s = ""
                while(tokens[n] != '"'):
                    if(isinstance(tokens[n], Number)):
                        if(tokens[n] == int(tokens[n])):
                            s += f"{int(tokens[n])} "
                        else:
                            s += f"{tokens[n]} "
                    else:
                        s += f"{tokens[n]} "
                    n+=1
                print(s, end='')
                close_pos = n + 1
                return self.interpret(tokens[close_pos:])
            except IndexError:
                return False
            except ValueError:
                return False

        if tokens[0] == 'begin': #Repete Seq até condição Cond ser satisfeita
            D, R = self.fvm.stacks()
            try:
                until_pos = tokens.index('until')
                cond_pos = until_pos - 2
                seq = []
                j = 0
                while(j < cond_pos):
                    seq += [tokens[j]]
                    j += 1
                cond = []
                cond_pos = until_pos - 3
                while(cond_pos < until_pos):
                    cond += [tokens[cond_pos]]
                    cond_pos += 1
                self.interpret(seq[1:])
                self.interpret(cond[1:])
                while(D.pop() == 0):
                    self.interpret(seq[1:])
                    self.interpret(cond[1:])
                return self.interpret(tokens[(until_pos+1):])
            except ValueError:
                return False

        if tokens[0] == 'do': #Repete Seq enquanto B < E (E indica o fim e B o início)
            D, R = self.fvm.stacks()
            try:
                b = D.pop()
                e = D.pop()
                loop_pos = tokens.index('loop')
                j = 0
                seq = []
                while(j < loop_pos):
                    seq += [tokens[j]]
                    j += 1
                i_pos = -1
                if('i' in seq):
                    i_pos = seq.index('i')
                while(b < e):
                    if(i_pos > -1):
                        seq[i_pos] = b #Empilha em D o valor corrente de B
                    b += 1
                    self.interpret(seq[1:])
                return self.interpret(tokens[(loop_pos+1):])
            except ValueError:
                return False

        if tokens[0] == '(': #Pula comentários
            try:
                close_pos = tokens.index(')') + 1
                return self.interpret(tokens[close_pos:])
            except ValueError:
                return False
                
        else: #Se a palavra for um número
            D, R = self.fvm.stacks()
            try:
                t = float(tokens[0])
                D.push(tokens[0])
                return self.interpret(tokens[1:])
            except ValueError:
                return False
            
        return False

    # Quebra a string em tokens
    def tokenize(self, tokens):
        def string_to_num(tokens):
            try:
                return float(tokens)
            except ValueError:
                return tokens
        return [string_to_num(t) for t in tokens.split()]

    # Função REPL
    def REPL(self):
        input_str = input('?> ')
        if input_str != 'bye':
            ok = self.interpret(self.tokenize(input_str))
            if not ok:
                print('?')
            else:
                print('<ok>')
            self.REPL()

    # Roda a VM
    def run(self, txt = None): 
        self.__init__()
        if txt is None:
            print('Micro Forth (September 2024)')
            self.REPL()
        else:
            self.interpret(self.tokenize(txt))
            
forth = LikeForthInterpreter()
forth.run()
