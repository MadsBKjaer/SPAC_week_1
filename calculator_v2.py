operator_dict = {
    "^": lambda a, b: a**b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}


def contains_operator(sub_string: str | list[str]) -> str | None:
    for operator in operator_dict.keys():
        if operator in sub_string:
            return operator

    return None


def operator_partition(user_input: list[str], equation_list: list = []) -> list[str]:
    for string in user_input:
        operator: str | None = contains_operator(string)

        if (operator is None) or (string == operator):
            equation_list.append(string)
            continue

        operator_partition(list(string.partition(operator)), equation_list)

    return [float(x) if x not in operator_dict.keys() else x for x in equation_list]


def calculator(equation_list: list[str]) -> float:
    operator: str = contains_operator(equation_list)
    if operator is None:
        print(f"Got stuck as {equation_list}")
    print(equation_list)
    first_index: int = equation_list.index(operator)
    left_float, right_float = (
        equation_list[first_index - 1],
        equation_list[first_index + 1],
    )
    sub_result: float = operator_dict[operator](left_float, right_float)
    del equation_list[first_index - 1 : first_index + 2]
    equation_list.insert(first_index - 1, sub_result)

    if len(equation_list) == 1:
        print(f"Answer: {equation_list[0]}")
        return

    calculator(equation_list)


if __name__ == "__main__":
    print(f"Supported operators: {", ".join(operator_dict)}")
    while True:
        user_input: str = input("Input equation:").replace(" ", "")
        if user_input == "q":
            break

        equation_list: list[str] = operator_partition([user_input], equation_list=[])
        calculator(equation_list)
