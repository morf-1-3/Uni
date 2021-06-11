from selenium.webdriver.remote.webdriver import WebDriver

from pages.job_details_page import JobDetails
from utils import wait_for_element


class JobPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_jobs_names(self):
        wait_for_element(self.driver, 'span.ce-ml-10', 20)
        jobs_names_elements = self.driver.find_elements_by_css_selector('span.ce-ml-10')

        return [x.text for x in jobs_names_elements]

    def open_job(self, job_index):
        wait_for_element(self.driver, '.box-item-body.hover-item-body.cursor-pointer.radius', 20)
        jobs_links_elements = self.driver.find_elements_by_css_selector('.box-item-body.hover-item-body.cursor-pointer.radius')
        jobs_links_elements[job_index].click()

        return JobDetails(self.driver)
