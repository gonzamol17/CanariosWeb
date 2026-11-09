from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePageLocators:
    tryItYourSelfOption = (By.XPATH, "//button[normalize-space()='Try It Yourself']")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def selectTryItYourSelfOption(self):
        self.driver.find_element(*BasePageLocators.tryItYourSelfOption).click()

