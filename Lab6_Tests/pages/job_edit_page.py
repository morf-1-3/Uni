from selenium.webdriver.remote.webdriver import WebDriver

import pages.job_details_page
from utils import wait_for_element, clear_input


class JobEdit:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_po(self, po):
        wait_for_element(self.driver, 'po', 10)
        input_po = self.driver.find_element_by_name("po")

        clear_input(input_po)
        input_po.send_keys(po)

    def submit_expecting_success(self):
        self._submit_btn()
        return pages.job_details_page.JobDetails(self.driver)

    def _submit_btn(self):
        submit_btn = self.driver.find_element_by_css_selector('button[type=submit]')
        submit_btn.click()
