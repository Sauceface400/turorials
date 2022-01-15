from selenium.webdriver.support.ui import WebDriverWait
#this file represents one element for the whole page so that it is quick access 
#so that we can change the element

#when ever we want to set the value it needs to go to this proccess
class BasePageElement(object):
    #this is for setting the value
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)) #lambda stands for anonymouse function and locator is to locate the element
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)
    
    #this is for getting the value
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
