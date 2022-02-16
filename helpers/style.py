from colorama import init
from colorama import Fore, Style

init(autoreset=True)


def print_error(text: str):
    """
    prints red text to console
    """
    print(Fore.RED + Style.BRIGHT + text)
