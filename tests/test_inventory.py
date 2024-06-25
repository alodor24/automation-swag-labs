from pages.inventory_page import InventoryPage
from utils.login import login
from utils.click_on_product import click_on_product
from utils.consts import USER_CREDENTIALS, URL_PATH, MODE_CLICK_PRODUCT
from selenium import webdriver
class TestInventory:
  # Prueba para comprobar si se encuentra en la página de inventario
  def test_is_inventory_page(self, driver: webdriver.Remote):
    isLoginSuccess = login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    if (isLoginSuccess):
      driver.get(f'{URL_PATH}/inventory.html')
      inventory_page = InventoryPage(driver)
      title_page = inventory_page.get_title_page()
      print(f'El título de la página es: {title_page}')
  
  
  # Prueba para comprobar si existen productos
  def test_exist_some_product(self, driver: webdriver.Remote):
    isLoginSuccess = login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    if (isLoginSuccess):
      driver.get(f'{URL_PATH}/inventory.html')
      inventory_page = InventoryPage(driver)
      products = inventory_page.exist_some_inventory_item()
    
      if (products > 0):
        print(f'La cantidad de productos visibles es: {products}')
      else:
        raise Exception('No existen productos para interactuar')
    
    
  # Prueba para seleccionar un producto desde el titulo
  def test_handle_click_title_product(self, driver: webdriver.Remote):
    click_on_product(driver, MODE_CLICK_PRODUCT["title"], 3)
    
    
  # Prueba para seleccionar un producto desde la imagen
  def test_handle_click_image_product(self, driver: webdriver.Remote):
    click_on_product(driver, MODE_CLICK_PRODUCT["image"], 2)
    
    
  # Prueba para agregar uno o más producto al carrito
  def test_handle_click_add_to_cart(self, driver: webdriver.Remote):
    isLoginSuccess = login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    if (isLoginSuccess):
      driver.get(f'{URL_PATH}/inventory.html')
      inventory_page = InventoryPage(driver)
      inventory_page.handle_click_add_to_cart(3)
      inventory_page.handle_click_add_to_cart(1)
      
      try:
        items = inventory_page.get_quantity_added_to_cart()
        
        if (items):
          output = f'Fueron añadidos al carrito {items} productos' if items > 1 else f'Fue añadido al carrito {items} producto'
          print(output)
        
      except:
        print('No fue seleccionado algún producto')
        
        
  # Prueba para remover uno o más producto del carrito
  def test_handle_click_remove_from_cart(self, driver: webdriver.Remote):
    isLoginSuccess = login(
      driver, 
      USER_CREDENTIALS["username"]["standard_user"], 
      USER_CREDENTIALS["password"]["secret_sauce"]
    )
    
    if (isLoginSuccess):
      driver.get(f'{URL_PATH}/inventory.html')
      inventory_page = InventoryPage(driver)
      
      # Agrega los siguientes productos al carrito
      inventory_page.handle_click_add_to_cart(3)
      inventory_page.handle_click_add_to_cart(1)
      
      # Verifica que la cantidad de productos agregados es correcta
      items_before = inventory_page.get_quantity_added_to_cart()
      print(f'Cantidad de productos en el carrito antes de remover: {items_before}')
      
      # Indica el o los productos a remover del carrito
      inventory_page.handle_click_remove_from_cart(1)
      
      try:
        # Verifica nuevamente la cantidad de productos existentes en el carrito
        items_after = inventory_page.get_quantity_added_to_cart()
        
        if (items_after):
          print(f'Cantidad de productos existen en el carrito luego: {items_after}')
        
      except:
        print('El carrito se encuentra vacío')
      