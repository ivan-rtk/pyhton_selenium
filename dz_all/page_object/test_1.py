from testpage import OperationsHelper
import logging
import yaml


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# def test_step1(browser):
#     logging.info("Test Starting1")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login("test")
#     testpage.enter_pass("test")
#     testpage.click_login_button()
#     assert testpage.get_error_text() == "401"

# def test_step2(browser):
#     logging.info("Test Starting2")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata.get("login"))
#     testpage.enter_pass(testdata.get("password"))
#     testpage.click_login_button()
#     # print("*"* 60)
#     # print(testpage.get_text())
#     # print("*" * 60)


# """ проверка механики работы формы Contact Us на главной странице личного кабинета:
# открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert."""
def test_step3(browser):
    logging.info("Test Starting3")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("password"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata.get("name"))
    testpage.enter_email(testdata.get("email"))
    testpage.enter_content(testdata.get("content"))
    testpage.click_contact_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test FAILED"