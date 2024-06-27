from bs4 import BeautifulSoup

class RentingData:
    def __init__(self,data):
        self.soup = BeautifulSoup(data, 'html.parser')
        self.proprties_data = []

    def parse_data(self):
        # Get all thr Tags that have href with the link for property in them
        property_links = self.soup.find_all(name='a', class_='property-card-link')
        # Get all the tags that have the property info (address and price)
        property_data_list = self.soup.find_all(name='div', class_='StyledPropertyCardDataWrapper')

        for n in range(len(property_data_list)):
            # Get rid of the spaces and split to list
            text = property_data_list[n].getText().strip().split('\n')

            address = text[0]
            # there is only one time with the second item in index 1 that the index of the price is diffrent
            price = text[7 if n == 1 else 6].split('$')[1].split('+')[0]
            url = property_links[n].get('href')

            new_data = {'address': address, 'price': price, 'link': url}
            self.proprties_data.append(new_data)