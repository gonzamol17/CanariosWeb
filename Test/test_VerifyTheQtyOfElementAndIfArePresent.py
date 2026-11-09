import json
import time

from POM.ConceptsPage import ConceptsPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage

class TestVerifyTheQtyElementsAndIfArePresent(BaseClass):

      def test_VerifyTheQtyOfElementAndIfArePresent(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          cp.searchAParticularComponent("Button")
          elementsWithButton = cp.showMeAllButtonResults()
          assert len(elementsWithButton) == 2
          for element in elementsWithButton:
              assert "Button" in element.text
          time.sleep(2)