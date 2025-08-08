from selenium import webdriver # web driver drives the chrome browser and does all our automated tasks

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new browser
driver  = webdriver.Chrome(options=chrome_options) # Setup a chrome driver

# open a web page
driver.get("https://www.amazon.com")

# close the tabs and quit chrome with the program
driver.close() # closes a particular tab
driver.quit() # quit the entire thing