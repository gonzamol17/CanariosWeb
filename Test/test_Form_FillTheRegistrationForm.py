import json
import time

from Data import UserDataFactory
from POM.ConceptsPage import ConceptsPage
from POM.FormPage import FormPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from Data.UserDataFactory import UserDataFactory


class TestFormFillTheRegistrationForm(BaseClass):

      def testFormFillTheRegistrationForm(self):
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
          data = UserDataFactory.create_user()
          #name = fake.name()
          #email = fake.email()
          #phoneNumber = fake.numerify(text='6########')
          #fp.fillForm(name, email, phoneNumber, event, ticketNumber)
          event = "Design & UX Meetup"
          ticketNumber = 3
          fp.fillForm(data["name"], data["email"],data["phone"],event,ticketNumber)
          assert fp.verifyIfSubmitBtnIsEnabled() is True
          time.sleep(4)