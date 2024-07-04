from selenium import webdriver
from utils.consts import STANDARD_USER, URL_PATH
from utils.login import login
from pages.logout_page import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
  # Prueba para realizar el logout
  def test_logout(self, driver: webdriver.Remote):
    isLoginSuccess = login(driver, STANDARD_USER)
    
    if (isLoginSuccess):
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/inventory.html'))
      logout_page = LogoutPage(driver)
      logout_page.handle_click_on_burger_btn()
      logout_page.handle_click_on_logout_sidebar_link()
      current_url = driver.current_url
      # En la siguiente línea se utiliza la variable current_url[:-1] 
      # para poder eliminar el / al final de la url y pueda ser validado con el comparador
      assert current_url[:-1] == URL_PATH
      print('Se ha realizado el logout correctamente...!!')