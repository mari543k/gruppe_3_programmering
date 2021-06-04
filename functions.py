from classes import *
import csv


coordinator = Coordinator()     # instansiering af tomt objekt for Coordinator klassen der er globalt tilgængeligt alle steder i filen


def login():
    h1("Velkommen til Windco", 7)

    user_id = input("\t\t\t\tBruger ID: ")
    password = input("\t\t\t\tAdgangskode: ")

    fetch_user(user_id, password)       # videregiver værdier til næste funktion


def fetch_user(user_id, password):
    with open("csv_users.csv", mode="r") as f:      # læser i csv_users fil
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


def fetch_all_windfarms():
    h1("Hej {}!".format(coordinator.get_name().upper()), 8)        # henter coordinator objektets navn og bruger det i overskriften

    with open("csv_windfarms.csv", mode="r") as f:      # læser csv_windfarms fil
        csv_windfarms = csv.reader(f, delimiter=",")

        print("\tVindfarm ID\t\tNavn\t\t\t\tPlacering\tStatus".upper())       # danner tabel header

        for row in csv_windfarms:
            if row[3] == "1":       # omskriver talværdi til forståelig tekst
                row[3] = "OK"
            elif row[3] == "2":
                row[3] = "* Advarsel *"
            elif row[3] == "3":
                row[3] = "** Kritisk **"

            print("\t{}\t\t\t\t{}\t\t{}\t\t{}".format(row[0], row[1], row[2], row[3]))        # printer hver række

    select_windfarm()


def select_windfarm():
    h2("Vælg en handling", 7)

    try:        # try/except ved int input sørger for programmet ikke stopper hvis ugyldig værdi indtastes
        choice = int(input("\t\t\t\tLog ud (1) \n\t\t\t\tVælg vindfarm (indtast vindfarm ID): "))

        if choice == 1:     # kigger på brugerens valg og handler derudfra
            message("Logger ud....", 8)
            login()
        elif choice in range(10, 30, 5):        # kigger om brugeren har indtastet et værdi fra 5 til 30 med et hop på 5
            print("")
            fetch_windfarm(choice)     # videregiver værdi til næste funktion
        else:
            message("Ugyldigt valg! Prøv igen", 6)
            fetch_all_windfarms()
    except Exception as e:
        message("Ugyldigt valg! Prøv igen", 6)
        fetch_all_windfarms()


def fetch_windfarm(windfarm_id):
    windfarm_id = str(windfarm_id)      # konverterer variablen windfarm_id fra int til str så den kan bruges senere til at kigge ned i csv_windfarms filen

    with open("csv_windfarms.csv", mode="r") as f:      # kigger ned i csv_windfarms fil
        csv_windfarms = csv.reader(f, delimiter=",")

        for row in csv_windfarms:
            if windfarm_id in row[0]:      # udvælger den række der indeholder værdien for windfarm_id i index 0

                windfarm = Windfarm(windfarm_id, row[1], row[2], row[3])        # instansiering af Windfarm objekt

                if windfarm.status == "1":      # omskriver talværdi til forståelig tekst
                    windfarm.status = "OK"
                elif windfarm.status == "2":
                    windfarm.status = "** Advarsel **"
                elif windfarm.status == "3":
                    windfarm.status = "** Kritisk **"

    h1(windfarm.name, 6)       # indsætter navnet for vinfarmen i overskrift
    print("\t\t\t\tPlacering:\t{}".format(windfarm.location))       # printer flere værdier for vindfarmen ud
    print("\t\t\t\tStatus:\t\t{}".format(windfarm.status))

    print("")
    windfarm.fetch_all_windmills()      # eksekverer klassemetode

    h2("Vælg en handling", 7)

    try:    # try/except ved int input sørger for programmet ikke stopper
        user_choice = int(input("\t\t\t\tTilbage til hovedmenu (1) \n\t\t\t\tSe kalender (2) \n\t\t\t\tOpret vedligeholdelses opgave (3): "))

        if user_choice == 1:        # kigger på brugerens valg og handler derudfra
            print("")
            fetch_all_windfarms()
        elif user_choice == 2:
            print("")
            request_maintenance_calendar(windfarm_id)      # videregiver værdi til næste funktion
        elif user_choice == 3:
            request_maintenance(windfarm_id)        # videregiver værdi til næste funktion
        else:
            message("Ugyldigt valg! Prøv igen", 6)
            fetch_windfarm(windfarm_id)
    except:
        message("Ugyldigt valg! Prøv igen", 6)
        fetch_windfarm(windfarm_id)


