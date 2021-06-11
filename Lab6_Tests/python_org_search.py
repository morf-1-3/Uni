from selenium import webdriver

from pages.login_page import LoginPage

URL = 'http://localhost:3443/login'

VALID_JOB_ID = "100003698"
VALID_JOB_NAME = "Flagging #" + VALID_JOB_ID

INVALID_JOB_ID = "000000000"
INVALID_JOB_NAME = "Flagging #" + INVALID_JOB_ID

PO = "23"


def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)


def run():
    driver = get_web_driver()
    driver.get(URL)

    # login tests
    login_page = LoginPage(driver)

    login_page.input_email("lina.savevna@gmail.com")
    login_page.input_password("qwerty123")
    login_page.submit_expecting_failure()

    errors = login_page.get_errors()
    assert len(errors) > 0

    login_page.input_password("qwqweer12ty")

    # job tests
    job_page = login_page.submit_expecting_success()
    jobs_names = job_page.get_jobs_names()

    assert VALID_JOB_NAME in jobs_names
    assert INVALID_JOB_NAME not in jobs_names

    # job details tests
    job_details_page = job_page.open_job(0)
    conf_id = job_details_page.get_confirmation_id()

    assert conf_id == VALID_JOB_ID

    # job edit tests
    job_edit_page = job_details_page.open_edit_job(4)
    job_edit_page.input_po(int(PO))

    # job details tests
    job_details_page = job_edit_page.submit_expecting_success()
    po = job_details_page.get_po()

    assert po == PO

    print('All tests were passed successfully')
    input()


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print('An exception was thrown during running tests: ' + str(e))
