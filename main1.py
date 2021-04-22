import phonenumbers
from test import number
from text import text1
from phonenumbers import timezone

from phonenumbers import geocoder


ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
num=phonenumbers.parse(number)

# This will print the phone number and
# it's basic details.
print(num)

# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(num)

# It print the timezone of a phonenumber
print(timeZone)


# Pass the text and country code to the below function
numbers = phonenumbers.PhoneNumberMatcher(text1, "IN")

# Printing the phone numbers matched with country code
# and also the indexes of the phone numbers in the string input
for number in numbers:
    print(number)

# Validating a phone number
valid = phonenumbers.is_valid_number(num)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(num)

# Printing the output
print(valid)
print(possible)