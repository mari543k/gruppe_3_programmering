from classes import *
import csv


def login():
    print("*" * 75)
    print("\t\t\t\t\t\t\tLog ind på Windco")
    print("*" * 75)

    user_id = input("\t\t\t\tBruger ID: ")
    password = input("\t\t\t\tAdgangskode: ")

    fetch_user(user_id, password)


def fetch_user(user_id, password):
    # kigger ned i csv_users fil
    with open("csv_users.csv", mode="r") as f:
        csv_users = csv.reader(f, delimiter=",")

        for row in csv_users:
            # validerer om user eksisterer
            if user_id and password in row:
                # danner en ny instans af Coordinator klassen
                coordinator = Coordinator(row[0],user_id,password)
                print("")
                # videregiver information til næste funktion
                show_all_windfarms(coordinator)
                return True

    print("\n\t\t\t\t\t\tUgyldigt log ind! Prøv igen\n".upper())
    login()
    return False


def show_all_windfarms(coordinator):
    # kigger på coordinator objektets navn
    name = coordinator.name.upper()

    print("*" * 75)
    print("\t\t\t\t\t\t\t\tHej {}!".format(name))
    print("*" * 75)

    # kigger ned i csv_windfarms fil
    with open("csv_windfarms.csv", mode="r") as f:
        csv_windfarms = csv.reader(f, delimiter=",")

        print("\t\tVindfarm ID\t\tNavn\t\t\tPlacering\tStatus".upper())

        for row in csv_windfarms:
            # omskriver talværdi til forståelig tekst
            if row[3] == "1":
                row[3] = "OK"
            elif row[3] == "2":
                row[3] = "** Warning **"
            elif row[3] == "3":
                row[3] = "** Critical **"

            print("\t\t{}\t\t\t\t{}\t\t{}\t\t{}".format(row[0], row[1], row[2], row[3]))

    print("-" * 75)
    print("\t\t\t\t\t\t\tVælg en handling")
    print("-" * 75)

    # try/except ved int input sørger for programmet ikke stopper
    try:
        user_choice = int(input("\t\t\t\tLog ud (1) \n\t\t\t\tVælg vindfarm (indtast vindfarm ID): "))

        # kigger på brugerens valg og handler derudfra
        if user_choice == 1:
            print("\n\t\t\t\t\t\t\t\tLogger ud...\n".upper())
            login()
        elif user_choice in range(5, 25, 5):
            print("")
            # videregiver information til næste funktion
            show_windfarm_details(user_choice)
        else:
            print("\n\t\t\t\t\t\tUgyldigt valg! Prøv igen\n".upper())
            show_all_windfarms(coordinator)
    except:
        print("\n\t\t\t\t\t\tUgyldigt valg! Prøv igen\n".upper())
        show_all_windfarms(coordinator)


def show_windfarm_details(windfarm_id):
    # konverterer variablen windfarm_id fra int til str så den kan bruges senere til at kigge ned i csv_windfarms filen
    windfarm_id = str(windfarm_id)

    # kigger ned i csv_windfarms fil
    with open("csv_windfarms.csv", mode="r") as f:
        csv_windfarms = csv.reader(f, delimiter=",")

        for row in csv_windfarms:
            # udvælger den række der matcher værdien for windfarm_id
            if windfarm_id in row:

                # danner en ny instans af Windfarm klassen
                windfarm = Windfarm(windfarm_id, row[1], row[2], row[3])

                # omskriver talværdi til forståelig tekst
                if windfarm.status == "1":
                    windfarm.status = "OK"
                elif windfarm.status == "2":
                    windfarm.status = "** Warning **"
                elif windfarm.status == "3":
                    windfarm.status = "** Critical **"

                print("*" * 75)
                print("\t\t\t\t\t\t\t\t{}".format(windfarm.name))
                print("*" * 75)
                print("\t\t\t\tPlacering:\t{}".format(windfarm.location))
                print("\t\t\t\tStatus:\t\t{}".format(windfarm.status))
                print()

                windfarm.fetch_all_windmills()

