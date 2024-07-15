from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:
  """
  Clase que contiene los elementos del checkout step two
  """
  def __init__(self, driver: webdriver.Remote):
      self.driver = driver
      
  @property
  def __titlePage(self):
    return self.driver.find_element(By.CLASS_NAME, 'title')
  
  @property
  def __button_cancel(self):
    return self.driver.find_element(By.ID, 'cancel')
  
  @property
  def __button_finish(self):
    return self.driver.find_element(By.ID, 'finish')
  
  
  def get_title_page(self):
    """
    Método que se encarga de obtener el título de la página
    Return: título de la página
    """
    return self.__titlePage.text
  
  
  def handle_click_on_cancel(self):
    """
    Método que se encarga de hacer click sobre el botón cancel
    """
    self.__button_cancel.click()
    
    
  def handle_click_on_finish(self):
    """
    Método que se encarga de hacer click sobre el botón finish
    """
    self.__button_finish.click()