from selenium import webdriver
import time 

email = "ur email"
password = "ur password"
url = "website link that you want to login"

# Here webdriver have multiple function with different brower driver
# Example: Edge, FireFox, Chrome, etc. Here I use Chrome  
w_driver = webdriver.Chrome("chromedriver location")

w_driver.get(url) # This is obvious

# On website press F12 to check for input name element
#w_driver.find_element_by_name("email").send_keys(email)
#w_driver.find_element_by_name("password").send_keys(password)
#
#w_driver.find_element_by_css_element("input[type=\"submit\"] i").click()
#
#print("Success!")

w_driver.find_element_by_id("email").send_keys(email)
w_driver.find_element_by_id("password").send_keys(password)
w_driver.find_element_by_id("submit").click()

print("Logged in successfully")
# Refresh page to see ur login
time.sleep(3)
w_driver.get("ur url after login page")


