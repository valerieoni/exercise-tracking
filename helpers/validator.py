from helpers.style import *
import enum

def validate_user_action(action: str, menu: enum.Enum):
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
                "You have not entered a value"
            )
        value = int(action)
        menu(value).name
    except ValueError as error:
        print_error(f"\nInvalid data: {error}, please try again\n")
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
    except ValueError as error:
        print_error(f"Invalid data: {error}, please try again")
        return False

    return True


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
        if user_length < 6 or user_length > 18:
            raise ValueError(
                "Username must be between 6 and 18 characters. "
                f"you entered {user_length} characters"
            )
    except ValueError as error:
        print_error(f"\nInvalid data: {error}, please try again\n")
        return False

    return True


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
    except ValueError as error:
        print_error(f"\nInvalid action value: {error}\n")
        return False

    return True

def validate_yes_no(value: str) -> bool:
    """
    gets the first letter of the value
    changes value to lowercase and validates
    value. returns true if first letter of the value
    is y or n.

    :returns bool
    """
    try:
        if not value:
            raise ValueError("You have not entered a value "
                             "Please enter Y/N")
        response = value[0:1]
        if response.lower() not in ['y', 'n']:
            raise ValueError(
                f"Expected value is either Y, Yes, N or No, you provided {value}"
            )
    except ValueError as error:
        print_error(f"\nInvalid action value: {error}\n")
        return False

    return True

def validate_int(value: str, value_name: str) -> bool:
    """
    validates value passed in for age
    converts value to int and
    checks that value is greater than 0
    """
    try:
        int_value = int(value)
        if not int_value:
            raise ValueError(
                f"You have not entered a valid value for {value_name}"
            )
    except ValueError as error:
        print_error(f"Invalid value: {error}. Please try again")
        return False

    return True

def validate_float(value: str, value_name: str) -> bool:
    """
    validates value passed in for age
    converts value to int and
    checks that value is greater than 0
    """
    try:
        float_value = float(value)
        if not float_value:
            raise ValueError(
                f"You have not entered a valid value for {value_name}"
            )
    except ValueError as error:
        print_error(f"Invalid value: {error}. Please try again")
        return False

    return True
