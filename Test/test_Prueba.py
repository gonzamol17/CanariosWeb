import json
import time

import pytest

from Data import UserDataFactory
from POM.ConceptsPage import ConceptsPage
from POM.FormPage import FormPage
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from Data.UserDataFactory import UserDataFactory

@pytest.mark.report
class TestPrueba(BaseClass):

      def testPrueba(self):
          log = self.get_Logger()
          log.info("Está entrando a la página")
          log.debug("Es otro mensaje de debug")
          log.error("ES otro mensaje de Error")
          driver = self.driver

          time.sleep(4)