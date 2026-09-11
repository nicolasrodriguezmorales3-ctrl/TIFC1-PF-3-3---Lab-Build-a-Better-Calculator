def main():
  print("Hello learners!")

import math

def addmultiplenumbers(numeros):
    return sum(numeros)

def multiplymultiplenumbers(numeros):
    if not numeros:
        return 0
    return math.prod(numeros)

def isiteven(num):
    return num % 2 == 0 and num % 1 == 0

def main():
    print("¡Bienvenido a la calculadora!")

def isitaninteger(num):
    if isinstance(num, bool):
        return False
    return isinstance(num, (int, float)) and num % 1 == 0
if __name__=="__main__":
  main()