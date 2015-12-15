__author__ = 'marco'
import sqlite3, random
conn = sqlite3.connect('randomNumbers.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE nummers
#              (getal INTEGER)''')

# Insert the random numbers
# randomBytes = random.SystemRandom()
# for x in range(0,1000):
#     print(randomBytes.randint(1, 499))
#     c.execute("INSERT INTO nummers VALUES ('" + str(randomBytes.randint(1, 499)) + "')")

c.execute("SELECT sum(getal), avg(getal), min(getal), max(getal) FROM nummers")

response = c.fetchall()
print("Alle getallen opgeteld is: " + str(response[0][0]))
print("Gemiddelde van de getallen: " + str(response[0][1]))
print("Minimum: " + str(response[0][2]))
print("Maximum: " + str(response[0][3]))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
