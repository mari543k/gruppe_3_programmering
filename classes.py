from functions import *
import csv


class Coordinator():
    def __init__(self, name="", user_id="", password=""):       # attributter med tomme værdier - gør det muligt at instansiere et tomt objekt
        self.name = name
        self.user_id = user_id
        self.password = password

    def set_name(self, name):
        self.name = name

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_user_id(self):
        return self.user_id

    def get_password(self):
        return self.password


class Crew():
    def __init__(self, crew_id, job_id):
        self.crew_id = crew_id
        self.job_id = job_id
        super().__init__(first_name, last_name)


class Windco():
    def __init__(self, windfarm_list):
        self.windfarm_list = windfarm_list

    def fetch_user(self, user_id, password):
        pass

    def fetch_all_windfarms(self):
        pass

    def fetch_crew(self, crew_id):
        pass


class Windfarm():
    def __init__(self, windfarm_id, name, location, status):
        self.windfarm_id = windfarm_id
        self.name = name
        self.location = location
        self.status = status

    def fetch_all_windmills(self):
        maintenance_count = 0

        # kigger ned i csv_windfarms fil
        with open("csv_windmills.csv", mode="r") as f:
            csv_windmills = csv.reader(f, delimiter=",")

            print("\t\t\t\tVindmølle ID\tVedligeholdelse\t\tMegawatt".upper())

            for row in csv_windmills:

                # udtrækker de vindmøller med et matchende windfarm_id
                if self.windfarm_id in row[3]:

                    # læg 1 til maintenance_count hvis True eksisterer for vindmøllen
                    if "True" in row:
                        maintenance_count += 1

                    # danner en ny instans af Windmill klassen
                    windmill = Windmill(row[0], row[1], row[2], row[3])

                    # omskriver boolean til forståelig tekst
                    if windmill.maintenance == "True":
                        windmill.maintenance = "Ja"
                    elif windmill.maintenance == "False":
                        windmill.maintenance = "Nej"

                    print("\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t{}".format(windmill.windmill_id, windmill.maintenance, windmill.megawatt))

        if maintenance_count == 0:
            print("\n\t\t\t\tIngen vedligeholdelse påkrævet")
        else:
            print("\n\t\t\t\t{} vindmølle(r) skal vedligeholdes!".format(maintenance_count))


class Windmill():
    def __init__(self, windmill_id, maintenance, megawatt, windfarm_id):
        self.windmill_id = windmill_id
        self.maintenance = maintenance
        self.megawatt = megawatt
        self.windfarm_id = windfarm_id


class Maintenance_Job_Calendar():
    def __init__(self, windfarm_id, job_role, date, time, status, responsible):
        self.windfarm_id = windfarm_id
        self.job_role = job_role
        self.date = date
        self.time = time
        self.status = status
        self.responsible = responsible

