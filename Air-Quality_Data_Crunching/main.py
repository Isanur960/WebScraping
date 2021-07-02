#Author : Isanur Sardar

import requests
import csv

st_code = input('Write the station code with inverted comma')
url = 'http://emis.wbpcb.gov.in/airquality/JSP/aq/fetch_val_ajax.jsp'
myobj = {'stn_code': st_code,
         'type': 'date'}

x = requests.post(url, data = myobj)
da = eval(x.text)

main = []
def boxx(x):
  ix = int(x)
  if (x - ix) > 0.5:
    ix = ix +1
  else:
    pass
  return ix
f_name = 'wbpcb-data-IS'+st_code+'.csv'
fxx = open(f_name, 'w', newline='')
writer = csv.writer(fxx)
writer.writerow(["DATE", "NO2","NO2-SI", "PM10","PM10-SI","SO2","SO2-SI"])
dates = da['list']
n = 0
for el in dates:
  date = el['dates']
  date_el = date.split("/")
  day = date_el[1]
  month = date_el[0]
  year = date_el[2]
  if eval(year) < 2010 or eval(year) > 2020 :
    pass
  else:
    try:
      d = day + '/'+ month +'/' + year
      data = { 'stn_code': st_code,
            'date': d,
            'type': 'aqi'}
      #print(data)
      res = requests.post(url, data = data)
      rest = eval(res.text)
      #print(rest)
      NO2 = rest['list'][0]['value']
      vno2 = eval(NO2)
      if (vno2<=40):
        no2si=vno2*50/40
      elif (vno2>40 and vno2<=80):
        no2si=50+(vno2-40)*50/40
      elif (vno2>80 and vno2<=180):
        no2si=100+(vno2-80)*100/100
      elif (vno2>180 and vno2<=280):
        no2si=200+(vno2-180)*100/100
      elif (vno2>280 and vno2<=400):
        no2si=300+(vno2-280)*100/120
      else:
        no2si=400+(vno2-400)*100/120

      PM10 = rest['list'][1]['value']
      vpm10 = eval(PM10)
      if vpm10<=100:
        pm10si=vpm10
      elif vpm10>100 and vpm10<=250:
        pm10si=100+(vpm10-100)*100/150
      elif vpm10>250 and vpm10<=350:
        pm10si=200+(vpm10-250)
      elif vpm10>350 and vpm10<=430:
        pm10si=300+(vpm10-350)*100/80
      else:
        pm10si=400+(vpm10-430)*100/80

      SO2 = rest['list'][2]['value']
      vso2 = eval(SO2)
      if (vso2<=40):
        so2si=vso2*50/40
      elif (vso2>40 and vso2<=80):
        so2si=50+(vso2-40)*50/40
      elif (vso2>80 and vso2<=380):
        so2si=100+(vso2-80)*100/300
      elif (vso2>380 and vso2<=800):
        so2si=200+(vso2-380)*100/420
      elif (vso2>800 and vso2<=1600):
        so2si=300+(vso2-800)*100/800
      else:
        so2si=400+(vso2-1600)*100/800
      texxt = [d, NO2,boxx(no2si), PM10,boxx(pm10si) ,SO2, boxx(so2si)]
      main.append(texxt)
      #try:
      writer.writerow(texxt)
      #print('ok')
      #except:
      #  print("Unexpected error:", sys.exc_info()[0])
    except:
      pass
  n = n +1
  print(n)
