from functions import *
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


class Crew():
    def __init__(self, crew_id, job_id):
        self.crew_id = crew_id
        self.job_id = job_id
        super().__init__(first_name, last_name)


class Windco():
    def __init__(self, country):
        self.country = country
