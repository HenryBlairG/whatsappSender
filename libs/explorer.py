from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    UnexpectedAlertPresentException as UnAlPr,
    TimeoutException as To
)
from selenium.webdriver.common.action_chains import (
    ActionChains as chains
)
from selenium.webdriver.support.ui import (
    WebDriverWait as wait
)
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located as poel,
    alert_is_present as aip,
)


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
            Keys.CONTROL
        ).send_keys(
            't'
        ).key_up(
            Keys.CONTROL
        ).perform()

    def close_tab(self):
        chains(
            self.driver
        ).key_down(
            Keys.CONTROL
        ).send_keys(
            'w'
        ).key_up(
            Keys.CONTROL
        ).perform()

    def get(self,
        url, elem_name):
        self.driver.get(
            url
        )
        self.accept_alert()
        return self.get_wait(elem_name)   
    
    def get_wait(self, elem_name, wait_timeout=None):
        if wait_timeout is None:
            wait_timeout = self.timeout
        try:
            wait(
                self.driver,
                wait_timeout
            ).until(
                poel(
                    (
                        By.CLASS_NAME,
                        elem_name
                    )
                )
            )
            return True
        except To:
            return False

    def dismiss_alert(self):
        if aip()(self.driver):
            alert = self.driver.switch_to.alert
            alert.dismiss()

    def accept_alert(self):
        if aip()(self.driver):
            alert = self.driver.switch_to.alert
            alert.accept()

    def quit_driver(self):
        print('Closing Driver')
        self.driver.quit()
