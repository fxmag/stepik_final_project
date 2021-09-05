from pages.base_page import BasePage
#from pages.main_page import MainPage
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()  

    def should_be_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        #instead of writing opening login for each test, move the above line to base_page and import here
        #self.browser.go_to_login_page()
        assert "login" in self.browser.current_url, "should be login page, the url does not contain login"
        #нужно найти метод прочитать адрес строки и тогда проверить, есть ли там слово "login"
        # в should_be_login_url проверяем в assert не равена ли строка self.url через find строке login.  (!= -1)
        #assert "/login" in self.open(), "login is absent in current url"
        #if 'login' in login_url:
        #   return True

        #второй вариант нахождения совпадения в тексте
        #index = login_url.find('login')
        #if index != -1:
        #    return True
        
        
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # в shold_be_login_form и register_form ищем через id login_form или register_form в locators
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "No registration form"