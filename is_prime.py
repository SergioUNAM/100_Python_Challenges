def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % i == 0:
            return False
    return True


def run():
    print(is_prime(38421))


if __name__ == "__main__":
    run()
