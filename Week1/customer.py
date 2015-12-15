import re
import random

class Customer():
    """This class is about the customer fields and methods (opdracht 1)"""
    next_id = 1000

    def __init__(self, name="NONE", phoneNumber="NONE", mailAddress="NONE"):
        """"Initializes the basic customer data into the class (opdracht 2)"""
        self.name = name
        self.phoneNumber = phoneNumber
        self.mailAddress = mailAddress
        self.id = Customer.next_id
        self.domain = self.__getEmailDomain()
        self.password = "welkom"

        Customer.next_id += 1

    def checkTelephoneNumber(self):
        """Check if a phonenumber is a dutch phone number (Opdracht 4)"""
        dutchPhoneRegex = "^(((\\+31|0|0031)6){1}[-]?[1-9]{1}[0-9]{7})$"
        if re.match(dutchPhoneRegex, self.phoneNumber) is not None:
            return True
        else:
            return False

    def __getEmailDomain(self):
        """Grab the domain name from the users email address"""
        email = self.mailAddress
        domainSearchRegex = "@[\w.]+"
        domain = re.search(domainSearchRegex, email).group().replace("@", "")

        return domain

    def resetPassword(self):
        """Reset a users password to a random 8 character string password."""
        randomBytes = random.SystemRandom()
        availableCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
        newPassword = ""
        for i in range(0, 8):
            newPassword += availableCharacters[randomBytes.randint(0,len(availableCharacters))]
        self.password = newPassword
        return True

    def __str__(self):
        """Creates a printable object value for the customer object."""
        return("Naam: " + self.name + ", Adres: " + self.mailAddress + ", Telefoonnummer: " +  self.phoneNumber)