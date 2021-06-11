from selenium.webdriver.remote.webdriver import WebDriver

from pages.job_page import JobPage
from utils import wait_for_element, clear_input


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_email(self, email):
        input_email = self.driver.find_element_by_name("email")
        input_email.send_keys(email)

    def input_password(self, password):
        input_password = self.driver.find_element_by_name("password")
        clear_input(input_password)
        input_password.send_keys(password)

    def submit_expecting_success(self):
        self._submit_btn()

        wait_for_element(self.driver, '#job', timeout=30)

        submit_btn = self.driver.find_element_by_css_selector('#job')
        submit_btn.click()

        return JobPage(self.driver)

    def submit_expecting_failure(self):
        self._submit_btn()

    def get_errors(self):
        wait_for_element(self.driver, 'button[type=button]', timeout=2)
        errors_elements = self.driver.find_elements_by_css_selector('button[type=button]')

        return [x.text for x in errors_elements]

    def _submit_btn(self):
        submit_btn = self.driver.find_element_by_css_selector('button[type=submit]')
        submit_btn.submit()
