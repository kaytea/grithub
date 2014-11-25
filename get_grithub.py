from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.grubhub.com/search/92_Pearson_Rd_Somerville,_MA_02144_ll_42.403537,-71.115832/')
# print page.text
soup = BeautifulSoup(page.text)
places = [h3.text for h3 in soup.findAll('h3', attrs={'class': 'restaurant-name'})]
print places
#places should return a list of restaurant titles i believe, but returns "[]"
