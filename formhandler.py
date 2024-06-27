from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class FormHandler:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def send_data_to_form(self, url, data_list):

        self.driver.get(url)

        for data in data_list:
            # Get the input fields for address, price and link
            address_input = self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            url_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            # send the values of address, price and link to the input fields
            time.sleep(3)
            address_input.send_keys(data['address'])
            price_input.send_keys(data['price'])
            url_input.send_keys(data['link'])

            # Get the Send button and click it
            send_btn = self.driver.find_element(By.XPATH, '//span[contains(text(), "שליחה")]')
            send_btn.click()

            # Go to another form sending while in loop
            another_send = self.driver.find_element(By.XPATH, '//a[contains(text(), "שליחת תגובה נוספת")]')
            another_send.click()

        self.driver.close()