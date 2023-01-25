def validate_min_size(password: str, value: int) -> bool:
    validate: bool = True

    if len(password) < value:
        validate: bool = False

    return validate


def validate_no_repeted(password: str) -> bool:
    validate: bool = True

    previous_char: str = ''
    for char in password:
        if char == previous_char:
            validate: bool = False
            break
        previous_char: str = char

    return validate


def count_char(password: str, function) -> int:
    count: int = 0
    for char in password:
        if any(map(function, char)):
            count += 1

    return count


def validate_min_digit(password: str, value: int) -> bool:
    validate: bool = True

    count: int = count_char(password=password, function=str.isdigit)

    if count < value:
        validate: bool = False
    return validate


def validate_min_low_case(password: str, value: int) -> bool:
    validate: bool = True

    count: int = count_char(password=password, function=str.islower)

    if count < value:
        validate: bool = False

    return validate


def validate_min_upper_case(password: str, value: int) -> bool:
    validate: bool = True

    count: int = count_char(password=password, function=str.isupper)

    if count < value:
        validate: bool = False

    return validate


def validate_min_special_chars(password: str, value: int) -> bool:
    validate: bool = True
    special_chars: str = '!@#$%^&*()-+\/{}[]'

    count: int = 0
    for char in password:
        if special_chars.find(char) != -1:
            count += 1

    if count < value:
        validate: bool = False

    return validate
