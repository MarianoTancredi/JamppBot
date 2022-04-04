import requests
import http.client, urllib.parse
import json
from atmreader import reduce_load
from random import randrange
from constants import POSITION_STACK_API,MAP_API_KEY,REGION,MAXIMUM_DISTANCE,MINIMUM_DISTANCE,POSTION_ACCESS_KEY


#Map function: Uses the selected ATMS and the user latitud and longitude
#Doesnt return anything. Just creates a Static map with the pointers
def mapa(atms,center_lat,center_lon):
   #Depending on the amount of possible ATMS, the url changes for more markers
   amount = len(atms)
   if(amount == 1):
      base_url = ('https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/geojson'
               '(%7B%22type%22%3A%22FeatureCollection%22%2C%22features%22%3A%5B%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23462eff%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[0].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[0].lon},{atms[0].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23b0857d%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22y%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{center_lon},{center_lat}%5D%7D%7D%5D%7D)/{center_lon},{center_lat},13/600x400?'
               'access_token=') 
   
   if(amount == 2):
      base_url = ('https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/geojson'
               '(%7B%22type%22%3A%22FeatureCollection%22%2C%22features%22%3A%5B%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23462eff%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[0].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[0].lon},{atms[0].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23e99401%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[1].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[1].lon},{atms[1].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23b0857d%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22y%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{center_lon},{center_lat}%5D%7D%7D%5D%7D)/{center_lon},{center_lat},13/600x400?'
               'access_token=') 

   if(amount == 3):
      base_url = ('https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/geojson'
               '(%7B%22type%22%3A%22FeatureCollection%22%2C%22features%22%3A%5B%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23462eff%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[0].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[0].lon},{atms[0].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23e99401%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[1].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[1].lon},{atms[1].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23e99401%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22{atms[2].net[0].lower()}%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{atms[2].lon},{atms[2].lat}%5D%7D%7D%2C%7B%22type%22%3A%22Feature%22%2C%22properties%22%3A%7B%22'
               f'marker-color%22%3A%22%23b0857d%22%2C%22marker-size%22%3A%22small%22%2C%22marker-symbol%22%3A%22y%22%7D%2C%22geometry%22%3A%7B%22type%22%3A%22Point%22%2C%22coordinates%22%3A%5B{center_lon},{center_lat}%5D%7D%7D%5D%7D)/{center_lon},{center_lat},13/600x400?'
               'access_token=') 
   
   URL = base_url + MAP_API_KEY
   response = requests.get(URL)
   # storing the response in a file (image)
   with open(f'map.png', 'wb') as file:
      # writing data into the file
      file.write(response.content)
   file.close()


#Maximum Distance Function: With the possible Atms in a list, and the user latitude and longitude, calculates the distance of
#each ATM from the user. Then they are selected if under 500 meters radius. In case none of them are, the distance is increased
#to 600, up until 800. If none of them are near by that distance, then the result is zero.
def maximum_distance(atms_list,lat_user,lon_user):
      distances = []
      sorted_atms = []
      for atm in atms_list:
         result = atm.distance_func(lat_user,lon_user)
         atm.distance = result
         distances.append(result)

      found = False
      minimum_distance = MINIMUM_DISTANCE
      while(minimum_distance <=MAXIMUM_DISTANCE and not found):
         for index,result in enumerate(distances):
            if result < minimum_distance:
               sorted_atms.append(atms_list[index])
               found = True
         
         if not found:
            minimum_distance += 100
      if(len(sorted_atms)>0):
         sorted_atms.sort(key=lambda x: x.distance,reverse=False)
      return sorted_atms

#Possible selection function: Picks a random numer from 1 to 100. If the number is bigger than 30(1 in 70), the nearest ATM
#is selected for extraction. In case the number is less than 20(1 in 20) the second nearest ATM is selected. The only case
#left is that the number is between 20-30(1 in 10), so in that case the farthest is selected.
#Note: In case there is only one available, it goes with the first if, the same goes for the second if statement
def possible_selection(atm_list):
   selection_percentage = randrange(1,100)
   
   if(selection_percentage>=30 or len(atm_list) == 1):
      reduce_load(atm_list[0].index)
   elif(selection_percentage<=20 or len(atm_list) == 2):
      reduce_load(atm_list[1].index)
   else:
      reduce_load(atm_list[2].index)


#Map function: With the user latitud and longitude, we use the search query from the KD Tree to search for the 3 nearest points.
#We need that the KD tree is passed as an argument to the function
def map(tree,lon_user,lat_user,atms):
   location = tree.query([(lon_user,lat_user)],k=3)
   location = location[1][0]
   atms_list = []
   
   #Check visibility of ATM to see if we have to remove one of the options
   for index in location:
      if(atms[index].visibility):
         atms_list.append(atms[index])
   
   atms_list = maximum_distance(atms_list,lat_user,lon_user)
   if(len(atms_list)>0):
      possible_selection(atms_list)
      mapa(atms_list,lat_user,lon_user)
   
   return atms_list
   

#Locality Function: With the user latitud and longitude, we can check first if the location he/she send us, is really in CABA   

def localidad(lat,lon):
   conn = http.client.HTTPConnection(POSITION_STACK_API)
   params = urllib.parse.urlencode({
      'access_key': POSTION_ACCESS_KEY,
      'query': f'{lat},{lon}',
      })

   conn.request('GET', '/v1/reverse?{}'.format(params))

   res = conn.getresponse()
   json1 = json.load(res)
   city =  json1["data"][0]["region"]
   if city == REGION:
      return True
   return False

# HTTP request
