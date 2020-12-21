"""
Sends messages from url.
"""
import libs.explorer as xp
import time


class WebWSP(xp.ExplorerHandler):

    START_URL = 'https://web.whatsapp.com/'
    PROFILE_PHOTO_NAME = '_1l12d'
    SEND_BUTTON_NAME = '_2Ujuu'
    INVALID_NUM_NAME = '_2fuxX'
    BODY_CHAT_NAME = '_1awRl copyable-text selectable-text'

    def __init__(self, user=None, driver_path='', timeout=600):
        super().__init__(user, driver_path, timeout)
        self.get(
            WebWSP.START_URL,
            WebWSP.PROFILE_PHOTO_NAME
        )
        # self.driver.minimize_window()
    
    def click_send(self):
        btn = self.driver.find_elements_by_class_name(
            WebWSP.SEND_BUTTON_NAME
        )
        if btn:
            btn = btn[0]
            btn.click()
        # self.click_out()
        
    
    def invalid_num(self):
        inv = self.driver.find_elements_by_class_name(
            WebWSP.INVALID_NUM_NAME
        )
        if inv:
            return True
        return False
    
    def pressEnter(self, pages, **kwargs):
        largo = len(pages)
        count = 0
        for page in pages:
            print(f'{count}/{largo}')
            count +=1
            self.open_tab()
            self.get(page, WebWSP.PROFILE_PHOTO_NAME)
            if self.invalid_num():
                print(f'Invalid number: {page}')
                continue
            self.click_send()
            self.close_tab()
            self.dismiss_alert()
                

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
