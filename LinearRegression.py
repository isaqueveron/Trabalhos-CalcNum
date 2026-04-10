#Autor: Isaque Verona, 2025

import numpy as np
import matplotlib.pyplot as plt
import random as rd
import time

def f_true(x):
    a = -30
    b = 66
    return a*x+b

#Gerando base de dados scattered

XS = np.linspace( 0 , 6 , 100)
YS = [] #array para amazenar os valores de referencia
YS_scattered = []
for i in XS:
    YS.append(f_true(i))
    YS_scattered.append(f_true(i)+rd.random()+rd.randint(-20,20)) 

def J(a=float,b=float, xs=XS, ys=YS_scattered) -> float:
    """Funcao Custo usando MSE (min squared error)"""
    sum = 0
    indice_ys = 0
    for i in xs:
        sum += (ys[indice_ys]-((a*i)+b))**2
        indice_ys += 1
    return sum/len(xs)

plt.plot(XS,YS) #funcao base, ou real
plt.plot(XS,YS_scattered, '.') #dados para serem aproximados por uma regressao linear
plt.show()

def descendo_b(a=float,b=float, xs=XS, ys=YS_scattered) -> float:
    sum = 0
    indice_ys = 0
    for i in xs:
        sum += (((a*i)+b)-ys[indice_ys])
        indice_ys += 1
    return sum/len(xs)

def descendo_a(a=float,b=float, xs=XS, ys=YS_scattered) -> float:
    sum = 0
    indice_ys = 0
    for i in xs:
        sum += (((a*i)+b)-ys[indice_ys])*i
        indice_ys += 1
    return sum/len(xs)

#parametros iniciais
a = 0
b = 0
hiperparameter = 0.1 # 0.1 best value
converged_a = 0
converged_b = 0
iterations = 0
time_to_converge = time.time()
J_b = 0
J_a = 0
all_J_a = []
all_J_b = []

#Descendo
while not(converged_a) or not(converged_b):
    iterations+=1
    J_a_ant = J_a
    all_J_a.append(J_a_ant)
    J_b_ant = J_b
    all_J_b.append(J_b_ant)
    a_ant = a
    b_ant = b
    if (not(converged_a)):
        a = a_ant - (hiperparameter)*descendo_a(a_ant,b_ant)
    if (not(converged_b)):
        b = b_ant - (hiperparameter)*descendo_b(a_ant,b_ant)
    J_a = J(a,0)
    J_b = J(0,b)
    """como o valor da outra variavel esta 
    fixada em 0, nao vai convergir para zero, 
      mas vai convergir pra algum lugar.
    """
    #testes de convergencia
    epislon = 1e-5
    if (abs(J_a-J_a_ant)<epislon):
        #a = a_ant
        converged_a = 1
    
    if (abs(J_b-J_b_ant)<epislon):
        #b = b_ant
        converged_b = 1
    
    print("------------")
    print("a:", a)
    print("b:", b)
    print("J:", J_a)  
    print("J:", J_b)
    print("------------")

print("converged a = ", a)
print("converged b = ", b)
print("nbr of iter = ", iterations)
print("time to converge = ", time.time()-time_to_converge)
plt.plot(XS,YS)
plt.plot(XS,a*XS+b)
plt.plot(XS,YS_scattered, '.')
plt.show()

plt.plot(list(range(len(all_J_a))),all_J_a)
plt.show()
plt.plot(list(range(len(all_J_a))),all_J_b)
plt.show()
    





