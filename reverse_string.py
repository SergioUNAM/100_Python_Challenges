def reverse_string(text):
    # Recursive termination
    if len(text) <= 1:
        return text

    first_char = text[0]
    remaining = text[1:]

    # recursive descent
    return reverse_string(remaining) + first_char


def reverse_string_short(text):
    return text if len(text) <= 1 else reverse_string_short(text[1:]) + text[0]


def run():
    text = "Sergio"
    print("Regular form: ", reverse_string(text))
    print("Short form: ", reverse_string_short(text))


if __name__ == "__main__":
    run()
