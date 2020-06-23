'''
Sends messages from url.
'''
from selenium import webdriver as wd 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as poel

import time


class WebWSPHandler:

    def __init__(self, user, driver_path='', timeout=600):
        self.profile = user
        self.timeout = timeout  # Timeout in 600 seconds
        self.options = wd.ChromeOptions()
        self.options.add_argument(f'user-data-dir={self.profile}')
        self.driver = wd.Chrome(driver_path, options=self.options)
        self.driver.get('https://web.whatsapp.com/')
        self.wait = None
    
    def pressEnter(self, pages, **kwargs):
        largo = len(pages)
        count = 0
        for page in pages:
            print(f'{count}/{largo}')
            count +=1
            try:
                self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
                self.driver.get(page)
                time.sleep(15)
                sendButton = self.driver.find_elements_by_class_name('_1U1xa')[0]
                sendButton.click()
                self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
                time.sleep(1)
                obj = self.driver.switch_to.alert
                obj.dismiss()
            except Exception as err:
                print(f'{err}\n\n')
                

if __name__ == '__main__':
    data = []
    wsp = WebWSPHandler(user='/home/henry/.config/google-chrome/Default',
                        driver_path='chromedriver')
    wsp.pressEnter(pages=data)
