from functions import *
import csv

class Coordinator():
    def __init__(self, first_name, last_name, user_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.password = password


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
    def __init__(self, windfarm_id, location, windmill_list, maintenance_total=0, status="OK"):
        self.windfarm_id = windfarm_id
        self.location = location
        self.windmill_list = windmill_list
        self.maintenance_total = maintenance_total
        self.status = status

    def fetch_all_windmills(self):
        pass


class Windmill():
    def __init__(self, windmill_id, maintenance=False):
        self.windmill_id = windmill_id
        self.maintenance = maintenance


class Maintenance_Job_Calendar():
    def __init__(self, windfarm_id, job_role, date, time=0, status="OK"):
        self.windfarm_id = windfarm_id
        self.job_role = job_role
        self.date = date
        self.time = time
        self.status = status