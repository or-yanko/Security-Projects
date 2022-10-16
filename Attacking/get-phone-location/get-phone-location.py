import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


number = input('Enter phonenumber to detect:\t')
if number == '':
    number = '0544565557'
if number[0] == '0':
    number = '+972' + number[1:]

z = phonenumbers.parse(number, None)
if phonenumbers.is_possible_number(z) == False or phonenumbers.is_valid_number(z) == False:
    print(f"number '{number}' is not a valid number!")


ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, 'en'))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, 'en'))

gb_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_number))
