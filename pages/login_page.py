from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    """
    Clase que contiene los elementos de la página de login
    """
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    @property
    def __input_username(self):
        return self.driver.find_element(By.ID, "user-name")
    
    @property
    def __input_password(self):
        return self.driver.find_element(By.ID, "password")
    
    @property
    def __button_login(self):
        return self.driver.find_element(By.ID, "login-button")
    
    @property
    def __h3_errorMessage(self):
        return self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']//h3")
    
    def to_do_login(self, username, password):
        """
        Método que se encarga de realizar el login completo
        Args:
        username: nombre de usuario
        password: contraseña
        """
        self.__input_username.send_keys(username)
        self.__input_password.send_keys(password)
        self.__button_login.click()
        
    def get_error_message(self):
        """
        Método que se encarga de obtener el mensaje de error
        Return: mensaje de error
        """
        return self.__h3_errorMessage.text