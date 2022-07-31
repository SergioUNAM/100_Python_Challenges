def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value = remaining_value // 10
        print(digit, end=" ")
    print()


# Using built-in function divmod(), wich returns both the divisor and the remainder as a result

def extract_digits2(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=" ")
    print()


def run():
    extract_digits(1234)
    extract_digits2(1234)


if __name__ == "__main__":
    run()
