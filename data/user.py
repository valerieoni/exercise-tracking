from data.spreadsheet import get_user
from helpers.validator import validate_gender,\
    validate_float, validate_int


class User(object):
    """
    ---
    Attributes:
    user_name (str):
    profile (dict)
    is_current_user
    """

    def __init__(self, user_name):
        """
        Gets user profile and
        set attributes user_name and profile.
        """
        user = get_user(user_name)
        self.user_name = user_name
        self.profile = {}
        self.is_current_user = False
        if user:
            self.is_current_user = True
            self.profile = {
                'gender': user.get('gender'),
                'age': int(user.get('age')),
                'height': float(user.get('height')),
                'weight': float(user.get('weight'))
            }

    def set_gender(self):
        """
        Prompts user for a value for gender.
        validates value and sets gender if valid
        else displays error message to user and
        prompts for gender value again.
        """
        gender_values = {
            'm': "male",
            'f': "female",
        }
        while True:
            value = input(
                "  \nPlease enter gender(male/female):\n"
            )
            value = value.strip().lower()
            if validate_gender(value, gender_values):
                break

        gender = value[0:1]
        self.profile['gender'] = gender_values[gender]

    def set_age(self):
        """
        Prompts user for a value for age.
        validates value and set age if valid
        else displays error message to user and
        prompts for gender value again.
        """
        while True:
            value = input(
                "  \nPlease enter age:\n"
            )
            if validate_int(value, 'age'):
                break

        self.profile['age'] = int(value)

    def set_height(self):
        """
        Prompts user for a value for height.
        validates value and set age if valid
        else displays error message to user and
        prompts for gender value again.
        """
        while True:
            value = input(
                "  \nPlease enter height in cm:\n"
            )
            if validate_float(value, 'height'):
                break

        self.profile['height'] = float(value)

    def set_weight(self):
        """
        Prompts user for a value for height.
        validates value and set age if valid
        else displays error message to user and
        prompts for gender value again.
        """
        while True:
            value = input(
                "  \nPlease enter Weight in kg:\n"
            )
            if validate_float(value, 'weight'):
                break

        self.profile['weight'] = float(value)
