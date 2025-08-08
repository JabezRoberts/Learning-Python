# how to do amazon price tracker project with selenium
from selenium import webdriver # web driver drives the chrome browser and does all our automated tasks
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new browser
driver  = webdriver.Chrome(options=chrome_options) # Setup a chrome driver

# open the web page
driver.get("https://en.wikipedia.org/wiki/Main_Page")


articles_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(articles_count.text)

driver.quit() # quit the entire thing