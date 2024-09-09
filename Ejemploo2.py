def calcular(a, b, c):
    return a * b + c


def principal():
    x = int(input("Introduce el valor de x: "))
    y = int(input("Introduce el valor de y: "))
    z = int(input("Introduce el valor de z: "))

    resultado = calcular(x, y, z)
    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    principal()
