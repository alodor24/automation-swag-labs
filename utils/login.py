from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.consts import URL_PATH, ERROR_MESSAGE
from selenium import webdriver

def login(driver:webdriver.Remote, username: str, password: str):
  driver.get(URL_PATH)
  login_page = LoginPage(driver)
  login_page.to_do_login(
      username, 
      password
  )
  
  try:
    error_message = login_page.get_error_message()
    
    assert ERROR_MESSAGE["expect_message_user_locked"] in error_message or ERROR_MESSAGE["expect_message_user_do_not_match"] in error_message
    print(f'Mensaje de error es el esperado => {error_message}')
    
  except:
    print('Login realizado correctamente...!!')
  
    # Navegar a la página de inventario y obtener el título
    driver.get(f'{URL_PATH}/inventory.html')
    inventory_page = InventoryPage(driver)
    expect_message = inventory_page.get_title_page()
    print(f'Título de la página de inventario de productos => {expect_message}')