#the webdriver is the one which we can link between this and the browser
import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("yes")
        self.driver = webdriver.Chrome(PATH) 
        self.driver.get("https://www.python.org")
    
    #Note: when executing the programme always put test at the beginning else the programme will not run
    def test_example(self):
        assert False

    def test_example2(self):
        assert True

    #this will run after the setup is finished
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

"""
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) 
driver.get("https://orteil.dashnet.org/cookieclicker/")

#this line of code is for wait for 5 seconds until the programme when the programme is running
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]#this is for selecting the items in the shop by refrencing the position

actions = ActionChains(driver)#this action is used for performing an action on a chain of events
actions.click(cookie)

#this section of code is for selecting the cookie 5000 times
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    #if the num of cookies = to the price it'll buy the item in the shop
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
            

time.sleep(3600)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) #this is for using the chromedriver.exe

#this will take you to the web page
driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")#this is for selecting the link that is inside the webpage and enter it
link.click()#this is for clicking the entering the link

try:
    #Note: when the slenium enters a new page it'll need to wait for a period of time if no time is given it can accidently close automatically
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003")))
    element.clear()#this clears the previous text inside the text box if clear is not present then the text that you input would append to the previous text
    element.click()
    #this is to go back to the previous page
    driver.back()
    driver.back()
    driver.back()
    #the forward is to go back to the page that you've already visit
    driver.forward()
    driver.forward()
     
except:
    driver.quit()
time.sleep(120)

search = driver.find_element_by_name("s")#this is for interaction of the html object
search.send_keys("test")#this is for input the text in the search bar of ig
search.send_keys(Keys.RETURN)#this will return the results

try:
    #this is saying that it'll wait for any secocnd that you give until the EC has been pop up.
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:
    articles = main.find_element_by_tag_name("article")#this in the main category of finding the tag name of article
    #this section is for looping through the articles which have the class name of entry_summary 
    #and will print out the header.text
    for article in articles:
        header = articles.find_element_by_class_name("enrty_summary")
        print(header.text)
finally:
    driver.quit()
"""
