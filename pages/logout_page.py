from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
  """
  Clase que contiene los elementos de la página de logout
  """
  
  def __init__(self, driver: webdriver.Remote):
    self.driver = driver
    
  @property
  def __burger_menu_btn(self):
    return self.driver.find_element(By.ID, 'react-burger-menu-btn')
  
  @property
  def __logout_sidebar_link(self):
    return (By.ID, 'logout_sidebar_link')
  
  
  def handle_click_on_burger_btn(self):
    """
    Método que se encarga de hacer click sobre el botón hamburguesa
    """
    self.__burger_menu_btn.click()
    
    
  def handle_click_on_logout_sidebar_link(self):
    """
    Método que se encarga de hacer click sobre el botón logout del sidebar
    """
    element = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located(self.__logout_sidebar_link)
    )
    element.click()