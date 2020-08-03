from selenium import webdriver as wd 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located as poel,
    alert_is_present as aip
)
from selenium.webdriver.common.action_chains import ActionChains as chains
import time


class ExplorerHandler:

    def __init__(self, 
        user=None, 
        driver_path='', 
        timeout=15):

        self.profile = user
        self.timeout = timeout  # Timeout in 600 seconds
        self.options = wd.ChromeOptions()
        if self.profile is not None:
            self.options.add_argument(
                f'user-data-dir={self.profile}'
            )
        self.driver = wd.Chrome(
            driver_path, 
            options=self.options
        )
    
    def click_out(self):
        chains(
            self.driver
        ).move_by_offset(
            50, 
            50
        ).click().perform()

    def open_tab(self):
        chains(
            self.driver
        ).key_down(
            Keys.COMMAND
        ).send_keys(
            't'
        ).key_up(
            Keys.COMMAND
        ).perform()
    
    def close_tab(self):
        chains(
            self.driver
        ).key_down(
            Keys.COMMAND
        ).send_keys(
            'w'
        ).key_up(
            Keys.COMMAND
        ).perform()
    
    def get(self, 
        url, elem_name):

        self.driver.get(
            url
        )
        res = wait(
            self.driver, 
            self.timeout
        ).until(
            poel(
                (
                    By.CLASS_NAME,
                    elem_name
                )
            )
        )

    
    def dismiss_alert(self):
        time.sleep(1)
        if aip()(self.driver):
            alert = self.driver.switch_to.alert
            alert.dismiss()

    def quit_driver(self):
        print('Closing Driver')
        self.driver.quit()
