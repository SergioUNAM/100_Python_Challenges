"""Basic  Arithmetic Operations

EN: Write function calc(m, n) that multiplies two variables m and n of type int, then divides the product by two, and ouputs the remainder with respect to 7

ES: Escribe la función calc(m, n) que multiplica dos variables m y n de tipo int, luego divide el producto por dos, y devuelve el resto con respecto a 7
"""


def calc(m, n):
    return ((m * n) // 2) % 7


def run():
    print(calc(5, 5))


if __name__ == "__main__":
    run()
