from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.inventory_page import InventoryPage
from utils.consts import STANDARD_USER, URL_PATH
from utils.login import login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutStepOne:
  # Prueba para comprobar el funcionamiento del botón Cancel
  def test_cancel_btn(self, driver: webdriver.Remote):
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
      
      # Hace click sobre el botón cancel
      checkout_step_one_page = CheckoutStepOnePage(driver)
      checkout_step_one_page.handle_click_on_cancel()
      
      current_url = driver.current_url
      assert current_url == f'{URL_PATH}/cart.html'
      print(f'Realizado satisfactoriamente...!! => {current_url}')