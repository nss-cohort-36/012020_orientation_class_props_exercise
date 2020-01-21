# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

#     Social security number
#     Date of birth
#     Health insurance account number
#     First name
#     Last name
#     Address

# The first three properties should be read-only.
class Patient:

    def __init__(self, ssn, dob, hin, first_name, last_name, address):
        self.__dob = dob
        self.__ssn = ssn
        self.__hin = hin
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def ssn(self):
        return self.__ssn

    @property
    def dob(self):
        return self.__dob

    @property
    def hin(self):
        return self.__hin

# First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name.

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

# Address should have a getter and setter.
    @property
    def address(self):
      return self.__address

    @address.setter
    def address(self, new_address):
      if type(new_address) is str:
          self.__address = new_address
      else:
          raise TypeError("WTF?")


bubba = Patient(404044404, "09/22/1967", 1234567, "Bubba", "Sparkle", "213 Sesame St")

# bubba.address = 12345 <-- Throws error!

print(bubba.ssn, bubba.full_name, bubba.address)
