from selenium import webdriver
from selenium.webdriver.common.by import By

class InventoryPage:
  """
  Clase que contiene los elementos de la página de login
  """
  
  def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
  @property
  def __titlePage(self):
    return self.driver.find_element(By.CLASS_NAME, "title")
  
  def get_title_page(self):
    return self.__titlePage.text