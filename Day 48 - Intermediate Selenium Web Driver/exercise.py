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

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)

# Event Names
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_names:
    print(name.text)
    
events = {}

# Now to put them all together
for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "event" : event_names[n].text
    }
print(events)


driver.quit() # quit the entire thing
