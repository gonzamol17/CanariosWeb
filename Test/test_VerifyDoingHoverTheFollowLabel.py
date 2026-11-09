import json
import time

from POM.ConceptsPage import ConceptsPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ButtonPage import ButtonPage

class TestVerifyDoingHoverTheFollowLabel(BaseClass):

      def testVerifyDoingHoverTheFollowLabel(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          cp.selectTheButtonElement()
          bp = ButtonPage(driver)
          bp.selectTryItYourSelfOption()
          bp.hoverSecondFollowButton()
          assert bp.printLabelOnceYouDoHover() == "Follow"
          time.sleep(2)