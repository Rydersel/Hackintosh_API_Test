import requests
import time
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#your API KEY from IFTTT
IFTTTAPIKEY = "your key"  #IFFT API Key
CoinmarketcapAPIKEY = "your key" #Coinmarketcap API Key


def CryptoPriceCheck(Ammount,StartingCur,ConvertingCur):
  url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion' #Rest API Endpoint
  parameters = {
    'amount': Ammount,
   'symbol': ConvertingCur,
   'convert': StartingCur,
  }
  headers = {
   'Accepts': 'application/json', #acception format
   'X-CMC_PRO_API_KEY': CoinmarketcapAPIKEY, #send API Key
  }
  session = Session()
  session.headers.update(headers)
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    CryptoPrice = (data["data"]["quote"][StartingCur]["price"])
    print(ConvertingCur + "is currently equal to " + str(CryptoPrice) +  " " + str(StartingCur))
  except (ConnectionError, Timeout, TooManyRedirects) as e: #Account for if API throws error.
    print(e)
def LightsON(wtime):
  requests.post("https://maker.ifttt.com/trigger/lights_on/with/key/" + IFTTTAPIKEY) #Turn Lights on (Color is whatever color was set to before lights lost power)
  time.sleep(wtime)
def LightsPurple(wtime):
  requests.post("https://maker.ifttt.com/trigger/lights_purple/with/key/" + IFTTTAPIKEY) #Turn Lights Purple
  time.sleep(wtime)
def SendNotification(wtime):
  requests.post("https://maker.ifttt.com/trigger/Notification_Send/with/key/" + IFTTTAPIKEY) #Send Mobile Notification (For Testing)
  time.sleep(wtime)

#Runtime Loop
while True:
  Userstartingcur = input("Please enter your starting currency:")
  UserAmmount = input("Please enter the ammount of this currency you would like to convert:")
  UserConvertingCurrency = input("Please enter the  currency you would like to convert to:")
  CryptoPriceCheck(UserAmmount,Userstartingcur,UserConvertingCurrency) #Grab Price
  time.sleep(1)
  input("Press Enter to Restart...\n") #restarts program





#Action(Ammount of time to wait after trigger)

#Turns Lights On
#LightsON(1)
#Changes lights to purple
#LightsPurple(1)
#Sends Notification to my phone for testing purposes
#SendNotification(1)




