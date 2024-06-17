from pages.inventory_page import InventoryPage
from utils.login import login
from utils.click_on_product import click_on_product
from utils.consts import USER_CREDENTIALS, URL_PATH, MODE_CLICK_PRODUCT
from selenium import webdriver
class TestInventory:
  # Prueba para comprobar si existen productos
  def test_exist_some_product(self, driver:webdriver.Remote):
    login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    driver.get(f'{URL_PATH}/inventory.html')
    inventory_page = InventoryPage(driver)
    products = inventory_page.exist_some_inventory_item()
    
    if (products > 0):
      print(f'La cantidad de productos visibles es: {products}')
    else:
      raise Exception('No existen productos para interactuar')
    
  # Prueba para seleccionar un producto desde el titulo
  def test_handle_click_title_product(self, driver:webdriver.Remote):
    click_on_product(driver, MODE_CLICK_PRODUCT["title"])
    
  # Prueba para seleccionar un producto desde la imagen
  def test_handle_click_image_product(self, driver:webdriver.Remote):
    click_on_product(driver, MODE_CLICK_PRODUCT["image"])