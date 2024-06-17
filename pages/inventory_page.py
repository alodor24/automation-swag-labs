from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.consts import MODE_CLICK_PRODUCT

class InventoryPage:
  """
  Clase que contiene los elementos de la página de inventario
  """
  
  def __init__(self, driver: webdriver.Remote):
    self.driver = driver
        
  @property
  def __titlePage(self):
    return self.driver.find_element(By.CLASS_NAME, "title")
  
  @property
  def __inventory_items(self):
    return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
  
  @property
  def __a_link_item(self):
    return self.driver.find_element(By.CSS_SELECTOR, '.inventory_item:nth-child(2) .inventory_item_label > a')
  
  @property
  def __img_link_item(self):
    return self.driver.find_element(By.CSS_SELECTOR, '.inventory_item .inventory_item_img > a')
  
  def get_title_page(self):
    """
    Método que se encarga de obtener el título de la página
    Return: título de la página
    """
    return self.__titlePage.text
  
  def exist_some_inventory_item(self):
    """
    Método que se encarga de contabilizar los productos encontrados
    Return: cantidad de productos
    """
    return len(self.__inventory_items)
  
  def handle_click_on_product(self, mode: str):
    """
    Método que se encarga de hacer click sobre el producto
    Args:
    mode: usado para condicionar la forma para seleccionar
    """
    if (mode == MODE_CLICK_PRODUCT["title"]):
      self.__a_link_item.click()
    else:
      self.__img_link_item.click()