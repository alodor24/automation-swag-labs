from pages.login_page import LoginPage
from utils.login import login
from utils.consts import ERROR_MESSAGE, URL_PATH, USER_CREDENTIALS
from selenium import webdriver

class TestLogin:
    # Prueba para el login con usuario estándar
    def test_login(self, driver: webdriver.Remote):
        isLoginSuccess = login(
            driver,
            USER_CREDENTIALS["username"]["standard_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        
        if (isLoginSuccess):
            print('Login realizado correctamente...!!')
            
        
    # Prueba para el login con usuario bloqueado
    def test_locked_user(self, driver: webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        
        isLoginSuccess = login(
            driver,
            USER_CREDENTIALS["username"]["locked_out_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        
        if not (isLoginSuccess):
            error_message = login_page.get_error_message()
            assert ERROR_MESSAGE["expect_message_user_locked"] in error_message
            print(f'Mensaje de error es el esperado => {error_message}')
            
        
    # Prueba para el login con credenciales incorrectas
    def test_credentials_error(self, driver: webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        
        isLoginSuccess = login(
            driver,
            USER_CREDENTIALS["username"]["malicious_user"], 
            USER_CREDENTIALS["password"]["failed_password"]
        )
        
        if not (isLoginSuccess):
            error_message = login_page.get_error_message()
            assert ERROR_MESSAGE["expect_message_user_do_not_match"] in error_message
            print(f'Mensaje de error es el esperado => {error_message}')