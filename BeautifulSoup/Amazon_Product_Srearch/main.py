import urllib.parse
import requests
from bs4 import BeautifulSoup
item = input('Write the desire search item..... - ')
item_enc = urllib.parse.quote(item)
url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + item_enc
x = requests.post(url)
soup = BeautifulSoup(x.content, 'html.parser')
all = soup.find_all(class_="celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results")
for el in all:
  soup_name = BeautifulSoup(str(el), 'html.parser')
  name = soup_name.find_all(class_="a-size-medium a-color-base a-text-normal")[0].get_text()
  link ='https://www.amazon.in' + soup_name.find_all(class_="a-link-normal a-text-normal", href=True)[0]['href']
  try:
    price = soup_name.find_all(class_="a-price-whole")[0].get_text()
  except:
    pass
  print(name,'-',price,'-',link)
