import pytest

from Data.Testdata import *
from Pages.LoginPage import Login


@pytest.mark.usefixtures("test_setup")
class Testloginpage():
    def test_fbpage(self):
        driver=self.driver
        lg=Login(driver)
        lg.Login1(Username,Password)
