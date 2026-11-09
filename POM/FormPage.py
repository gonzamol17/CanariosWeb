from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.BasePage import BasePage


class FormPageLocators:
    #tryItYourSelfOption = (By.XPATH, "//button[normalize-space()='Try It Yourself']")
    fullNameField = (By.CSS_SELECTOR, "input[data-testid='input-fullname']")
    emailField = (By.CSS_SELECTOR, "input[data-testid='input-email']")
    phoneNumberField = (By.CSS_SELECTOR, "input[data-testid='input-phone']")
    ticketQty = (By.CSS_SELECTOR, "input[data-testid='input-tickets']")
    dropdownEvent = (By.CSS_SELECTOR, "div[role='combobox']")
    optionsFromEventDropdown = (By.CSS_SELECTOR, "li[role='option']")
    btnSubmit = (By.CSS_SELECTOR, "button[data-testid='btn-submit']")
    redWarningEmail = (By.ID, "«rd»-helper-text")
    redWarningPhoneNumber = (By.ID, "«re»-helper-text")




class FormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def fill_basic_info(self, name, email, phone):
        self.driver.find_element(*FormPageLocators.fullNameField).send_keys(name)
        self.driver.find_element(*FormPageLocators.emailField).send_keys(email)
        self.driver.find_element(*FormPageLocators.phoneNumberField).send_keys(phone)

    def select_event(self, event):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FormPageLocators.dropdownEvent)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", dropdown
        )
        dropdown.click()

        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(FormPageLocators.optionsFromEventDropdown)
        )

        for item in items:
            if item.text == event:
                item.click()
                break


    def set_ticket_quantity(self, qty):
        el = self.driver.find_element(*FormPageLocators.ticketQty)
        el.click()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(str(qty))


    def fillForm(self, name, email, phone, event, qty):
        self.fill_basic_info(name, email, phone)
        self.select_event(event)
        self.set_ticket_quantity(qty)


    def verifyIfSubmitBtnIsEnabled(self):
        #btn = WebDriverWait(self.driver, 10).until(
        #    EC.element_to_be_clickable(FormPageLocators.btnSubmit)
        #)

        #self.driver.execute_script(
        #    "arguments[0].scrollIntoView({block: 'center'});", btn
        #)
        return self.driver.find_element(*FormPageLocators.btnSubmit).is_enabled()

    def get_email_warning(self):
        return self.driver.find_element(*FormPageLocators.redWarningEmail).text

    def get_phone_warning(self):
        return self.driver.find_element(*FormPageLocators.redWarningPhoneNumber).text

    def is_register_button_enabled(self):
        return self.driver.find_element(*FormPageLocators.btnSubmit).is_enabled()