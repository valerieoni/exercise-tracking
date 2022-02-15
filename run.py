import time
import click
from exercise_tracker import ExerciseTracker, Menu
from helpers.validator import validate_user_action, validate_yes_no
from helpers.style import *
import data.user as user
import helpers.validator as validate

TERMINAL_WIDTH = os.get_terminal_size().columns

def intro_message():
    """
    prints out the information about exercise tracker
    and the list of actions user can perform
    """
    print("\n You can use exercise tracker to:")
    print("  - View the calories you have burnt exercising.")
    print("  - Save the new exercise data")
    print("  - View logs you previously entered\n")


def get_user_name():
    """
    Prompts user from username.
    checks username entered is valid data and
    returns username if valid otherwise prompts user for username
    """

    while True:
        input_value = input("Please enter a user name:\n")
        user_name = input_value.strip()
        if validate.validate_username(user_name):
            break

    return user_name

def end_program():
    """
    displays exit text to user and exits the program after 2 seconds
    """
    click.clear()
    print('\n')
    print("Thank you for using Exercise Tracker. Good Bye!!!".center(TERMINAL_WIDTH))
    print("\n\n")
    print(Fore.GREEN + f"{'*' * 10}\033[01m The natural language search "
                       f"is powered by nutriontix.com {'*' * 10}".center(TERMINAL_WIDTH))


def get_user_action() -> int:
    """
    Requests action to perform from user.

    :returns int
    """
    while True:
        print(" What would you like to do?")
        print("  1 - Get calories burnt")
        print("  2 - View exercise logs")
        print("  3 - Exit")

        user_action = input("\nEnter 1 or 2 to continue:\n")
        if validate_user_action(user_action, Menu):
            break

    value = int(user_action)
    return Menu(value)

def run_program():
    """
    Displays welcome message to user.
    Creates a new instance of ExerciseTracker class.
    Prompts the user to input 1 or 2 for action to perform from list
    and if the value is valid it moves on to perform action
    but if the user input is invalid, it
    displays error message and prompts user for input again.
    """
    print("WELCOME TO EXERCISE TRACKER".center(TERMINAL_WIDTH))
    print('***'.center(TERMINAL_WIDTH, '='))
    intro_message()
    name = get_user_name()
    app_user = user.User(name)
    print(f" \nWelcome {app_user.user_name},\n")

    new_exercise_tracker = ExerciseTracker(app_user)
    while True:
        action = get_user_action()
        if action == Menu.EXIT:
            end_program()
            break
        new_exercise_tracker.perform_user_action(action)

def run_program2():
    """
    Displays welcome message to user.
    Creates a new instance of ExerciseTracker class.
    Prompts the user to input 1 or 2 for action to perform from list
    and if the value is valid it moves on to perform action
    but if the user input is invalid, it
    displays error message and prompts user for input again.
    """
    print("WELCOME TO EXERCISE TRACKER".center(TERMINAL_WIDTH))
    print('***'.center(TERMINAL_WIDTH, '='))
    intro()
    new_exercise_tracker = ExerciseTracker()
    time.sleep(1)
    action = get_user_action()

    try:
        new_exercise_tracker.perform_user_action(action)
    except ValueError as error:
        print_error(f"Invalid action value: {error}")
        get_user_action()

    while True:
        print("\nWould you like to perform another action?")
        response = input("Please enter Y/N to continue:\n")
        if validate_yes_no(response) and response.lower() in ['yes', 'y']:
            action = get_user_action()
            new_exercise_tracker.perform_user_action(action)
        else:
            end_program()
            break

if __name__ == '__main__':
    run_program()