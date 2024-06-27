from selenium import webdriver
from selenium.webdriver.common.by import By

class CartPage:
  """
  Clase que contiene los elementos de la página del carrito
  """
  def __init__(self, driver: webdriver.Remote):
      self.driver = driver
      
  @property
  def __continue_shopping_btn(self):
    return self.driver.find_element(By.ID, 'continue-shopping')
  
  @property
  def __checkout_btn(self):
    return self.driver.find_element(By.ID, 'checkout')
  
  
  def handle_click_on_continue_shopping(self):
    """
    Método que se encarga de hacer click sobre el botón continue shopping
    """
    self.__continue_shopping_btn.click()
    
    
  def handle_click_on_checkout(self):
    """
    Método que se encarga de hacer click sobre el botón checkout
    """
    self.__checkout_btn.click()