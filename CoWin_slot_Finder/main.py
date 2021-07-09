#Author : Isanur Sardar
import requests

date = input("Write the date in the format(including inveerted comma) : 'dd-mm-yyyy'  :: ")
pin = str(input('Write the Pincode of your area in the format : XXXXXX  :: '))
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pin+'&date='+date
response = requests.get(url)
dat = eval(response.text)

avl_centers = dat['centers']
for cent in avl_centers:
  name = cent['name']
  av = cent['sessions'][0]['available_capacity']
  min_age = cent['sessions'][0]['min_age_limit']
  print(name ,'--', min_age, '--', av)
