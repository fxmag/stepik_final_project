from pages.main_page1 import MainPage
#from pages.login_page1 import LoginPage

# закомментированный ниже код переехал в main_page.py чтоб использовать для логина во всех тестах
#def go_to_login_page(browser):
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()



def test_login_link_should_be_present_on_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #ниже тестировалась ссылка с изменённым селектором логина
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()

def test_login_url_should_open_and_accept_inputs(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #
    page.open()
    login_page = page.go_to_login_page() #
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()