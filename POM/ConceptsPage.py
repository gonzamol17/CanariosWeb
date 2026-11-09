from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage


class ConceptsPageLocators:
    searchBar = (By.CSS_SELECTOR, "input[placeholder='Search by title, category, or alias']")
    buttonsTitle = (By.CSS_SELECTOR, "p.MuiTypography-root.MuiTypography-body1.css-1vgbump")
    openDropdown = (By.CSS_SELECTOR, "div[role='combobox']")
    dropdownListFilterByCategory = (By.CSS_SELECTOR, "ul.MuiList-root.MuiList-padding.MuiMenu-list.css-ubifyk>li")
    yellowLabelsList = (By.CSS_SELECTOR, "div.MuiChip-root.MuiChip-filledDefault.css-je7t37")
    buttonOption = (By.XPATH, "//p[normalize-space()='Button']")
    formOption = (By.XPATH, "//p[normalize-space()='Form']")






class ConceptsPage(BasePage):

    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    def searchAParticularComponent(self, element):
        self.driver.find_element(*ConceptsPageLocators.searchBar).send_keys(element)

    def showMeAllButtonResults(self):
        itemsWithButton = self.driver.find_elements(*ConceptsPageLocators.buttonsTitle)
        button_results = []
        for item in itemsWithButton:
            text = item.text.lower()
            if "button" in text:
                button_results.append(item)
        return button_results

    def selectOptionFromDropdownByCategory(self, value):
        self.driver.find_element(*ConceptsPageLocators.openDropdown).click()
        listDropdownFilterByCategory = self.driver.find_elements(*ConceptsPageLocators.dropdownListFilterByCategory)
        for item in listDropdownFilterByCategory:
            text = item.text.strip().lower()
            if text == value.lower():
                item.click()
                break

    def showMeAllYellowLabels(self):
        labels = self.driver.find_elements(*ConceptsPageLocators.yellowLabelsList)
        listOfLabels = []
        for label in labels:
            listOfLabels.append(label.text)
        return listOfLabels

    def selectTheButtonElement(self):
        self.driver.find_element(*ConceptsPageLocators.buttonOption).click()

    def selectTheFormElement(self):
        self.driver.find_element(*ConceptsPageLocators.formOption).click()