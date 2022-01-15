from location import *
from element import BasePageElement

##this section is for accessing the element##
class SearchTextElemnt(BasePageElement):
    locator = "q"
##--##

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):
    #this is called the descripter
    search_text_elements = SearchTextElemnt()

    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)#*this means unpacked which is maked it into a single object
        element.click()

#this will run if the results are false(does not match with the search results)
class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source 