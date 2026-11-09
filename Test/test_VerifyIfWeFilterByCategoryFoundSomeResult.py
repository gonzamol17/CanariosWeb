import json
import time

from POM.ConceptsPage import ConceptsPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage

class TestVerifyFilterByCategoryFoundSomeResult(BaseClass):

      def test_VerifyFilterByCategoryFoundSomeResult(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          driver = self.driver
          hp = HomePage(driver)
          hp.selectStartLearningBtn()
          cp = ConceptsPage(driver)
          expected_counts = {
              "Interaction": 2,
              "Element": 3,
              "Input": 7,
              "Event": 3,
              "Navigation": 3,
              "Overlay": 1,
              "DOM Interaction": 1,
          }
          category_name = "Overlay"
          cp.selectOptionFromDropdownByCategory(category_name)
          labels = cp.showMeAllYellowLabels()
          assert len(labels) == expected_counts[category_name], \
              f"Se esperaban {expected_counts[category_name]} labels para '{category_name}' pero se encontraron {len(labels)}"
          for label in labels:
              assert category_name.lower() in label.lower(), \
                  f"El label '{label}' no coincide con la categoría '{category_name}'"
          time.sleep(1)