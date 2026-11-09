import json
import time

from POM.ConceptsPage import ConceptsPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ButtonPage import ButtonPage

class TestVerifyWhenFollowToSomeOneTheButtonNameChange(BaseClass):

      def testVerifyWhenFollowToSomeOneTheButtonNameChange(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          cp.selectTheButtonElement()
          bp = ButtonPage(driver)
          bp.selectTryItYourSelfOption()
          originName = bp.getSecondButtonText()
          assert originName == "Follow"
          bp.clickSecondFollowButton()
          bp.waitUntilFollowing()
          newName = bp.getSecondButtonText()
          assert newName == "Following"
          time.sleep(2)