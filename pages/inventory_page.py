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
  
  @property
  def __inventory_list(self):
    return self.driver.find_element(By.CLASS_NAME, 'inventory_list')
  
  @property
  def __inventory_items(self):
    return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
  
  def get_title_page(self):
    return self.__titlePage.text
  
  def exist_some_inventory_item(self):
    return len(self.__inventory_items)