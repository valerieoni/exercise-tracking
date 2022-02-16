from colorama import init
from colorama import Fore, Style

init(autoreset=True)


def print_error(text: str):
    """
    prints red text to console
    """
    print(Fore.RED + Style.BRIGHT + text)


def print_success(text: str):
    """
    print green text to console
    """
    print(Fore.GREEN + Style.BRIGHT + text)


def print_info(text: str):
    """
    print blue text to console
    """
    print(Fore.BLUE + Style.BRIGHT + text)
