from colorama import init
from colorama import Fore, Back, Style
import os

init(autoreset=True)


def print_error(text: str):
    """
    prints red text to console
    """
    print(Fore.RED + text)


def print_success(text: str):
    """
    print green text to console
    """
    print(Fore.RED + text)
