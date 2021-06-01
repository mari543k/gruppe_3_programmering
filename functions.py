from classes import *
import csv


def login():
    print("*" * 75)
    print("\t\t\t\t\t\t\tLog ind på Windco")
    print("*" * 75)

    user_id = input("\t\t\t\tBruger ID: ")
    password = input("\t\t\t\tAdgangskode: ")

    with open("csv_users.csv", mode="r") as f:
        csv_users = csv.reader(f, delimiter=",")

        for user in csv_users:
            if user_id and password in user:
                print("")
                show_all_windfarms(user)
                return True

    print("\n\t\t\t\t\t\tUgyldigt log ind! Prøv igen\n".upper())
    login()
    return False


def show_all_windfarms(user):
    name = user[0].upper()

    print("*" * 75)
    print("\t\t\t\t\t\t\t\tHej {}!".format(name))
    print("*" * 75)

    # TODO indsæt vindfarm overblik her

    print("")
    print("-" * 75)
    print("\t\t\t\t\t\t\tVælg en handling")
    print("-" * 75)

    try:
        user_choice = int(input("\t\t\t\tLog ud (1) \n\t\t\t\tVælg vindfarm (indtast vindfarm ID): "))

        if user_choice == 1:
            print("\n\t\t\t\t\t\t\t\tLogger ud...\n".upper())
            login()
        elif user_choice in range(5, 25, 5):
            print("")
            show_windfarm_details(user_choice)
        else:
            print("\n\t\t\t\t\t\tUgyldigt valg! Prøv igen\n".upper())
            show_all_windfarms(user)
    except:
        print("\n\t\t\t\t\t\tUgyldigt valg! Prøv igen\n".upper())
        show_all_windfarms(user)


def show_windfarm_details(windfarm):
    pass
