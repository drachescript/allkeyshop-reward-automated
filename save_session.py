import time
import json
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Load configuration from config.json
def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()

# Set up the webdriver using the path from the config file
chrome_service = Service(config["chromedriver_path"])
driver = webdriver.Chrome(service=chrome_service)

# Open Steam login page (manual login required)
driver.get("https://store.steampowered.com/login/")

# Wait for the user to log in manually
print("Please log in to Steam manually. Press Enter to continue once logged in.")
input("Press Enter when you are logged in and the page is loaded.")

# Wait for the page to load after login (you can adjust this time based on your needs)
time.sleep(5)

# Save cookies and localStorage after logging in
cookie_file = "cookies.pkl"
local_storage_file = "local_storage.pkl"

# Save Steam cookies
with open(cookie_file, "wb") as cookiesfile:
    pickle.dump(driver.get_cookies(), cookiesfile)
    print("Cookies saved successfully.")

# Save localStorage for Steam
local_storage = driver.execute_script("return window.localStorage;")
with open(local_storage_file, "wb") as local_storagefile:
    pickle.dump(local_storage, local_storagefile)
    print("LocalStorage saved successfully.")

# Now, go to AllKeyShop page
driver.get("https://www.allkeyshop.com/blog/reward-program/")

# Wait for AllKeyShop to load
time.sleep(5)

# Save AllKeyShop cookies
allkeyshop_cookie_file = "allkeyshop_cookies.pkl"
allkeyshop_local_storage_file = "allkeyshop_local_storage.pkl"

with open(allkeyshop_cookie_file, "wb") as cookiesfile:
    pickle.dump(driver.get_cookies(), cookiesfile)
    print("AllKeyShop cookies saved successfully.")

# Save localStorage for AllKeyShop
allkeyshop_local_storage = driver.execute_script("return window.localStorage;")
with open(allkeyshop_local_storage_file, "wb") as local_storagefile:
    pickle.dump(allkeyshop_local_storage, local_storagefile)
    print("AllKeyShop localStorage saved successfully.")

# Close the browser
driver.quit()
