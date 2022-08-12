# Excercise 2: Number as Text
# Write a function number_as_text(n) which, for a given positive number, converts th respective digits into corresponding text

def number_as_text(n):
    value = ""
    remaining_value = n
    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = int(remaining_value / 10)
        value = remainder_as_text + "" + value

    return value.strip()

value_to_text_mapping = {
    0: "Zero", 1: "ONE", 2: "TWO", 3: "THREE", 4
}