from pages.login_page import LoginPage
from utils.consts import URL_PATH
from selenium import webdriver

def login(driver:webdriver.Remote, username: str, password: str):
  """
  Método que se encarga de realizar el login
  Args:
  username: nombre de usuario
  password: contraseña
  Return: true si se ha realizado correctamente
  """
  driver.get(URL_PATH)
  login_page = LoginPage(driver)
  
  login_page.to_do_login(
      username, 
      password
  )
  
  try:
    error_message = login_page.get_error_message()
  
    if error_message:
      return False
    
  except:
    return True