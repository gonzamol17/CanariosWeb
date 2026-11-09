from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage


class ButtonPageLocators:
    tryItYourSelfOption = (By.XPATH, "//button[normalize-space()='Try It Yourself']")
    secondFollowButton = (By.XPATH, "(//button[contains(text(),'Follow')])[2]")
    secondFollowingButton = (By.XPATH, "//button[normalize-space()='Following']")
    allFollowEnabledButton = (By.XPATH, "//button[@type='button' and normalize-space()='Follow' and not(@disabled)]")
    allFollowDisabledButton = (By.XPATH, "//button[@type='button' and normalize-space()='Follow' and (@disabled)]")
    removeSuggestionsItems = (By.CSS_SELECTOR, "svg.MuiSvgIcon-root.close.css-vh810p")
    noSuggestionsMessage = (By.XPATH, "//*[contains(text(),'No suggestions at the moment')]")
    labelOnceYouDoHover = (By.XPATH, "//div[contains(@class, 'MuiTooltip-tooltip') and text()='Follow']")


class ButtonPage(BasePage):

    def __init__(self, driver):
        #self.driver = driver
        #self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    #def selectTryItYourSelfOption(self):
    #    self.driver.find_element(*ButtonPageLocators.tryItYourSelfOption).click()

    def getSecondButtonText(self):
        return self.wait.until(
            EC.visibility_of_element_located(ButtonPageLocators.secondFollowButton)
        ).text

    def clickSecondFollowButton(self):
        self.wait.until(
            EC.element_to_be_clickable(ButtonPageLocators.secondFollowButton)
        ).click()

    def waitUntilFollowing(self):
        self.wait.until(
            EC.text_to_be_present_in_element(ButtonPageLocators.secondFollowButton, "Following")
        )

    def showMeAllFollowEnabledButton(self):
        return len(self.driver.find_elements(*ButtonPageLocators.allFollowEnabledButton))

    def showMeAllFollowDisabledButton(self):
        return len(self.driver.find_elements(*ButtonPageLocators.allFollowDisabledButton))

    def removeAllSuggestionsItems(self):
        itemsSuggestions = self.driver.find_elements(*ButtonPageLocators.removeSuggestionsItems)
        for item in itemsSuggestions:
            item.click()
        # while True:
        #     items = self.driver.find_elements(*ButtonPageLocators.removeSuggestionsItems)
        #     if not items:
        #         break
        #     items[0].click()

    def getNoSuggestionsMessage(self):
        return self.driver.find_element(*ButtonPageLocators.noSuggestionsMessage).text

    # def selectAllFollowEnabledButton(self):
    #     followButtons = self.driver.find_elements(*ButtonPageLocators.allFollowEnabledButton)
    #     for button in followButtons:
    #         button.click()


    #def showMeAllFollowingButton(self):
    #    return len(self.driver.find_elements(*ButtonPageLocators.secondFollowingButton))


    def selectAllFollowEnabledButton(self):
        followButtons = self.driver.find_elements(*ButtonPageLocators.allFollowEnabledButton)
        for button in followButtons:
            button.click()
        # Espera explícita para que el texto cambie a "Following"
            self.wait.until(
            EC.text_to_be_present_in_element(ButtonPageLocators.secondFollowButton, "Following")
        )

    # Esperar hasta que todos los botones "Follow" hayan cambiado a "Following"
        self.wait.until(lambda driver: all(
        button.text == "Following" for button in self.driver.find_elements(*ButtonPageLocators.allFollowEnabledButton)
    ))


    def showMeAllFollowingButton(self):
    # Espera hasta que todos los botones hayan cambiado a "Following"
        self.wait.until(
        EC.presence_of_all_elements_located(ButtonPageLocators.secondFollowingButton)
    )
    # Ahora devuelve la cantidad de botones "Following"
        followingButtons = self.driver.find_elements(*ButtonPageLocators.secondFollowingButton)
        return len(followingButtons)

    def hoverSecondFollowButton(self):
        element = self.wait.until(
            EC.visibility_of_element_located(ButtonPageLocators.secondFollowButton)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def printLabelOnceYouDoHover(self):
       return self.driver.find_element(*ButtonPageLocators.labelOnceYouDoHover).text