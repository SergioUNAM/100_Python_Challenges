"""In the following, you examine how to determine all real divisors of a number (i. e., those without the number itself).

The algorithm is quite simple. Initially, the result contains the number 1, as this is always a valid divider.

Then you go through all numbers starting by 2 up to half of the value (all higher values cannot be integer divisors if 2 is already a divisor) and check if they divide the given number without a remainder. If this is the case, then this number is a divisor and is included in a result list.

You implement the whole thing as follows:"""

"""A continuación, se examina cómo se determinan todos los divisores reales de un número (es decir, los que no son el número mismo).

El algoritmo es bastante sencillo. Inicialmente, el resultado contiene el número 1, ya que éste es siempre un divisor válido.

A continuación, se recorren todos los números a partir de 2 hasta la mitad del valor (todos los valores superiores no pueden ser divisores enteros si el 2 ya es un divisor) y se comprueba si dividen el número dado sin un resto. Si este es el caso, entonces este número es un divisor y se incluye en una lista de resultados.

Se implementa el todo como sigue:"""


def find_proper_divisors(value):
    # Function that finds the proper divisors of a given number
    divisors = [1]
    for i in range(2, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


def find_proper_divisors2(value):
    """Returns the proper divisors of a number, same function as the previous one but with List comprehensions."""
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


def run():
    value = int(input("Type an integer number: "))
    print(f"\nThe proper divisor of {value} are {find_proper_divisors(value)}")
    print(f"\nWith list comprehensions:\nThe proper divisors of {value} are {find_proper_divisors2(value)}")


if __name__ == "__main__":
    run()
