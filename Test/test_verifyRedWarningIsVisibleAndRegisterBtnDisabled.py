import json
import time

from Data import UserDataFactory
from POM.ConceptsPage import ConceptsPage
from POM.FormPage import FormPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from Data.UserDataFactory import UserDataFactory


class TestVerifyRedWarningIsVisibleAndRegisterBtnDisabled(BaseClass):

      def testVerifyRedWarningIsVisibleAndRegisterBtnDisabled(self):
          log = self.get_Logger()
          #fake = Faker()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          cp.selectTheFormElement()
          fp = FormPage(driver)
          fp.selectTryItYourSelfOption()
          log.info("Estoy en la parte de Form")
          fp.fillForm("Pepe", "AAAA", "BB", "Design & UX Meetup","1")
          assert fp.get_email_warning() == "Enter a valid email address"
          assert fp.get_phone_warning() == "Enter a valid phone (7-15 digits)"
          assert not fp.is_register_button_enabled()
          time.sleep(4)