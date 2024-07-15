from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckoutCompletePage:
  """
  Clase que contiene los elementos de checkout complete
  """
  def __init__(self, driver: webdriver.Remote):
      self.driver = driver
      
  @property
  def __titlePage(self):
    return self.driver.find_element(By.CLASS_NAME, 'title')
  
  @property
  def __button_back_home(self):
    return self.driver.find_element(By.ID, 'back-to-products')
  
  
  def get_title_page(self):
    """
    Método que se encarga de obtener el título de la página
    Return: título de la página
    """
    return self.__titlePage.text
  
  
  def handle_click_on_back_home(self):
    """
    Método que se encarga de hacer click sobre el botón back home
    """
    self.__button_back_home.click()