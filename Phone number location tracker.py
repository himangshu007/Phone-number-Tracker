# print on terminal : "pip install phonenumbers"
import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmbr = phonenumbers.parse(number , "CH")
print(geocoder.description_for_number(ch_nmbr,"en"))

from phonenumbers import carrier 
service_nmbr = phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service_nmbr , "en"))