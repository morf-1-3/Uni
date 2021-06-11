from selenium.webdriver.remote.webdriver import WebDriver

from pages.job_edit_page import JobEdit
from utils import wait_for_element


class JobDetails:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_confirmation_id(self):
        wait_for_element(self.driver, '.box-item-body', 10)

        box_items = self.driver.find_elements_by_css_selector('.w-20')
        conf = box_items[0].text.split("\n")

        return conf[1]

    def get_po(self):
        wait_for_element(self.driver, '.box-item-body', 10)

        box_items = self.driver.find_elements_by_css_selector('.w-20')
        conf = box_items[1].text.split("\n")

        return conf[1]

    def open_edit_job(self, link_index):
        wait_for_element(self.driver, '.nav-link', 10)

        nav_links = self.driver.find_elements_by_css_selector('.nav-link')
        nav_links[link_index].click()

        return JobEdit(self.driver)

