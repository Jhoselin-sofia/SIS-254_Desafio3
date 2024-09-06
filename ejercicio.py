import sympy as sp
import math as M

x = sp.symbols('x')


"""PARAMETROS""" 
# Definir la función simbólica 
funcion = 2*x**4+x**3-(x/10)+(1/x) 
x0 = 1 #parametro 
x1 = 3.5 #parametro 
orden_maximo = 4 #nro iteraciones 
"""-------------"""

# Calcular derivadas automáticamente
def calcular_derivadas(funcion, variable, orden_maximo):
    derivadas = []
    derivada_actual = funcion
    for i in range(orden_maximo + 1):
        derivadas.append(sp.diff(derivada_actual, variable))
        derivada_actual = derivadas[-1]
    return derivadas

# Calcular la serie de Taylor en torno a x0
def serie_taylor(funcion, x0, x1, orden_maximo):
    # Calcular derivadas
    derivadas = calcular_derivadas(funcion, x, orden_maximo)

    # Calcular valor de la función en x0
    fx = funcion.subs(x, x0)

    # Calcular h
    h = x1 - x0

    # Calcular serie de Taylor
    yi = float(fx)
    resultados = []

    for i in range(orden_maximo + 1):
        Rn = derivadas[i].subs(x, x0) * (h**(i+1)) / M.factorial(i+1)
        resultados.append((i, yi, Rn))
        yi += Rn
    return resultados



# Calcular resultados de la serie de Taylor
resultados = serie_taylor(funcion, x0, x1, orden_maximo)

# Imprimir resultados
print("valores iniciales")
print("x0 =", x0)
print("x1 =", x1)
print()

print("f(x0) =", float(funcion.subs(x, x0)))
print("h =", x1 - x0)
print()

print("#","\t","|","f(x)","\t","|","Rn")
print("-"*30)
for i, yi, Rn in resultados:
    print(i, "\t", "|", yi, "\t", "|", Rn)
