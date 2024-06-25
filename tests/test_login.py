from pages.login_page import LoginPage
from utils.login import login
from utils.consts import ERROR_MESSAGE, LOCKED_OUT_USER, MALICIOUS_USER, STANDARD_USER, URL_PATH
from selenium import webdriver

class TestLogin:
    # Prueba para el login con usuario estándar
    def test_login(self, driver: webdriver.Remote):
        isLoginSuccess = login(driver, STANDARD_USER)
        
        if (isLoginSuccess):
            print('Login realizado correctamente...!!')
            
        
    # Prueba para el login con usuario bloqueado
    def test_locked_user(self, driver: webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        
        isLoginSuccess = login(driver, LOCKED_OUT_USER)
        
        if not (isLoginSuccess):
            error_message = login_page.get_error_message()
            assert ERROR_MESSAGE["expect_message_user_locked"] in error_message
            print(f'Mensaje de error es el esperado => {error_message}')
            
        
    # Prueba para el login con credenciales incorrectas
    def test_credentials_error(self, driver: webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        
        isLoginSuccess = login(driver, MALICIOUS_USER)
        
        if not (isLoginSuccess):
            error_message = login_page.get_error_message()
            assert ERROR_MESSAGE["expect_message_user_do_not_match"] in error_message
            print(f'Mensaje de error es el esperado => {error_message}')