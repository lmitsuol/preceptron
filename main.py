from random import randint, seed
from time import time
import sys

epocas =  100
N = 0.01 #Ritmo de aprendizado


x = [
    [ -1, 0, 0],
    [ -1, 0, 1],
    [ -1, 1, 0],
    [ -1, 1, 1],
]

w = [0.0, 0.0, 0.0]


OR = [ 0, 1, 1, 1]
AND = [ 0, 0, 0, 1]
XOR = [ 0, 1, 1, 0]

t = OR # operação lógica para ser treinada

NUM_EXEMPLOS = len(x)
NUM_ENTRADAS = len(x[0])


def atribuir_pesos_aleatorios():
    seed(time())
    for i in range(NUM_ENTRADAS):
        w[i] = randint(-100, 100) / 100.0

def funcao_de_ativacao(valor):
    return 1 if valor > 0 else 0

def net(e):
    soma = 0.0
    for i in range(NUM_ENTRADAS):
        soma += x[e][i] * w[i]
    return funcao_de_ativacao(soma)

def ajusta_pesos(e, y):
    for i in range(NUM_ENTRADAS):
        w[i] += N * (t[e] - net(e)) * x[e][i]

def treinamento():
    atribuir_pesos_aleatorios()

    n = 0  # inicializa contador de épocas

    while True:
        treinou = True  # assume que treinou corretamente

        for e in range(NUM_EXEMPLOS):
            y = net(e)

            if y != t[e]:
                ajusta_pesos(e, y)
                treinou = False

        n += 1

        if treinou or n > epocas:
            return (n, True) if treinou else (n, False)
        
def executar(x):
    soma = 0.0
    for i in range(NUM_ENTRADAS):
        soma += x[i] * w[i] 
    return funcao_de_ativacao(soma)
    
        
print(treinamento())

x1 = float(sys.argv[1])
x2 = float(sys.argv[2])
print(executar([-1, x1, x2]))
