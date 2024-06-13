from utils.consts import USER_CREDENTIALS, PAGES
from utils.navigate_to_page import navigate_to_page
from selenium import webdriver

class TestLogin:
    # Prueba para el login con usuario estándar
    def test_login(self, driver:webdriver.Remote):
        login_page = navigate_to_page(driver, PAGES["login_page"])
        login_page.login_completo(
            USER_CREDENTIALS["username"]["standard_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        print('Login realizado correctamente...!!')
        
    # Prueba para el login con usuario bloqueado
    def test_locked_user(self, driver:webdriver.Remote):
        login_page = navigate_to_page(driver, PAGES["login_page"])
        login_page.login_completo(
            USER_CREDENTIALS["username"]["locked_out_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        error_message = login_page.obtener_mensaje_error()
        expect_message = "Epic sadface: Sorry, this user has been locked out."
        assert expect_message in error_message
        print(f'Mensaje de error es el esperado => {expect_message}')
        
    # Prueba para el login con credenciales incorrectas
    def test_credentials_error(self, driver:webdriver.Remote):
        login_page = navigate_to_page(driver, PAGES["login_page"])
        login_page.login_completo(
            USER_CREDENTIALS["username"]["malicious_user"], 
            USER_CREDENTIALS["password"]["failed_password"]
        )
        error_message = login_page.obtener_mensaje_error()
        expect_message = "Epic sadface: Username and password do not match any user in this service"
        assert expect_message in error_message
        print(f'Mensaje de error es el esperado => {expect_message}')