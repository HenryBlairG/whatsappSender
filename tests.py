"""
Test file for dependencies
"""
import libs.url_utils as url


def test_no_msg_url():
    assert url.no_msg_url('123') == 'https://web.whatsapp.com/send?phone=123&text=&source&data&app_absent'


def test_send():
    assert url.send_msg_url('123', 'a') == 'https://web.whatsapp.com/send?phone=123&text=abc&source&data&app_absent'
