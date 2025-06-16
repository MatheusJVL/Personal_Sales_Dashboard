from colorama import init, Fore, Style

init(autoreset=True)


def print_red(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.RED}{msg}"


def print_green(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.GREEN}{msg}"


def print_yellow(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.YELLOW}{msg}"


def print_blue(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.BLUE}{msg}"


def print_magenta(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.MAGENTA}{msg}"


def print_cyan(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.CYAN}{msg}"


def print_white(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.WHITE}{msg}"


def print_gray(msg: str) -> str:
    return f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}{msg}"


def print_bold(msg: str) -> str:
    return f"{Style.BRIGHT}{msg}"
