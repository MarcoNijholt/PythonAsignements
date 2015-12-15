__author__ = 'marco'
import matplotlib.pyplot as grafiek
import csv

# #1
# grafiek.plot([1,2,4,9,16,25,36,1])
# grafiek.show()
#
# #2
# grafiek.plot([10,10,10,30,20,25,30,35,70,75,80,10])
# grafiek.ylabel('Gemiddelde belasting per uur in %')
# grafiek.show()
#
# #3
# belastingTijden = [7,8,9,10,11,12,13,14,15,16,17,18]
# belastingWaarden = [10,10,10,30,20,25,30,35,70,75,80,10]
# grafiek.plot(belastingTijden,belastingWaarden, label="CPU Belasting")
# grafiek.ylabel('Belasting percentage')
# grafiek.xlabel('Uren')
# grafiek.axis([min(belastingTijden),max(belastingTijden),0,100])
# grafiek.grid(True)
# grafiek.annotate('Wat gebeurt hier?!', xy=(17, max(belastingWaarden)), xytext=(13, max(belastingWaarden)+3), arrowprops=dict(facecolor="black", shrink=0.05),)
# grafiek.title("Gemiddelde CPU belasting per uur")
# legend = grafiek.legend(loc='upper center', shadow=True, fontsize='x-large')
#
# grafiek.show()
#

#4
csvDataContainer = []
osInfoContainer = []
test123
# try:
with open("topOperatingSystems.csv") as csvfile:
    operatingSystemsData = csv.DictReader(csvfile, delimiter=",")

    for row in operatingSystemsData:
        csvDataContainer.append(row)
    counter = 0


#generate datastructure
    for key, value in csvDataContainer[0].items():
        if key != "" and key != "Date":
            #print(key, value)
            osInfoContainer.append({"values": [], "osName": key})
            counter += 1

#generate the valuess
    for row in csvDataContainer:
        counter = 0
        for key, value in row.items():
            if key != "" and key != "Date":
                #print(key, value)
                osInfoContainer[counter]["values"].append(value)
                counter += 1

print(osInfoContainer)





#
# except IOError:
#     print("Kon klantgegevens.csv niet openen, bekijk of dit bestand al wel bestaat")
# except PermissionError:
#     print("Kon writeTest.csv niet openen, bekijk of dit bestand niet geopened is in een ander programma")
# except:
#     print("Er is iets fout gegaan tijdens het lezen van de CSV bestand, is het wel in CSV format?")




#5