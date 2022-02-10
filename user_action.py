from validator import validate_user_action


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
