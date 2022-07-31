"""Determine number of digits Instead of extracting individual digits, you can also use a repeated division to determine the number of digits in a decimal number by simply dividing by 10 until there is no remainder left:"""

"""Determinar el número de dígitos En lugar de extraer dígitos individuales, también se puede utilizar una división repetida para determinar el número de dígitos de un número decimal, simplemente dividiendo por 10 hasta que no quede ningún resto:"""


def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count


def run():
    print(count_digits(12345))


if __name__ == "__main__":
    run()
