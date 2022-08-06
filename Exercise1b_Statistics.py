"""Count as well as sum up the natural numbers that are divisible by 2 or 7 up to a given maximun value (exclusive) and output it to the console. Write a function calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive). Extend it so that it returns the two values instead of performing the console output.

For example Maximun: 8; Divisible by 2: 2, 4, 6; Divisible by 7: 7; Count: 4; Sum: 2 + 4 + 5 + 7 = 19

Hint: The modulo operator helps to check whether divisibility is given
"""

""""Contar así como sumar los números naturales que son divisibles por 2 o 7 hasta un valor máximo dado (exclusivo) y enviarlo a la consola. Escribe una función calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive). Extiéndela para que devuelva los dos valores en lugar de realizar la salida por consol

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


def run():
    test_number_list = list(range(1, 100))
    for number in test_number_list:
        print(f"In the range of 1 to {number}")
        calc_sum_and_count_all_numbers_div_by_2_or_7(number)
        print()


if __name__ == "__main__":
    run()
