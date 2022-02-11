from exercise_tracker import ExerciseTracker
from validator import validate_user_action, validate_yes_no


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


def get_user_action() -> int:
    """
    Requests action to perform from user.

    :returns int
    """
    while True:
        print("What would you like to do?\n")
        print("1 - get calories burnt\n")
        print("2 - view exercise logs\n")

        user_action = input("Enter 1 or 2 to continue: ")
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
    intro()
    new_exercise_tracker = ExerciseTracker()
    action = get_user_action()

    try:
        new_exercise_tracker.perform_user_action(action)
    except ValueError as error:
        print(f"\nInvalid action value: {error}\n")
        get_user_action()

    while True:
        print("Would you like to perform another action?")
        response = input("Please enter Y/N to continue: ")
        if validate_yes_no(response) and response.lower() in ['yes', 'y']:
            action = get_user_action()
            new_exercise_tracker.perform_user_action(action)
        else:
            print("Good Bye!!!")
            break

run_program()
