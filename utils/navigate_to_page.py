from utils.consts import URL_PATH, PAGES
from pages.login_page import LoginPage
from selenium import webdriver

def navigate_to_page(driver:webdriver.Remote, page: dict[str, str]):
    """
    Función que navega a la URL de la página especificada y devuelve una instancia de la clase.
    Args:
    driver: instancia de WebDriver
    page: argumento utilizado para identificar la instancia de la clase a consultar
    Return: instancia de la clase consultada
    """
    driver.get(URL_PATH)
    
    if (page == PAGES["login_page"]):
      return LoginPage(driver)