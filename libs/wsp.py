"""
Sends messages from url.
"""
import libs.explorer as xp
import time


class WebWSP(xp.ExplorerHandler):

    BODY_CHAT_NAME = '_13NKt copyable-text selectable-text'
    CONTENT_TIMEOUT = 5
    INVALID_NUM_MESG = 'El número de teléfono compartido a través de la dirección URL es inválido'
    INVALID_NUM_NAME = '_2Nr6U'
    PROFILE_PHOTO_NAME = '_1lPgH'
    SEND_BUTTON_NAME = '_4sWnG'
    START_URL = 'https://web.whatsapp.com/'

    def __init__(self, user=None, driver_path='', timeout=600):
        super().__init__(user, driver_path, timeout)
        self.get(
            WebWSP.START_URL,
            WebWSP.PROFILE_PHOTO_NAME
        )
        # self.driver.minimize_window()

    def click_send(self):
        if self.get_wait(WebWSP.SEND_BUTTON_NAME, WebWSP.CONTENT_TIMEOUT):
            self.driver.find_elements_by_class_name(
                WebWSP.SEND_BUTTON_NAME
            )[0].click()

    def invalid_num(self):
        time.sleep(2)
        inv = self.driver.find_elements_by_class_name(
            WebWSP.INVALID_NUM_NAME
        )
        if inv:
            return inv[0].get_attribute('innerText') == WebWSP.INVALID_NUM_MESG
        return False

    def pressEnter(self, pages, param_getter, **kwargs):
        largo = len(pages)
        count = 0
        for page in pages:
            count +=1
            self.open_tab()
            if self.get(page, WebWSP.PROFILE_PHOTO_NAME):
                if self.invalid_num():
                    phone, msg = param_getter(page)
                    print(f'{count}/{largo} {WebWSP.INVALID_NUM_MESG}: {phone} with message {msg}')
                    continue
                self.click_send()
                self.close_tab()
                self.dismiss_alert()
            else:
                print(f'Could not connect to {page}')
            print(f'{count}/{largo}')


if __name__ == '__main__':
    import os
    data1 = []
    data2 = [
        'https://web.whatsapp.com/send?phone=56944361035&text=abc{}&source&data&app_absent'.format(i)
        for i in range(1000)
    ]
    data = data1+data2
    wsp = WebWSP(driver_path=os.path.join(os.getcwd(), 'chromedriver'))
    wsp.pressEnter(pages=data)
    wsp.quit_driver()
