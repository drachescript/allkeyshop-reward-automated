import time
import pickle
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Load configuration from config.json
def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()

# Set up the webdriver using the path from the config file
chrome_service = Service(config["chromedriver_path"])
driver = webdriver.Chrome(service=chrome_service)

# Open Steam login page (Steam cookies are saved on this domain)
driver.get("https://store.steampowered.com/login/")

# Load and apply Steam cookies for Steam domain
try:
    # Load cookies from the file for Steam (ensure cookies are for Steam domain)
    with open("cookies.pkl", "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        if cookies:  # Check if cookies are not empty
            for cookie in cookies:
                # Only add cookies to the Steam domain
                if "steampowered" in cookie["domain"]:
                    driver.add_cookie(cookie)
            driver.refresh()
            print("Steam cookies loaded successfully.")
        else:
            print("No Steam cookies found.")
except Exception as e:
    print(f"Error loading Steam cookies: {e}")

# Now, go to AllKeyShop page
driver.get("https://www.allkeyshop.com/blog/reward-program/")

# Wait for AllKeyShop to load (can be adjusted based on your needs)
time.sleep(5)

# Load and apply AllKeyShop cookies for AllKeyShop domain
try:
    # Check if the AllKeyShop cookies file exists
    with open("allkeyshop_cookies.pkl", "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        if cookies:  # Check if cookies are not empty
            for cookie in cookies:
                # Only add cookies to the AllKeyShop domain
                if "allkeyshop" in cookie["domain"]:
                    driver.add_cookie(cookie)
            driver.refresh()
            print("AllKeyShop cookies loaded successfully.")
        else:
            print("No AllKeyShop cookies found.")
except FileNotFoundError:
    print("AllKeyShop cookies file not found. Skipping AllKeyShop cookies.")
except Exception as e:
    print(f"Error loading AllKeyShop cookies: {e}")

# Function to send the result to the Discord Webhook
def send_to_webhook(message):
    webhook_url = config["webhook_url"]
    payload = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Webhook sent successfully.")
        else:
            print(f"Failed to send webhook: {response.status_code}")
    except Exception as e:
        print(f"Error sending webhook: {e}")

# Function to click the center of the wheel
def click_wheel():
    try:
        # Locate the wheel element
        wheel_element = driver.find_element(By.CSS_SELECTOR, '.wheel-wheel canvas')
        
        # Get the center of the canvas
        actions = ActionChains(driver)
        actions.move_to_element(wheel_element).click().perform()
        print("Wheel clicked.")
    except Exception as e:
        print(f"Error clicking the wheel: {e}")

# Function to handle the result from the popup and send to webhook
def handle_popup_and_send():
    try:
        # Wait for the popup to appear
        time.sleep(15)  # Wait for the result of the wheel spin

        # Find the popup content
        popup_content = driver.find_element(By.CSS_SELECTOR, '.modal-body h3')
        prize_text = popup_content.text
        print(f"Prize: {prize_text}")

        send_to_webhook(f"Congratulations! {prize_text}")

        # Close the popup
        close_button = driver.find_element(By.CSS_SELECTOR, '.modal-content .mini-close')
        close_button.click()
        print("Popup closed.")

    except Exception as e:
        print(f"Error handling popup: {e}")

# Function to run the entire process: Spin and wait for the result
def run_spin_and_get_result():
    click_wheel()  # First click to spin the wheel
    time.sleep(2)  # Wait 1-2 seconds before the second click
    click_wheel()  # Second click to spin the wheel

    # Handle the popup after spinning
    handle_popup_and_send()

    # Wait before repeating the spin
    time.sleep(3)

    # Spin again if needed
    click_wheel()  # Spin again
    time.sleep(2)  # Wait 1-2 seconds before the second click
    click_wheel()  # Second click to spin the wheel again

    # Handle the popup after the second spin
    handle_popup_and_send()

# Run the process
run_spin_and_get_result()

# Close the browser
driver.quit()
