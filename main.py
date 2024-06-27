import requests
from rentingdata import RentingData
from formhandler import FormHandler

form_url = 'https://forms.gle/RW73kkXaivbHmv7H8'
renting_url = 'https://appbrewery.github.io/Zillow-Clone/'

# Get the HTML code from the renting website
response = requests.get(url=renting_url)
response.raise_for_status()
data = response.text

# Send the data of the HTML and send to parse it and extract data from it
renting_data_handler = RentingData(data=data)
renting_data_handler.parse_data()

# Send the Data of the rentings exracted and send it to form
form_handler = FormHandler()
form_handler.send_data_to_form(form_url, renting_data_handler.proprties_data)



