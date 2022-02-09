import requests


class Exercise:
    """
    Communicates with the exercise endpoint
    """

    API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    APP_ID = '3f5b8702'
    API_KEY = '9f123cba166d107c2d00e0d7a078eb12'

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": '0',
    }

    def __init__(self, gender: str, age: int, height_in_cm: float, weight_in_kg: float):
        self.age = age
        self.gender = gender
        self.height = height_in_cm
        self.weight = weight_in_kg

    def get_exercise_calories(self):
        print("To get calories for the exercise(s), you can type in text like ran 5k and danced for 30 minutes\n")
        exercise_text = input("Tell me which exercises you did\n")

        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age
        }
        print("Retrieving exercise and calories information..........")
        response = requests.post(self.API_ENDPOINT, json=parameters, headers=self.headers)
        status = response.status_code

        if status == 200:
            print("Request successful. parsing data....")
            print(response.json())
        elif status == 404:
            print("Resource not found on server")
        else:
            print("Unable to process request")
