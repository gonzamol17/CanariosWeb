import json
import time

from POM.ConceptsPage import ConceptsPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.ButtonPage import ButtonPage

class TestSelectAllTheFollowButtons(BaseClass):

      def testSelectAllTheFollowButtons(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          cp.selectTheButtonElement()
          bp = ButtonPage(driver)
          bp.selectTryItYourSelfOption()
          driver.execute_script("window.scrollTo(0, 400)")
          totalFollowBtns= bp.showMeAllFollowEnabledButton()
          bp.selectAllFollowEnabledButton()
          totalFollowingBtns= bp.showMeAllFollowingButton()
          assert totalFollowBtns==totalFollowingBtns
          time.sleep(2)