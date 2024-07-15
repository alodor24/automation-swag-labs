from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from utils.consts import FORM_DATA, STANDARD_USER, URL_PATH
from utils.login import login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutComplete:
  # Prueba para comprobar que se encuentra en la página Checkout Complete
  def test_is_checkout_complete(self, driver: webdriver.Remote):
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
      
      # Carga datos en el formulario
      checkout_step_one_page = CheckoutStepOnePage(driver)
      checkout_step_one_page.to_do_checkout(FORM_DATA)
      
      # Continua a la siguiente pantalla del proceso
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/checkout-step-two.html'))
      checkout_step_two_page = CheckoutStepTwoPage(driver)
      checkout_step_two_page.handle_click_on_finish()
      
      # Cuando se presiona el botón finish es redirigido a la página checkout complete
      WebDriverWait(driver, 10).until(EC.url_to_be(f'{URL_PATH}/checkout-complete.html'))
      checkout_complete_page = CheckoutCompletePage(driver)
      
      # Obtiene el título de la página
      title_page = checkout_complete_page.get_title_page()
      print(f'El título de la página es: {title_page}')