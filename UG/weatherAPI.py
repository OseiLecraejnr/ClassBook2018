import pyowm
from pyowm import OWM, timeutils


print 'World Weather 1.0'
print 'welcome to the guess game .please enter your details to continue'



print 'WHAT IS YOUR NAME' 
d =raw_input("The Enter your NAME: ")

print 'Which countryu are you in??' 
f =raw_input("The Enter your country: ")

print 'Which city are you in??' 
e =raw_input("The Enter your city: ")


owm = pyowm.OWM('7f80366080690181e5bea3a30e76efd7')
observation = owm.weather_at_place(f+","+e)
w = observation.get_weather()


 
wind = w.get_wind()
humid = w.get_humidity()
temperature = w.get_temperature('celsius')
rain = w.get_rain()




print 'weather in ',e,' and ',f 
print wind
print humid
print temperature
print rain


from pprint import pprint
import requests

API_key = "7f80366080690181e5bea3a30e76efd7"
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=' + API_key)
pprint(r.json())


