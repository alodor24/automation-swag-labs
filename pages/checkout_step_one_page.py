from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
  """
  Clase que contiene los elementos del checkout step one
  """
  def __init__(self, driver: webdriver.Remote):
      self.driver = driver
      
  @property
  def __input_first_name(self):
    return self.driver.find_element(By.ID, 'first-name')
  
  @property
  def __input_last_name(self):
    return self.driver.find_element(By.ID, 'last-name')
  
  @property
  def __input_postal_code(self):
    return self.driver.find_element(By.ID, 'postal-code')
  
  @property
  def __h3_errorMessage(self):
    return self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']//h3")
  
  @property
  def __button_cancel(self):
    return self.driver.find_element(By.ID, 'cancel')
  
  @property
  def __button_continue(self):
    return self.driver.find_element(By.ID, 'continue')
  
  
  def handle_click_on_cancel(self):
    self.__button_cancel.click()
  
  
  def to_do_checkout(self, firstname, lastname, postalcode):
    """
    Método que se encarga de realizar el checkout
    Args:
    firstname: nombre del cliente
    lastname: apellido del cliente
    postalcode: código postal del cliente
    """
    self.__input_first_name.send_keys(firstname)
    self.__input_last_name.send_keys(lastname)
    self.__input_postal_code.send_keys(postalcode)
    self.__button_continue.click()
      
  
  def get_error_message(self):
      """
      Método que se encarga de obtener el mensaje de error
      Return: mensaje de error
      """
      error_element = self.__h3_errorMessage
      
      if (error_element):
          return error_element.text
          
      return None