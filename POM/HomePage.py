from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from POM.BasePage import BasePage


class HomePageLocators:
    starLearningBtn = (By.XPATH, "//button[normalize-space()='Start Learning']")
    starTakeChallengeBtn = (By.XPATH, "// button[normalize - space() = 'Take Challenge']")





class HomePage(BasePage):

    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    def selectStartLearningBtn(self):
        self.driver.find_element(*HomePageLocators.starLearningBtn).click()

    def selectTakeChallengeBtn(self):
        self.driver.find_element(*HomePageLocators.starTakeChallengeBtn).click()

