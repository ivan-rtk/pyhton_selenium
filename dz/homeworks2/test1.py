import time

import yaml
# from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata["address"])

def test_step1(site, selector_login, selector_passwd, selector_button,
               selector_error, create_new_post, add_title_field,
               add_description_field, add_content_field,
               selector_save_post, check_title, title_name):
    input1 = site.find_element("xpath", selector_login)
    input1.clear()
    input1.send_keys("login")

    input2 = site.find_element("xpath", selector_passwd)
    input2.clear()
    input2.send_keys("password")

    btn = site.find_element("css", selector_button)
    btn.click()

    time.sleep(testdata["slep_time"])

    btn = site.find_element("xpath", create_new_post)
    btn.click()

    input3 = site.find_element("xpath", add_title_field)
    input3.clear()
    input3.send_keys("title")

    input4 = site.find_element("xpath", add_description_field)
    input4.clear()
    input4.send_keys("description")

    input5 = site.find_element("xpath", add_content_field)
    input5.clear()
    input5.send_keys("content")

    btn = site.find_element("xpath", selector_save_post)
    btn.click()

    time.sleep(testdata["sleep_time"])

    code_label = site.find_element("xpath", add_title_field).text
    assert code_label == title, "test 'add post' Failed"

    site.driver.close()




if __name__ == "__main__":
    pytest.main(["-vv"])