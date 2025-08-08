# how to do amazon price tracker project with selenium
from selenium import webdriver # web driver drives the chrome browser and does all our automated tasks
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new browser
driver  = webdriver.Chrome(options=chrome_options) # Setup a chrome driver

# open the web page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# How to click on something
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
article_count.click()

# we can use link text to do the same thing
# Eg. let's click on a link called content portals
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()


# How to type
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python") # sends keyboard input


# after importing from selenium.webdriver.common.keys import Keys
search_bar.send_keys("Python", Keys.ENTER)


# complete form to Angela's demo website - COMMENT OUT PREVIOUS CODE
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Jay") # sends keyboard input

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Uchiha") # sends keyboard input

# after importing from selenium.webdriver.common.keys import Keys
email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("name@test.com")

# Now for the send button
send_button = driver.find_element(By.CSS_SELECTOR, value="form button")
send_button.click()
driver.quit() # quit the entire thing