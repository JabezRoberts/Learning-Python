# how to do amazon price tracker project with selenium
from selenium import webdriver # web driver drives the chrome browser and does all our automated tasks
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a new browser
driver  = webdriver.Chrome(options=chrome_options) # Setup a chrome driver

# open a web page
driver.get("https://www.amazon.com/SAMSUNG-Mini-LED-FreeSync-Adjustable-LS55CG970NNXGO/dp/B0CDQKYXTC/ref=sr_1_18?crid=1I86ICJ2QBW1F&dib=eyJ2IjoiMSJ9.O-E0P_q5rh56RljQEB5lTl45Erf-EUowmcRBJuPGq-7vV6iitXYUleJ9uJEBkHi7kcPuwmeBvXvz5fn-efHi0PAtU5oDsSZO2Wroir5NKixzGvPAXuGu7NdpPAOVHUf-x6CsL4g0gtkQJn-TA6K3CbMvQLN2f8vWiWjadLrVyPzJrZieRjd-EL11PvamXkTvA0-gYMsm8RSwevpi95hNG6hjSwaHFRrx1jEthJoAvAk.YiplfGtNKmnN7_idUo9D8F3YzPQQW4nHNHBolgozfjg&dib_tag=se&keywords=55+in+curved+tv&qid=1754660910&sprefix=55+in+cu,aps,151&sr=8-18")


price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# price dollar and price cents are currently html elements. To access the text in that html element we need the text content using .text 
print(f"The price is {price_dollar.text}.{price_cents.text}")



# close the tabs and quit chrome with the program
# # driver.close() # closes a particular tab
driver.quit() # quit the entire thing
