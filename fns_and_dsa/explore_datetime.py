import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date.replace(microsecond=0)


current_date = display_current_datetime()
print("Current date and time:", current_date)

user_input = int(
    input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = timedelta(days=user_input) + current_date
    return future_date.replace(microsecond=0)


print("Future date:", calculate_future_date())
