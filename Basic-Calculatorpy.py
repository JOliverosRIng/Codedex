def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b

def calculadora():
    print("=== Calculadora Básica ===")
    print("Operaciones disponibles: +  -  *  /")

    try:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Elige la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))

        if operacion == "+":
            resultado = suma(num1, num2)
        elif operacion == "-":
            resultado = resta(num1, num2)
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = division(num1, num2)
        else:
            resultado = "Operación no válida."

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: por favor ingresa solo números válidos.")

# Ejecutar la calculadora
calculadora()
