"""Argument checking by the decorator

Previously, you performed various argument checks, such as to ensure a valid range of values. In Python, these safety checks can be delegated to a decorator. Consequently, the actual function code can remain as close as possible to the problem to be solved, without special treatment.

A function to check for positive integers can be implemented as follows, where a function is passed as a parameter and a function is used as a return:"""

"""Comprobación de argumentos por parte del decorador

Anteriormente, realizabas varias comprobaciones de argumentos, como por ejemplo para asegurar un rango válido de valores. En Python, estas comprobaciones de seguridad pueden ser delegadas a un decorador. En consecuencia, el código de la función real puede permanecer lo más cerca posible del problema a resolver, sin un tratamiento especial.

Una función para comprobar los enteros positivos puede implementarse de la siguiente manera, donde se pasa una función como parámetro y se utiliza una función como retorno:"""


def check_argument_is_positive_integer(unary_func):
    def helper(n):
        if type(n) == int and n > 0:
            return unary_func(n)
        else:
            raise ValueError("n must be positive and of type int")

    return helper


"""As a simple example of usage, let’s consider the calculation of the factorial where the parameter check is still included"""

"""Como ejemplo sencillo de uso, consideremos el cálculo del factorial en el que se sigue incluyendo la comprobación de parámetros"""


def factorial(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    if n == 1:
        return 1

    return n * factorial(n - 1)


def run():
    """To activate the check, you can wrap the above function with the argument check as follows:"""
    """Para activar la comprobación, puede envolver la función anterior con el argumento comprobación de la siguiente manera: """

    # factorial = check_argument_is_positive_integer(factorial)

    """It is also possible to define a new function as follows:"""
    """También es posible definir una nueva función como la siguiente:"""

    # wraping results in new function
    checked_factorial = check_argument_is_positive_integer(factorial)
    print(checked_factorial(5))

    # Factorial of the first 5 numbers
    for n in range(1, 6):
        print(checked_factorial(n))


"""In this example, the decorator is created using functions or nested functions. There are also higher order functions, wich are when a function receives another function as a parameter and returns a functiosn as result"""
"""En este ejemplo, el decorador se crea utilizando funciones o funciones anidadas. También hay funciones de orden superior, que son cuando una función recibe otra función como parámetro y, como resultado, devuelve una función."""

if __name__ == "__main__":
    run()
