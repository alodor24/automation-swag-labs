from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.consts import USER_CREDENTIALS, URL_PATH
from selenium import webdriver
class TestInventory:
  # Prueba para comprobar si existen productos
  def test_exist_some_product(self, driver:webdriver.Remote):
    driver.get(URL_PATH)
    login_page = LoginPage(driver)
    login_page.to_do_login(
        USER_CREDENTIALS["username"]["standard_user"], 
        USER_CREDENTIALS["password"]["secret_sauce"]
    )
    print('Login realizado correctamente...!!')
    
    # Navegar a la página de inventario y obtener el título
    driver.get(f'{URL_PATH}/inventory.html')
    inventory_page = InventoryPage(driver)
    expect_message = inventory_page.get_title_page()
    print(f'Título de la página de inventario de productos => {expect_message}')
    
    # Comprobar si existen productos
    products = inventory_page.exist_some_inventory_item()
    assert products > 0, 'No existen productos para interactuar'
    print(f'La cantidad de productos visibles es: {products}')