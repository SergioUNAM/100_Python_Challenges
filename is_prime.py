def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False
    return True


def run():
    primes = []
    for number in range(2, 10000):
        if is_prime(number):
            primes.append(number)
    print(primes)
    print(f"There are {len(primes)} primes")


if __name__ == "__main__":
    run()
