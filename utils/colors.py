def print_red(msg: str) -> str:
    return f"\033[1m\033[31m{msg}\033[0m"


def print_green(msg: str) -> str:
    return f"\033[1m\033[32m{msg}\033[0m"


def print_yellow(msg: str) -> str:
    return f"\033[1m\033[33m{msg}\033[0m"


def print_blue(msg: str) -> str:
    return f"\033[1m\033[34m{msg}\033[0m"


def print_magenta(msg: str) -> str:
    return f"\033[1m\033[35m{msg}\033[0m"


def print_cyan(msg: str) -> str:
    return f"\033[1m\033[36m{msg}\033[0m"


def print_white(msg: str) -> str:
    return f"\033[1m\033[37m{msg}\033[0m"


def print_gray(msg: str) -> str:

    return f"\033[1m\033[90m{msg}\033[0m"  # Cinza claro


def print_bold(msg: str) -> str:
    return f"\033[1m{msg}\033[0m"
