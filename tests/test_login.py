from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.consts import USER_CREDENTIALS, URL_PATH
from selenium import webdriver

class TestLogin:
    # Prueba para el login con usuario estándar
    def test_login(self, driver:webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        login_page.to_do_login(
            USER_CREDENTIALS["username"]["standard_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        print('Login realizado correctamente...!!')
        
        # Navegar a la página de inventario y obtener el título
        driver.get(f'{URL_PATH}/inventory.html')
        inventory_page = InventoryPage(driver)
        expect_message = inventory_page.get_title_page()
        print(f'Título de la página de inventario de productos => {expect_message}')
        
    # Prueba para el login con usuario bloqueado
    def test_locked_user(self, driver:webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        login_page.to_do_login(
            USER_CREDENTIALS["username"]["locked_out_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        error_message = login_page.get_error_message()
        expect_message = "Epic sadface: Sorry, this user has been locked out."
        assert expect_message in error_message
        print(f'Mensaje de error es el esperado => {expect_message}')
        
    # Prueba para el login con credenciales incorrectas
    def test_credentials_error(self, driver:webdriver.Remote):
        driver.get(URL_PATH)
        login_page = LoginPage(driver)
        login_page.to_do_login(
            USER_CREDENTIALS["username"]["malicious_user"], 
            USER_CREDENTIALS["password"]["failed_password"]
        )
        error_message = login_page.get_error_message()
        expect_message = "Epic sadface: Username and password do not match any user in this service"
        assert expect_message in error_message
        print(f'Mensaje de error es el esperado => {expect_message}')