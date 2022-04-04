from math import radians, cos, sin, asin, sqrt

#COnstants and classes for ATMReader file
#Excel Longitude column
LON_COLUMN = 2
#Excel Latitud column
LAT_COLUMN = 3
#Excel bank column
BANK_COLUMN = 4
#Excel bank net column
NET_COLUMN = 5
#Excel adress column
ADRESS_COLUMN = 6
#Excel Visibility column. In case of running out of money, the visibility will change to False and the atm will not appear until recharged
VISIBILITY = 18 
#Excel Loads column. How many "loads" of money the atm has before running out
LOADS = 19
#Dataset location
PATH = 'Archivos\Dataset2.xlsx'
#Earth radius for distance formula
EARTH_RADIUS = 6371
#Initial distance of user (Since is unkown at first, everyone starts at 0)
INITIAL_DISTANCE = 0

class AtmClass:
    #Latitude - Longitude - Net - Bank Franchise - Street Adress - Visibility - Distance from user point - List Index 
    def __init__(self, lat, lon, net, bank, adress,visibility,distance,index):
        self.lat = lat
        self.lon = lon
        self.net = net
        self.bank = bank
        self.adress = adress
        self.visibility = visibility
        self.distance = distance
        self.index = index
    
    def distance_func(self,lat,lon):
        lon1 = radians(self.lon)
        lon2 = radians(lon)
        lat1 = radians(self.lat)
        lat2 = radians(lat)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles
        r = EARTH_RADIUS
        result = (c * r)/10
        return result


#<--------------------------------------------------------!!!!!!!!!!!!!!!!----------------------------------------------->#

#Position Stack Api Site
POSITION_STACK_API = 'api.positionstack.com'
#Position Stack Access Token
POSTION_ACCESS_KEY = '931321eafe2fbe48fc026685ffc9f88f'

#Map Access token
MAP_API_KEY = "pk.eyJ1IjoibWFyaWFudGFuIiwiYSI6ImNsMWRsNTdnbDA4NW4zZHM1aDVhbndzMm0ifQ.b3nbqlkydBWfjENcfwUAow"
#Available Region for searching
REGION = 'Autonomous City of Buenos Aires'
#Maximum radius of search
MAXIMUM_DISTANCE = 800
#Minimun radius of search
MINIMUM_DISTANCE = 500

#<--------------------------------------------------------!!!!!!!!!!!!!!!!----------------------------------------------->#

#Telegram Bot access token
BOT_API_KEY = '5292798174:AAFGIM7HizlVl-d1Kx2Y1ew_bfi7rVuGDEs'