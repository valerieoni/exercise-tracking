import datetime
from enum import Enum
from tabulate import tabulate
from helpers.validator import validate_yes_no
from api.exercise import Exercise
import data.spreadsheet as sheet
import data.user as User
import helpers.style as style


class Menu(Enum):
    """
    actions from which user can select.
    """
    CALORIES = 1
    EXERCISE_LOGS = 2
    EXIT = 3


class ExerciseTracker:
    """
    Creates an ExerciseTracker instance.

    ---
    Attributes:
    user_name (str): Username set from user input.
    Default at instance creation is an empty dictionary
    profile (dict): dictionary values set from use input
    """

    def __init__(self, user: User):
        """
        Sets default values for the instance attributes.
        """
        self.exercise = None
        self.user = user
        self.user_name = user.user_name

    def perform_user_action(self, action: Menu):
        """
        Valid action expected is 1 or 2. Raises ValueError if value is invalid.
        if action is 1 it creates an Exercise instance if not existing and
        calls method to get calories from the instance.
        Else if action is 2 then prompt user for username and
        displays the exercise log.
        """
        if action == Menu.CALORIES:
            self.get_calories()
        elif action == Menu.EXERCISE_LOGS:
            self.view_exercise_logs()
        else:
            raise ValueError("You have provided a wrong value for action")

    def view_exercise_logs(self):
        """
        Retrieves exercise records from sheet and
        prints them to the console.
        """
        print("\nYou have chosen to view exercise logs\n")
        if not self.user.is_current_user:
            style.print_error("No result found for "
                              f"user {self.user.user_name}!\n")
            return

        user_workouts = sheet.get_user_workouts(self.user.user_name)
        print(tabulate(
            user_workouts,
            headers=["date", "exercise", "duration in mins", "calories"]))

    def get_calories(self):
        """
        creates an Exercise instance if not existing and
        calls method to get calories from the instance
        """
        print("\nYou have chosen to get calories\n")
        profile = self.get_user_profile()
        if self.exercise is None:
            self.exercise = Exercise(
                profile['gender'], profile['age'],
                profile['height'], profile['weight']
            )
        data = self.exercise.get_exercise_stats()
        if not data or data is None:
            style.print_error("  No result found!!!\n")
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

        if len(self.user.profile) != 0:
            return self.user.profile

        print("Please enter values for gender, age, height and weight data\n")
        self.user.set_gender()
        self.user.set_age()
        self.user.set_height()
        self.user.set_weight()

        return self.user.profile

    def request_to_save(self, data):
        """
        Prompts user to save data and if yes,
        it calls get_username to get the username.
        inserts user_name into the first column of the workout data
        saves the user data if not already in the worksheet
        and save updated workout data to the workout sheet
        by calling the save_data from the spreadsheet instance
        """
        print("\nWould you like to save workout stats?\n")

        while True:
            response = input("Enter Y/N:\n")
            if validate_yes_no(response):
                break

        if response.lower() in ['yes', 'y']:
            for workout in data:
                workout.insert(0, self.user.user_name)
            if not self.user.is_current_user:
                today = datetime.datetime.now()
                today_formatted = today.strftime("%Y-%m-%d")
                user_data = [
                    self.user.user_name,
                    today_formatted,
                    self.user.profile['gender'],
                    self.user.profile['age'],
                    self.user.profile['weight'],
                    self.user.profile['height']
                ]
                sheet.update_users_worksheet(user_data)
                self.user.is_current_user = True
            sheet.update_workout_worksheet(data)
