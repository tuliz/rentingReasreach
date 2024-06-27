import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

form_url = 'https://forms.gle/RW73kkXaivbHmv7H8'
renting_url = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(url=renting_url)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, 'html.parser')

property_links = soup.find_all(name='a', class_='property-card-link')
property_data_list = soup.find_all(name='div', class_= 'StyledPropertyCardDataWrapper')


proprties_data = []
for property in property_data_list:
    text = property.getText().strip().split('\n')
    address = text[0].split(',')[0]
    price = text[6].split('$')[1].split('+')[0]
    new_data = {'address':address, 'price':price}
    proprties_data.append(new_data)

print(proprties_data)