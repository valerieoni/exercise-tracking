import time
import click
from exercise_tracker import ExerciseTracker
from helpers.validator import validate_user_action, validate_yes_no
from helpers.style import *
from data.user import *
TERMINAL_WIDTH = os.get_terminal_size().columns


def intro():
    """
    prints out the information about exercise tracker
    and the list of actions user can perform
    """
    print("\n You can use exercise tracker to:")
    print("  - View the calories you have burnt exercising.")
    print("  - Save the new exercise data")
    print("  - View logs you previously entered\n")

    print(" You will be required to enter a valid username "
          "to view logs or save new exercise data\n")


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
        print("  1 - get calories burnt")
        print("  2 - view exercise logs")

        user_action = input("\nEnter 1 or 2 to continue:\n")
        if validate_user_action(user_action):
            break

    return int(user_action)


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