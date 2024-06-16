from utils.login import login
from utils.consts import USER_CREDENTIALS
from selenium import webdriver

class TestLogin:
    # Prueba para el login con usuario estándar
    def test_login(self, driver:webdriver.Remote):
        login(
            driver,
            USER_CREDENTIALS["username"]["standard_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        
    # Prueba para el login con usuario bloqueado
    def test_locked_user(self, driver:webdriver.Remote):
        login(
            driver,
            USER_CREDENTIALS["username"]["locked_out_user"], 
            USER_CREDENTIALS["password"]["secret_sauce"]
        )
        
    # Prueba para el login con credenciales incorrectas
    def test_credentials_error(self, driver:webdriver.Remote):
        login(
            driver,
            USER_CREDENTIALS["username"]["malicious_user"], 
            USER_CREDENTIALS["password"]["failed_password"]
        )