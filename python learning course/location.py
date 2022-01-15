from selenium.webdriver.common.by import By

#this will define a specific page(in this case the homepage)
#and we can access in a certain way.
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass