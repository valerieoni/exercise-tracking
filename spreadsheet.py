import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('exercise-record')
WORKOUT_SHEET = SHEET.worksheet("workouts")
USERS_SHEET = SHEET.worksheet("users")


def get_workouts():
    """
    Reads and returns the data in worksheet containing workouts
    """
    return WORKOUT_SHEET.get_all_values()


def get_users():
    """
    Reads and returns list of users
    """
    return USERS_SHEET.get_all_values()
