# how to do amazon price tracker project with selenium
from selenium import webdriver # web driver drives the chrome browser and does all our automated tasks
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new browser
driver  = webdriver.Chrome(options=chrome_options) # Setup a chrome driver

# open a web page
driver.get("https://www.python.org")

# get the search bar
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar) # it gives a selenium element. Use .tag_name to get the text, tag name, or other attributes
print(search_bar.tag_name) # OR print(search_bar.get_attribute("placeholder"))  


# Find element by ID
button = driver.find_element(By.ID, value="submit")
print(button.size) # console logs {'height': 40, 'width': 46}


# find element by CSS Selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value="documentation-widget a")
print(documentation_link.text)


# When you still can't find an element use XPath - right click copy xpath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# We have so far only used singular find when we use find_element but for everything we did we can use find_elements. Will return them in a list
documentation_link = driver.find_elements(By.CSS_SELECTOR, value="documentation-widget a")

# close the tabs and quit chrome with the program
# # driver.close() # closes a particular tab
driver.quit() # quit the entire thing
