import operator
from digits_converter import number_to_art

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def evaluate_expression(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops):
        try:
            func = operators[op]
            result = func(result, numbers[i + 1])
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None
        except Exception as e:
            print(f"Calculation error: {e}")
            return None
    return result


def main():
    print("Welcome to the ASCII Calculator!")

    while True:
        numbers = []
        ops = []

        while True:
            try:
                num = float(input("Enter a number: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            print("Select an operator:")
            for op in operators.keys():
                print(f" '{op}'", end=' ')
            print("\n")

            op = input("Enter an operator: ")
            if op not in operators:
                print("Unsupported operator. Please try again.")
                continue
            ops.append(op)

            while True:
                try:
                    num = float(input("Enter the next number: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Please enter a valid number.")

            choice = input(
                "Press 'Enter' to continue adding operations or type 'c' to calculate the result: ")
            if choice.lower() == 'c':
                break

        result = evaluate_expression(numbers, ops)
        if result is not None:
            result = round(result, 3)
            if result == int(result):
                result_display = int(result)
            else:
                result_display = result
            print(f"Result: {result_display}")
            art_result = number_to_art(f"{result_display}")
            if art_result:
                print("\nASCII Art Result:\n")
                print(art_result)

        again = input(
            "\nWould you like to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the ASCII Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
