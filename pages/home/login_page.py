from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    username_field = "//input[@placeholder='Email Id']"
    password_field = "//input[@placeholder='Password']"
    login_button = "//div[@class='button'][normalize-space()='Login']"

    def enterEmail(self, username):
        self.sendKeys(username, self.username_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self.password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self.login_button, locatorType="xpath")

    def login(self, username, password):
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()
