
def intro():
    """
    prints out the information about exercise tracker
    and the list of actions user can perform
    """
    print("WELCOME TO EXERCISE TRACKER!!!\n\n")
    print("You can use exercise tracker to:")
    print("1. view the calories you have burnt exercising.\n")
    print("2. view logs you previously entered\n")
    print("3. save the new exercise data\n")
    print("To view logs or save new exercise data you'll need to enter your user name")


def get_user_action() -> str:
    """
    Requests action to perform from user.

    :returns string
    """
    while True:
        print("What would you like to do?\n")
        print("1 - get calories burnt\n")
        print("2 - view exercise logs\n")
        
        user_action = input("Enter 1 or 2 to continue: ")
        if validate_user_action(user_action):
            print("Data is valid!")
            break
            
    return user_action


def validate_user_action(action: str):
    """
    checks that value for action is not empty and
    that the value passed in is either 1 or 2.
    Raises ValueError if value cannot be converted to int
    or values is neither 1 nor 2.

    :returns bool
    """
    try:
        if not action:
            raise ValueError(
                "You have not entered a value for action to perform"
            )
        value = int(action)
        if value not in [1, 2]:
            raise ValueError(
                f"Expected value is 1 or 2. You provided {action}"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again\n")
        return False

    return True


def run_program():
    """
    Start program
    """
    intro()
    action = get_user_action()

    print(action)


run_program()
