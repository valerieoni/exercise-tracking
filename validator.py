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
