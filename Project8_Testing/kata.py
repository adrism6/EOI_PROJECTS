import re


def sum_numbers_in(expression: str) -> int:
    if expression is None or expression == "":
        return 0
    separator, expression = get_separator(expression)
    if separator in expression:
        tokens = expression.split(separator)
        total = 0
        for token in tokens:
            total = total + parse_int(token)
        return total
    return parse_int(expression)


def get_separator(expression):
    config_separator = "^//(.+)/"
    separator = ","
    match_expression = re.match(config_separator, expression)
    if match_expression:
        print(match_expression)
        separator = match_expression.group(1)
        start_expression = match_expression.end()
        expression = expression[start_expression:]
    return (separator, expression)


def parse_int(token):
    if re.match("^[0-9]+$", token):
        return int(token)
    return 0
