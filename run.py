from exercise_tracker import ExerciseTracker
from user_action import *


def intro():
    """
    prints out the information about exercise tracker
    and the list of actions user can perform
    """
    print("WELCOME TO EXERCISE TRACKER!!!\n")
    print("You can use exercise tracker to:")
    print("- view the calories you have burnt exercising.")
    print("- save the new exercise data")
    print("- view logs you previously entered\n")
    print("You will be required to enter a valid username "
          "to view logs or save new exercise data\n")


def run_program():
    """
    Displays welcome message to user.
    Creates a new instance of ExerciseTracker class.
    Prompts the user to input 1 or 2 for action to perform from list
    and if the value is valid it moves on to perform action
    but if the user input is invalid, it
    displays error message and prompts user for input again.
    """
    intro()
    new_exercise_tracker = ExerciseTracker()
    action = get_user_action()

    try:
        new_exercise_tracker.perform_user_action(action)
    except ValueError as e:
        print(f"\nInvalid action value: {e}\n")
        get_user_action()


run_program()
