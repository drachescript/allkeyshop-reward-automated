# AllKeyShop Wheel Automation

This script automates the process of interacting with the **AllKeyShop Wheel**, logging in with saved cookies, spinning the wheel, handling the result, and sending the prize to a **Discord webhook**.

## Features
- **Steam Login**: Automatically logs into Steam using saved cookies.
- **AllKeyShop Login**: Automatically logs into AllKeyShop using saved cookies.
- **Wheel Spin**: Clicks the wheel to spin it.
- **Popup Handling**: Closes the popup and sends the prize information (e.g., points, gift cards) to a Discord webhook.
- **Re-spin**: Spins the wheel again after a short wait.
- **Discord Mention**: Mentions a specific user on Discord if the prize includes certain rewards (like €10 gift cards or the PS5 prize).

## Prerequisites

### 1. **Install Python**
Ensure you have **Python 3.x** installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2. **Install Dependencies**
You need to install the required Python libraries. You can install them using `pip`. Selenium and Requests

In your terminal, run:
```bash
pip install Selenium
pip install Requests
```
3. Download ChromeDriver
You'll need ChromeDriver for the script to work with Google Chrome. ChromeDriver is required for Selenium to control Chrome.

Download ChromeDriver: You can download it directly from ChromeDriver's official page. https://sites.google.com/chromium.org/driver/downloads

Ensure that the version of ChromeDriver matches your installed version of Google Chrome. You can check your version of Chrome by navigating to chrome://settings/help.

chromedriver_path: Provide the absolute path to the chromedriver.exe you downloaded.

webhook_url: Replace with your Discord webhook URL to send prize information.

4. Save Cookies (Initial Login)

Before using the automation script, you must log into Steam and AllKeyShop manually at least once and save the cookies.

For that start run_save.bat

This will:

Open the Steam login page, where you can log in manually.

Save the Steam cookies to cookies.pkl.

Open the AllKeyShop reward page, where you can log in manually and save the AllKeyShop cookies to allkeyshop_cookies.pkl.

6. Run the Automation Script
After saving the cookies, you can run the main automation script wheel.py:
or just run run_main.bat

Load the saved cookies for Steam and AllKeyShop.

Click the AllKeyShop wheel twice to spin it.

Handle the popup and send the result to the Discord webhook.

License
This project is licensed under the MIT License




