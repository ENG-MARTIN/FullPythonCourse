from geopy.geocoders import Nominatim

geolocator= Nominatim(user_agent="geoapiExercides")

place=input("Enter your village name: ")

location=geolocator.geocode(place)
print(location)