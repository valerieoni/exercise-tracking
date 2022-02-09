from exercise import *

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


def get_user_action() -> int:
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
            break

    return int(user_action)


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


def perform_user_action(action: int):
    try:
        if action == 1:
            print("Great!, you have chosen to get calories\n")
            print("We will need your gender, age, height and weight data\n")
            gender = request_gender()
            user_profile = request_profile()
            print(f"gender entered is {gender} and profile: {user_profile}")
            exercise = Exercise(
                gender, user_profile['age'], user_profile['height'], user_profile['weight']
            )
            exercise.get_exercise_calories()
        elif action == 2:
            print("Amazing! you have chosen to view logs\n")
            user_name = request_username()
            print(user_name)
        else:
            raise ValueError("You must have provided a wrong value for action")
    except ValueError as e:
        print(f"\nInvalid action value: {e}\n")
        get_user_action()


def request_profile():
    """
    Gets data from user to retrieve calories information
    Asks user for height, weight and age data.
    If data entered is valid, creates Exercise instance
    """
    print("\nNext is age,height in cm, weight in kg")
    print("Example data expected: 44,162.56,69.5\n")
    while True:
        data_str = input("Enter your age,height_in_cm,weight_in_kg: ")
        data = data_str.split(',')
        exercise_data = [i.strip() for i in data]
        if validate_user_profile(exercise_data):
            print("Data is valid!!!")
            break

    return {
        'age': int(exercise_data[0]),
        'height': float(exercise_data[1]),
        'weight': float(exercise_data[2])
    }


def request_gender() -> str:
    """
    Prompts user for a value for gender.
    validates value and returns gender if valid
    else displays error message to user and
    prompts for gender value again.

    :returns str
    """
    gender_values = {
        'm': "male",
        'f': "female",
    }
    while True:
        value = input(
            "Enter your gender (type m for male f for female): "
        )
        value = value.strip()
        if validate_gender(value, gender_values):
            break

    gender = value[0:1]
    return gender_values[gender.lower()]


def validate_gender(value: str, expected_values) -> bool:
    """
    validates gender value passed in.
    raises ValueError if value is empty
    or value is neither male nor female.

    :returns bool
    """
    try:
        if not value:
            raise ValueError("You must enter a value for gender")
        gender = value[0:1]
        if gender.lower() not in expected_values:
            raise ValueError(
                f"Expected value is m or f, you provided {value}"
            )
    except ValueError as e:
        print(f"\nInvalid action value: {e}\n")
        return False

    return True


def request_username():
    """
    Prompts user from username.
    checks username entered is valid data and
    returns username if valid otherwise prompts user for username
    """
    print("We will need your user name to retrieve your information.\n")
    while True:
        value = input("Please enter username: ")
        user_name = value.strip()
        if validate_username(user_name):
            break

    return user_name


def validate_username(value: str):
    """
    checks that user_name is not empty.
    Strips leading and trailing spaces from value passed in and
    checks that the value's length is between 8 and 16 long

    :returns bool
    """
    try:
        if not value:
            raise ValueError(
                "You have not entered a username"
            )
        user_length = len(value)
        if user_length < 8 or user_length > 18:
            raise ValueError(
                f"Username must be between 8 and 18 characters"
            )
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again\n")
        return False

    return True


def validate_user_profile(values):
    """
    Expects values to be an array of 3 elements.
    Raises ValueError if there aren't exactly 3 values
    or values cannot be converted to int and float
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
        [float(value) for value in values]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True


def run_program():
    """
    Start program
    """
    intro()
    action = get_user_action()
    perform_user_action(action)


run_program()
