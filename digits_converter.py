from digits import digits_art


def number_to_art(number):
    number_str = str(number)
    lines = ['' for _ in range(7)]

    for char in number_str:
        if char not in digits_art:
            print(f"Char '{char}' is not supported.")
            return None
        char_art = digits_art[char]
        for i in range(7):
            lines[i] += char_art[i] + '  '

    art_result = '\n'.join(lines)
    return art_result
