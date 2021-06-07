


"""
Code of cunduct:
    1. Selve programmet skrives på dansk og kode altid på engelsk
    2. Ordopdeling for klase- funktions/metode- og variabelnavne skrives med _
    3. Alle String omsluttes med "" og ikke ''
    4. Operatører skrives med mellemrum før og efter tegnet
    5. Husk altid forklarende kommentarer i koden
    6. Følg PyCharms automatiske indentering
    7. Ved indlejring af variabler i en String benyttes format() metoden = "{}".format()
    8. Undgå for meget redundant kode
"""
from classes import Windco, Coordinator
from user import login

"""
Bruger guide:
    1. Kør gerne programmer med PyCharm
    2. TIP: Bruger ID: 10
    3. TIP: Adgangskode: 1010
"""

windco = Windco("Danmark")

# instansiering af tomt objekt for Coordinator klassen der er globalt tilgængeligt alle steder i filen
coordinator = Coordinator()


def main():
    login()


main()
