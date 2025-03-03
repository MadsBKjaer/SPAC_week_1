from math import sqrt


def add(num1: float, num2: float) -> float:
    return num1 + num2


def substract(num1: float, num2: float) -> float:
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    return num1 / num2


def power(num1: float, num2: float) -> float:
    return num1**num2


def sqrt_(num1: float, num2: float) -> float:
    return sqrt(num2)


def operator_detection(user_input: str) -> list:
    if "+" in user_input:
        return [add] + user_input.split("+")
    elif "-" in user_input:
        return [substract] + user_input.split("-")
    elif "*" in user_input:
        return [multiply] + user_input.split("*")
    elif "/" in user_input:
        return [divide] + user_input.split("/")
    elif ":" in user_input:
        return [divide] + user_input.split(":")
    elif "^" in user_input:
        return [power] + user_input.split("^")
    elif "sqrt" in user_input:
        return [sqrt_] + user_input.split("sqrt")
    else:
        return [False]


if __name__ == "__main__":
    num1: float = 0
    print("Accepted operators:\n+, -, *, /, :, ^, sqrt.\nType q to quit session.")
    while True:
        user_input = input("Input equation:")

        if user_input == "q":
            print("Session ended.")
            break

        input_list = operator_detection(user_input=user_input.replace(" ", ""))
        operator: callable = input_list[0]

        if not operator:
            print(f"No operation detected!\n")
            continue

        num2: float = float(input_list[2])

        if operator == divide and not num2:
            print("Can't divide by 0!\n")
            continue

        if operator == sqrt_ and num2 < 0:
            print("Can't take root of negative number!\n")
            continue

        num1_str: str = str(num1)
        if input_list[1]:
            num1: float = float(input_list[1])
            num1_str: str = ""

        # print(input_list)
        num1: float = operator(num1, num2)
        print(f"{(num1_str + user_input).replace(" ", "")} = {num1}")
