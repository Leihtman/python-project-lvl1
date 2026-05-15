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


def sort_integers(numbers: list[int]) -> list[int]:
    sorted_list = numbers.copy()
    sorted_list.sort()
    return sorted_list


def find_greatest_common_divisor(number_1: int, number_2: int) -> int:
    min_number, max_number = sort_integers([number_1, number_2])
    greatest_divisor = min_number

    if min_number == max_number:
        return min_number
    elif max_number % min_number == 0:
        return min_number
    elif min_number == 0:
        return max_number

    while greatest_divisor > 0:
        greatest_divisor -= 1

        if max_number % greatest_divisor == 0 and min_number % greatest_divisor == 0:
            return greatest_divisor
