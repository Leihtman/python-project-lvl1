def is_even(number: int) -> bool:
    return number % 2 == 0


def calc(operator: str, operand_1: int, operand_2: int) -> int | None:
    match operator:
        case "+":
            return operand_1 + operand_2
        case "-":
            return operand_1 - operand_2
        case "*":
            return operand_1 * operand_2
    return None
