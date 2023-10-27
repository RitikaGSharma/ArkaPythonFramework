from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseurl = "https://beta.arkaenergy.com/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseurl)
        loginpage = LoginPage(driver)
        loginpage.login("CRM1beta@gmail.com", "CRM1beta@gmail.com")

        dashboardIcon = driver.find_element(By.XPATH,"//div[@class='selection-container el-popover__reference']//p[contains(text(),'Default Dashboard')]")

        if dashboardIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

