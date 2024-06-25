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
  def __shopping_cart_badge(self):
    return self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link .shopping_cart_badge')
  
  
  def __a_link_item(self, element):
    return element.find_element(By.CSS_SELECTOR, '.inventory_item_label > a')
  
  
  def __img_link_item(self, element):
    return element.find_element(By.CSS_SELECTOR, '.inventory_item_img > a')

  
  def __button_add_to_cart(self, element):
    return element.find_element(By.CSS_SELECTOR, '.btn.btn_primary.btn_inventory')
  
  
  def __button_remove_from_cart(self, element):
    return element.find_element(By.CSS_SELECTOR, '.btn.btn_secondary.btn_inventory')
  
  
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
  
  
  def handle_click_on_product(self, mode: str, index: int):
    """
    Método que se encarga de hacer click sobre el producto
    Args:
    mode: usado para condicionar la forma de selección
    index: hace referencia al item a seleccionar
    """
    products = self.__inventory_items
    product_selected = products[index]
    
    if (mode == MODE_CLICK_PRODUCT["title"]):
      self.__a_link_item(product_selected).click()
    else:
      self.__img_link_item(product_selected).click()
      
      
  def handle_click_add_to_cart(self, index: int):
    """
    Método que se encarga de agregar un producto al carrito
    Args:
    index: usado para seleccionar el elemento por su indice
    """
    products = self.__inventory_items
    product_selected = products[index]
    
    self.__button_add_to_cart(product_selected).click()
    
    
  def get_quantity_added_to_cart(self):
    """
    Método que se encarga de devolver la cantidad de productos existentes en el carrito
    Return: cantidad de productos
    """
    element = self.__shopping_cart_badge
    
    if (element):
      return int(element.text)
    
    
  def handle_click_remove_from_cart(self, index: int):
    """
    Método que se encarga de remover un producto del carrito
    Args:
    index: usado para seleccionar el elemento por su indice
    """
    products = self.__inventory_items
    product_selected = products[index]
    
    self.__button_remove_from_cart(product_selected).click()