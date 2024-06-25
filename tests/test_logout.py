from selenium import webdriver
from utils.consts import URL_PATH, USER_CREDENTIALS
from utils.login import login
from pages.logout_page import LogoutPage

class TestLogout:
  # Prueba para realizar el logout
  def test_logout(self, driver: webdriver.Remote):
    isLoginSuccess = login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    if (isLoginSuccess):
      driver.get(f'{URL_PATH}/inventory.html')
      logout_page = LogoutPage(driver)
      logout_page.handle_click_on_burger_btn()
      logout_page.handle_click_on_logout_sidebar_link()
      current_url = driver.current_url
      # En la siguiente línea se utiliza la variable current_url[:-1] 
      # para poder eliminar el / al final de la url y pueda ser validado con el comparador
      assert current_url[:-1] == URL_PATH
      print('Se ha realizado el logout correctamente...!!')