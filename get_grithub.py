from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.grubhub.com/search/92_Pearson_Rd_Somerville,_MA_02144_ll_42.403537,-71.115832/')
# print page.text
soup = BeautifulSoup(page.text)
places = [h3.text for h3 in soup.findAll('h3', attrs={'class': 'restaurant-name'})]
# id_num = [li.FIND for li in soup.findAll('li', attrs={'FIND': 'FIND'})]
#    ^^^need to figure out more of how soup is scraping; id contained in obj attr, not txt <li data-restaurant-id="270495"

# class restaurant(object):
#    def __init__(self, id): """holding out on adding arr of food_types for prelim"""
#        self.id = id
#    def goto(self):
#        url = 'https://www.grubhub.com/restaurant/' + self.id
#        rest_page = requests.get(url)
#        rest_soup = BeautifulSoup(page.text)
#
#
# for (i = 0; i < len(places); i++):
#    location[i] = restaurant(places[i], id_num[i])

