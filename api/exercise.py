import os
from datetime import date
import requests
from dotenv import load_dotenv, find_dotenv
import helpers.style as style


class Exercise:
    """
    Gets exercise stats with natural language queries
    from nutritionix api
    """

    API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

    def __init__(self, gender: str, age: int,
                 height_in_cm: float, weight_in_kg: float):
        self.age = age
        self.gender = gender
        self.height = height_in_cm
        self.weight = weight_in_kg
        self.headers = self.get_header()

    def get_exercise_stats(self) -> []:
        """
        gets exercise stats with natural language queries.
        calls parse_exercise_stats passing in the json as the parameter.
        returns an array of the formatted json or an empty array.
        """
        print("\nTo get calories for the exercise(s),"
              " you can type in text like:")
        style.print_info("      ran 5k and danced for 30 minutes")
        exercise_text = input("\n What exercise(s) did you do?\n")

        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age
        }
        print("\nSearching...")

        try:
            response = requests.post(
                self.API_ENDPOINT, json=parameters, headers=self.headers
                )
            status = response.status_code

            if status != 200:
                style.print_error(" Unable to process request")
                return []
            return self.parse_exercise_stats(
                response.json()
            )
        except requests.ConnectionError:
            style.print_error(" Unable to process request")
            return []

    def parse_exercise_stats(self, data):
        """
        get date of input from the date object.
        The date if formatted to Y-m-d i.e. 2022-01-30
        iterates through the data passed in and extracts
        name of exercise, duration in minutes, and calories.
        Depending on the size of data passed in, it returns either
        an array in the form [
                today_formatted,
                exercise_name,
                duration_min,
                calories
                ]
        for example ['2022-10-02', 'running', 18.65, 204.09]
        or an array of arrays [['2022-10-02', 'running', 18.65, 204.09],
        ['2022-10-02', 'walking', 15, 58.63]]
        """
        today = date.today()
        today_formatted = today.strftime("%Y-%m-%d")
        exercises = data['exercises']
        exercise_list = []
        for exercise in exercises:
            exercise_list.append(
                [
                    today_formatted,
                    exercise['name'],
                    exercise['duration_min'],
                    exercise['nf_calories']
                ]
            )

        return exercise_list

    def get_header(self) -> dict:
        """
        gets the NUTRITIONIX_APP_ID and NUTRITIONIX_API_KEY
        from the env file. Returns a dictionary object with keys
         "x-app-id", "x-app-key" and "x-remote-user-id".
        """
        load_dotenv(find_dotenv())
        return {
            "x-app-id": os.getenv('NUTRITIONIX_APP_ID'),
            "x-app-key": os.getenv('NUTRITIONIX_API_KEY'),
        }
