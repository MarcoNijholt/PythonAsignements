import csv
import random
from datetime import date

try:
    with open("klantgegevens.csv") as csvfile:
        klantgegevensReader = csv.DictReader(csvfile, delimiter=";")
        for row in klantgegevensReader:
            print("Voornaam:",row["Naam"] + ",", "E-mail:", row["E-Mail"])
except IOError:
    print("Kon klantgegevens.csv niet openen, bekijk of dit bestand al wel bestaat")
except PermissionError:
    print("Kon writeTest.csv niet openen, bekijk of dit bestand niet geopened is in een ander programma")
except:
    print("Er is iets fout gegaan tijdens het lezen van de CSV bestand, is het wel in CSV format?")


try:
    with open('writeTest.csv', 'wt') as csvfile:
        header = ['Id', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=header, dialect="excel", delimiter=";", lineterminator="\n")
        writer.writeheader()

        for i in range(1, 101):
            randomBytes = random.SystemRandom()
            writer.writerow({'Id': str(i), 'Value': str(randomBytes.randint(0, 10000))})
except IOError:
    print("Kon writeTest.csv niet openen, bekijk of dit bestand al wel bestaat")
except PermissionError:
    print("Kon writeTest.csv niet openen, bekijk of dit bestand niet geopened is in een ander programma")
except:
    print("Er is iets fout gegaan tijdens het genereren en schrijven van de waardes naar het CSV beestand")


try:
    with open("klantgegevens.csv") as csvfile:
        klantgegevensReader = csv.DictReader(csvfile, delimiter=";")
        try:
            csvCombined = open('csvCombined.csv', 'wt')
            header = ['Naam', 'Geboortejaar', 'E-Mail', "Telefoonnummer", "Leeftijd", "Password", "Klantnummer", "Username"]
            combinedWriter = csv.DictWriter(csvCombined, fieldnames=header, dialect="excel", delimiter=";", lineterminator="\n")
            combinedWriter.writeheader()
            customerNumber = 1
            for row in klantgegevensReader:
                #calculate age
                leeftijd = date.today().year - int(row["Geboortejaar"])
                #generate random password
                randomBytes = random.SystemRandom()
                availableCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
                password = ""
                for i in range(0, 8):
                    password += availableCharacters[randomBytes.randint(0, len(availableCharacters))-1]
                #generate customer id
                klantnummer = str(customerNumber)
                customerNumber += 1
                username = row["Naam"] + row["Geboortejaar"]
                combinedWriter.writerow({'Naam': row["Naam"], 'Geboortejaar': row["Geboortejaar"], 'E-Mail': row["E-Mail"], "Telefoonnummer": row["Telefoonnummer"], "Leeftijd": leeftijd, "Password": password, "Klantnummer": klantnummer, "Username": username})
        except IOError:
            print("Kon csvCombined.csv niet openen, bekijk of dit bestand al wel bestaat")
        except PermissionError:
            print("Kon csvCombined.csv niet openen, bekijk of dit bestand niet geopened is in een ander programma")
        except:
            print("Er is iets fout gegaan tijdens het genereren en schrijven van de waardes naar het CSV beestand")
except IOError:
    print("Kon klantgegevens.csv niet openen, bekijk of dit bestand al wel bestaat")
except PermissionError:
    print("Kon klantgegevens.csv niet openen, bekijk of dit bestand niet geopened is in een ander programma")



