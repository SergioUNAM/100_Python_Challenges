"""

Count as well as sum up the natural numbers that are divisible by 2 or 7 up to a given maximun value (exclusive) and output it to the console. Write a function calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive). Extend it so that it returns the two values instead of performing the console output.

For example Maximun: 8; Divisible by 2: 2, 4, 6; Divisible by 7: 7; Count: 4; Sum: 2 + 4 + 5 + 7 = 19

Hint: The modulo operator helps to check whether divisibility is given

///////////////////////////////////////////////////////////////////////////////////////////////////////////

Contar así como sumar los números naturales que son divisibles por 2 o 7 hasta un valor máximo dado (exclusivo) y enviarlo a la consola. Escribe una función calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive). Extiéndela para que devuelva los dos valores en lugar de realizar la salida por consol

Por ejemplo Máximo: 8; Divisible por 2: 2, 4, 6; Divisible por 7: 7; Cuenta: 4; Suma: 2 + 4 + 5 + 7 = 19

Pista: El operador módulo ayuda a comprobar si se da la divisibilidad

"""


def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            sum += i

    print(f"count: {count}")
    print(f"sum: {sum}")


"""

What remains is the desire to return the two values. With Python, this is an easy task since tuples are applicable for this, for example, with return(sum, count), or the even shorter return sum, count.

It is even clearer to use a dictionary. This makes the unit text very readable in the end:

///////////////////////////////////////////////////////////////////////////////////////////////////////////

Con Python, esto es una tarea fácil ya que las tuplas son aplicables para esto, por ejemplo, con return(sum, count), o el aún más corto return sum, count.

Es aún más claro utilizar un diccionario. Esto hace que el texto de la unidad sea muy legible al final:

"""

# With dictionaries / Con diccionarios
def calc_sum_and_count_all_numbers_div_by_2_or_7_v2(max_exclusive):
    count = 0
    sum = 0

    for i in range(1, max_exclusive):
        if i % 2 == 0 or i % 7 == 0:
            count += 1
            sum += i

    return {"sum": sum, "count": count}


def run():
    test_number_list = list(range(1, 100))
    for number in test_number_list:
        print(f"In the range of 1 to {number}")
        calc_sum_and_count_all_numbers_div_by_2_or_7(number)
        print()

    for number in test_number_list:
        print("Version 2")
        print(f"In the range of 1 to {number}")
        print(calc_sum_and_count_all_numbers_div_by_2_or_7_v2(number))
        print()


if __name__ == "__main__":
    run()
