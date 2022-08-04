def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False
    return True


def run():
    primes = []
    for number in range(2, 100):
        if is_prime(number):
            primes.append(number)
    print(primes)
    print("\nUsing list comprehensions:")
    primes2 = [number for number in range(2, 100) if is_prime(number)]
    print(primes2)


if __name__ == "__main__":
    run()
