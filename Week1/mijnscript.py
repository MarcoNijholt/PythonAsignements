from Week1.customer import *

##Opdracht 3, maak 2 nieuwe klanten aan
customers = []
customers.append(Customer("Marco Nijholt", "0653466274", "info@marconijholt.com"))
customers.append(Customer("Steve Jobs", "06-56456589", "info@marconijholt.com"))
customers.append(Customer("Bill Gates", "+31625361425", "billy@microsoft.com"))
customers.append(Customer("Billy Goats", "+0015695865641564", "billy@microsoft.com"))


#loopt door de klanten om informatie af te drukken voor controle (onderdeel van meerdere opdrachten))
for customer in customers:
    print(customer) #shows the __str__ works
    print("Name: " + customer.name + ",", "Phone Valid: " + str(customer.checkTelephoneNumber()) + ",", "Customer ID: " + str(customer.id) + ",", "Email Domain: " + str(customer.domain) + "\n") ##shows some more info


#reset password for first user, then print the new password (assignement 7)
customers[0].resetPassword()
print("New password for Customer " + customers[0].name + ": " + customers[0].password)
