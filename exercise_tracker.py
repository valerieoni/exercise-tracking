import datetime

from validator import validate_gender, validate_user_profile, \
    validate_username, validate_yes_no
from exercise import Exercise
from tabulate import tabulate
from spreadsheet import get_users, update_users_worksheet, \
    update_workout_worksheet, is_existing_user, get_user_workouts


class ExerciseTracker:
    """
    Creates an ExerciseTracker instance.

    ---
    Attributes:
    user_name (str): Username set from user input.
    Default at instance creation is an empty dictionary
    profile (dict): dictionary values set from use input
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
            self.get_calories()
        elif action == 2:
            self.view_exercise_logs()
        else:
            raise ValueError("You must have provided a wrong value for action")

    def view_exercise_logs(self):
        print("Amazing! you have chosen to view logs\n")
        user_name = self.get_user_name()
        if not is_existing_user(user_name):
            print(f"No result found for user {user_name}!")
            return

        user_workouts = get_user_workouts(user_name)
        print(tabulate(
            user_workouts,
            headers=["date", "exercise", "duration in mins", "calories"]))

    def get_calories(self):
        print("Great!, you have chosen to get calories\n")
        profile = self.get_user_profile()
        if self.exercise is None:
            self.exercise = Exercise(
                profile['gender'], profile['age'],
                profile['height'], profile['weight']
            )
        data = self.exercise.get_exercise_stats()
        if not data or data is None:
            print("No result found")
            return

        print(tabulate(
            data,
            headers=["date", "exercise", "duration in mins", "calories"]
        ))
        self.request_to_save(data)

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
            data_str = input("Enter your age,height_in_cm,weight_in_kg:\n")
            data = data_str.split(',')
            exercise_data = [i.strip() for i in data]
            if validate_user_profile(exercise_data):
                print("Data is valid!!!")
                self.profile = {
                    'gender': gender,
                    'age': int(exercise_data[0]),
                    'height': float(exercise_data[1]),
                    'weight': float(exercise_data[2])
                }
                break

        return self.profile

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
                "Enter your gender(male/female):\n"
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

        print("Your user name is required to retrieve/save your information.\n")
        while True:
            value = input("Please enter username:\n")
            user_name = value.strip()
            if validate_username(user_name):
                self.user_name = user_name
                break

        return user_name

    def request_to_save(self, data):
        """
        Prompts user to save data and if yes,
        it calls get_username to get the username.
        inserts user_name into the first column of the workout data
        saves the user data if not already in the worksheet
        and save updated workout data to the workout sheet
        by calling the save_data from the spreadsheet instance
        """
        print(f"Would you like to save workout data?\n{data}")

        while True:
            response = input("Enter Y/N:\n")
            if validate_yes_no(response):
                print(f"you have answered {response}")
                break

        if response.lower() in ['yes', 'y']:
            username = self.get_user_name()
            print("Processing workout data for saving......")
            for workout in data:
                workout.insert(0, username)
            if not is_existing_user(username):
                print(f"Creating new user record for {username}\n")
                today = datetime.datetime.now()
                today_formatted = today.strftime("%Y-%m-%d")
                user_data = [
                    username,
                    today_formatted,
                    self.profile['gender'],
                    self.profile['age'],
                    self.profile['weight'],
                    self.profile['height']
                ]
                update_users_worksheet(user_data)
            update_workout_worksheet(data)
