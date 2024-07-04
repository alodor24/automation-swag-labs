from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.consts import STANDARD_USER, URL_PATH
from utils.login import login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCart:
  # Prueba para comprobar el funcionamiento del botón Continue Shopping
  def test_continue_shopping_btn(self, driver: webdriver.Remote):
    isLoginSuccess = login(driver, STANDARD_USER)
    
    if (isLoginSuccess):
      # Ingresa a la página de inventario de productos y hace click en el carrito de compras
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/inventory.html'))
      inventory_page = InventoryPage(driver)
      inventory_page.handle_click_on_shopping_cart()
      
      # Redirige a la página del carrito y hace click en el botón continue shopping
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/cart.html'))
      cart_page = CartPage(driver)
      cart_page.handle_click_on_continue_shopping()
      
      # Espera hasta ser redirigido a la página de productos
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/inventory.html'))
      current_url = driver.current_url
      assert current_url == f'{URL_PATH}/inventory.html'
      print(f'Realizado satisfactoriamente...!! => {current_url}')
      
      
  # Prueba para comprobar el funcionamiento del botón Ckeckout
  def test_checkout_btn(self, driver: webdriver.Remote):
    isLoginSuccess = login(driver, STANDARD_USER)
    
    if (isLoginSuccess):
      # Ingresa a la página de inventario de productos y hace click en el carrito de compras
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/inventory.html'))
      inventory_page = InventoryPage(driver)
      inventory_page.handle_click_on_shopping_cart()
      
      # Redirige a la página del carrito y hace click en el botón Checkout
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/cart.html'))
      cart_page = CartPage(driver)
      cart_page.handle_click_on_checkout()
      
      # Espera hasta ser redirigido a la primera página del proceso de compra
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/checkout-step-one.html'))
      current_url = driver.current_url
      assert current_url == f'{URL_PATH}/checkout-step-one.html'
      print(f'Realizado satisfactoriamente...!! => {current_url}')