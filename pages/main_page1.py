from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page1 import LoginPage #

class MainPage(BasePage): 
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #далее оставил для понимания процесса предыдущее исполнение до вынесения ссылки в селекторы
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url) #