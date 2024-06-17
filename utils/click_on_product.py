from pages.inventory_page import InventoryPage
from utils.login import login
from utils.consts import USER_CREDENTIALS, URL_PATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_on_product(driver: webdriver.Remote, mode: str):
  login(
    driver, 
    USER_CREDENTIALS["username"]["standard_user"], 
    USER_CREDENTIALS["password"]["secret_sauce"]
  )
  
  driver.get(f'{URL_PATH}/inventory.html')
  inventory_page = InventoryPage(driver)
  current_url = driver.current_url
  print(f'La url de la página de invetario es: {current_url}')
  
  inventory_page.handle_click_on_product(mode)
  # Espera hasta que la URL cambie
  WebDriverWait(driver, 10).until(EC.url_contains(f'{URL_PATH}/inventory-item.html?id='))
  # Verifica que la URL es la esperada
  current_url = driver.current_url
  print(f'Click realizado satisfactoriamente...!! => {current_url}')