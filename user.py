import csv
from functions import h1, fetch_all_windfarms, message
from main import windco, coordinator


def login():
    h1("Velkommen til Windco {}".format(windco.country), 6)

    user_id = input("\t\t\t\tBruger ID: ")
    password = input("\t\t\t\tAdgangskode: ")

    fetch_user(user_id, password)       # videregiver værdier til næste funktion


def fetch_user(user_id, password):
    with open("users.csv", mode="r") as f:      # læser i csv_users fil
        csv_users = csv.reader(f, delimiter=",")

        for row in csv_users:
            if user_id and password in row:     # validerer om rækken eksisterer
                coordinator.set_name(row[0])        # erstatter coordinator objektets tomme værdier med nogle reelle værdier
                coordinator.set_user_id(user_id)
                coordinator.set_password(password)

                print("")
                fetch_all_windfarms()
                return True

    message("Ugyldigt log ind! Prøv igen", 6)
    login()     # starter log ind processen forfra hvis user ikke findes
    return False
