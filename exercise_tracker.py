from validator import *
from exercise import Exercise


class ExerciseTracker:
    """
    Creates an ExerciseTracker instance.

    ---
    Attributes:
        user_name (str): Username set from user input. Default at instance creation is None
        profile (dict): Initialized as an empty dictionary at instance creation. values set from use input
    """

    def __init__(self):
        """
        Sets default values for the instance attributes.
        """
        self.exercise = None
        self.user_name = None
        self.profile = {}

    def perform_user_action(self, action: int):
        """
        Valid action expected is 1 or 2. Raises ValueError if value is invalid.
        if action is 1 it creates an Exercise instance if not existing and
        calls method to get calories from the instance.
        Else if action is 2 then prompt user for username and
        displays the exercise log.
        """
        if action == 1:
            print("Great!, you have chosen to get calories\n")
            profile = self.get_user_profile()
            print(f"profile: {profile}")
            if self.exercise is None:
                self.exercise = Exercise(
                    profile['gender'], profile['age'], profile['height'], profile['weight']
                )
            self.exercise.get_exercise_calories()
        elif action == 2:
            print("Amazing! you have chosen to view logs\n")
            user_name = self.get_user_name()
            print(user_name)
        else:
            raise ValueError("You must have provided a wrong value for action")

    def get_user_profile(self):
        """
        Gets user's profile to retrieve calories information.
        Request data from user if it hadn't been set i.e
        first time request_profile is called
        Asks user for height, weight and age data.
        If data entered is valid, creates Exercise instance.
        """

        if len(self.profile) != 0:
            return self.profile

        print("We will need your gender, age, height and weight data")

        gender = self.request_gender()
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
            'gender': gender,
            'age': int(exercise_data[0]),
            'height': float(exercise_data[1]),
            'weight': float(exercise_data[2])
        }

    def request_gender(self) -> str:
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

    def get_user_name(self):
        """
        Prompts user from username.
        checks username entered is valid data and
        returns username if valid otherwise prompts user for username
        """
        if self.user_name is not None:
            return self.user_name

        print("We will need your user name to retrieve your information.\n")
        while True:
            value = input("Please enter username: ")
            user_name = value.strip()
            if validate_username(user_name):
                break

        return user_name