def request_maintenance_calendar(windfarm_id):
    h1("Kalenderoversigt", 7)

    with open("csv_calendar.csv", mode="r") as f:       # kigger ned i csv_calendar fil
        csv_calendar = csv.reader(f, delimiter=",")

        print("\tDato\t\t\tTidspunkt\tOpgavetype\t\tAnsvarlig\tStatus".upper())     # danner tabel header

        for row in csv_calendar:
            if windfarm_id in row[0]:      # udvælger den række der indeholder værdien for windfarm_id i index 0

                if row[4] == "1":       # omskriver talværdi til forståelig tekst
                    row[4] = "Afsluttet"
                elif row[4] == "2":
                    row[4] = "Igangværende"
                elif row[4] == "3":
                    row[4] = "** Afventer **"

                print("\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}".format(row[3], row[2], row[1], row[5], row[4]))      # printer hver række

    h2("Vælg en handling", 7)

    try:        # try/except ved int input sørger for programmet ikke stopper
        choice = int(input("\t\t\t\tTilbage til hovedmenu (1) \n\t\t\t\tTilbage til vindfarm (2) \n\t\t\t\tOpret vedligeholdelses opgave (3): "))

        if choice == 1:     # kigger på brugerens valg og handler derudfra
            print("")
            fetch_all_windfarms()
        elif choice == 2:
            print("")
            fetch_windfarm(windfarm_id)
        elif choice == 3:
            print("")
            request_maintenance(windfarm_id)
        else:
            message("Ugyldigt valg! Prøv igen", 6)
            request_maintenance_calendar(windfarm_id)
    except:
        message("Ugyldigt valg! Prøv igen", 6)
        request_maintenance_calendar(windfarm_id)


def request_maintenance(windfarm_id):
    h1("Opret opgave", 7)

    fetch_crew()

    job_role = input("\n\t\t\t\t\t\tVælg opgavenr.: ")

    if job_role == "1":     # omskriver talværdi til passende tekst
        job_role = "Tekniker"
    elif job_role == "2":
        job_role = "Brandmand"
    elif job_role == "3":
        job_role = "Håndværker"
    elif job_role == "4":
        job_role = "Elektriker"
    elif job_role == "5":
        job_role = "Ingeniør"
    else:
        message("Ugyldigt valg! Prøv igen", 6)
        request_maintenance(windfarm_id)

    date = input("\t\t\t\t\t\tIndtast dato (dd-mm-yyyy): ")
    time = input("\t\t\t\t\t\tIndtast tidspunkt (hh:mm): ")

    task = Maintenance_Job_Calendar(windfarm_id, job_role, date, time, "3", coordinator.name)       # instansiering af Maintenance_Job_Calendar objekt

    update_calendar(task.windfarm_id, task.job_role, task.date, task.time, task.status, task.responsible)       # videregiver værdier til næste funktion


def fetch_crew():
    with open("csv_crew.csv", mode="r") as f:       # kigger ned i csv_crew fil
        csv_crew = csv.reader(f, delimiter=",")

        h2("Nr.\t\tOpgavetype".upper(), 6)     # danner tabel header

        for row in csv_crew:
            crew = Crew(row[0], row[1])     # instansiering af Crew objekt

            print("\t\t\t\t\t\t{}\t\t{}".format(crew.crew_id, crew.job_id))     # printer hver række


def update_calendar(windfarm_id, job_role, time, date, status, responsible):
    with open("csv_calendar.csv", mode="a", newline="") as f:       # åbner csv_calendar filen i "a" mode - giver mulighed for tilføje til filen
        csv_calendar = csv.writer(f, delimiter=",")
        csv_calendar.writerow([windfarm_id, job_role, time, date, status, responsible])       # skriver ny række til filen med de angivne værdier

    message("Opgaven er nu oprettet!", 6)
    request_maintenance_calendar(windfarm_id)


# funktion der forebygger redundant kode
def h1(text, tabs):
    text = text
    tabs = "\t" * tabs

    print("*" * 75)
    print("{}{}".format(tabs, text))
    print("*" * 75)


# funktion der forebygger redundant kode
def h2(text, tabs):
    text = text
    tabs = "\t" * tabs

    print("-" * 75)
    print("{}{}".format(tabs, text))
    print("-" * 75)


# funktion der forebygger redundant kode
def message(text, tabs):
    text = text
    tabs = "\t" * tabs

    print("\n{}{}\n".format(tabs, text).upper())
