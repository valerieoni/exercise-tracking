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

def get_user_workouts(user_name):
    """
    get workouts from workouts worksheet
    filter result to retrieve and return the
    workouts data for the user_name passed in.
    """
    print("Fetching workouts record.......")
    workouts = WORKOUT_SHEET.get_all_values()
    user_workouts = []
    for workout in workouts[1:]:
        if workout[0] == user_name:
            user_workouts.append(workout[1:])
    return user_workouts

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

def is_existing_user(user_name) -> bool:
    """
    gets the lists of users from the worksheet,
    extracts the first column which is the username and
    returns true if username is in the list, returns false otherwise
    """
    users = get_users()
    user_names = [user[0] for user in users]
    return user_name in user_names


def get_user(user_name: str):
    """
    Returns a dictionary object of the user's profile
    if user exists otherwise it returns None
    """
    users = get_users()
    for user in users:
        if user[0] == user_name:
            return {
                'user_name': user[0],
                'date_created': user[1],
                'gender': user[2],
                'age': user[3],
                'weight': user[4],
                'height': user[5]
            }

    return None
