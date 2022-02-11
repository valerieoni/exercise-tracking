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
    gets a list of users from worksheet
    returns the list excluding the
    first row which is the column names
    """
    users = USERS_SHEET.get_all_values()
    return users[1:]


def update_users_worksheet(data):
    """
    updates the users worksheet, and adds
     a new row with the list data provided
    """
    print("Updating users worksheet.......\n")
    USERS_SHEET.append_row(data)
    print("users worksheet successfully updated.\n")


def update_workout_worksheet(data):
    """
    updates the workouts worksheet, and adds
     a new row with the list data provided
    """
    print("Updating workout worksheet.......\n")
    WORKOUT_SHEET.append_rows(data)
    print("workout successfully added to the workout worksheet.\n")

