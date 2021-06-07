import csv


class Coordinator():
    def __init__(self, name="", user_id="", password=""):       # attributter med tomme værdier - gør det muligt at instansiere et tomt objekt
        self.name = name
        self.user_id = user_id
        self.password = password

    def set_name(self, name):       # set metode til at ændre attribut værdi
        self.name = name

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_password(self, password):
        self.password = password

    def get_name(self):     # get metode til at hente attribut værdi
        return self.name


class Windco():
    def __init__(self, country):
        self.country = country


class Windfarm():
    def __init__(self, windfarm_id, name, location, status):
        self.windfarm_id = windfarm_id
        self.name = name
        self.location = location
        self.status = status

    def fetch_all_windmills(self):
        maintenance_count = 0       # tælleren er som standard 0

        with open("windmills.csv", mode="r") as f:      # kigger ned i csv_windfarms fil
            csv_windmills = csv.reader(f, delimiter=",")

            print("\t\t\t\tVindmølle ID\tVedligeholdelse\t\tMegawatt".upper())      # danner tabel header

            for row in csv_windmills:
                if self.windfarm_id in row[3]:      # udvælger de vindmøller der indeholder værdien for windfarm_id i index 3

                    if "True" in row:       # læg 1 til maintenance_count hvis True eksisterer for vindmøllerækken
                        maintenance_count += 1

                    windmill = Windmill(row[0], row[1], row[2], row[3])     # instansiering af Windmill objekt

                    if windmill.maintenance == "True":      # omskriver boolean til forståelig tekst
                        windmill.maintenance = "Ja"
                    elif windmill.maintenance == "False":
                        windmill.maintenance = "Nej"

                    print("\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t{}".format(windmill.windmill_id, windmill.maintenance,
                                                                    windmill.megawatt))     # printer hver række

        if maintenance_count == 0:      # alt afhængig af hvad der er sket med tælleren så print følgende
            print("\n\t\t\t\tIngen vedligeholdelse påkrævet")
        else:
            print("\n\t\t\t\t{} vindmølle(r) skal vedligeholdes!".format(maintenance_count))


class Windmill():
    def __init__(self, windmill_id, maintenance, megawatt, windfarm_id):
        self.windmill_id = windmill_id
        self.maintenance = maintenance
        self.megawatt = megawatt
        self.windfarm_id = windfarm_id


class Crew():
    def __init__(self, crew_id, job_id):
        self.crew_id = crew_id
        self.job_id = job_id


class Maintenance_Job_Calendar():
    def __init__(self, windfarm_id, job_role, date, time, status, responsible):
        self.windfarm_id = windfarm_id
        self.job_role = job_role
        self.date = date
        self.time = time
        self.status = status
        self.responsible = responsible
