### AllKeyShop Wheel Automation
This script automates the process of interacting with the AllKeyShop Wheel, logging in with saved cookies, spinning the wheel, handling the result, and sending the prize to a Discord webhook.

## Features
- Steam Login: Automatically logs into Steam using saved cookies.
- AllKeyShop Login: Automatically logs into AllKeyShop using saved cookies.
- Wheel Spin: Clicks the wheel to spin it.
- Popup Handling: Closes the popup and sends the prize information (e.g., points, gift cards) to a Discord webhook.
- Re-spin: Spins the wheel again after a short wait.

Prerequisites
1. Install Python
Ensure you have Python 3.x installed. You can download it from python.org.

2. Install Dependencies
You need to install the required Python libraries. To do so, you can either use pip or run a batch file to install everything.

Option 1: Install using pip:
open cmd:
pip install selenium
pip install requests

Option 2: Simply run the provided install_requirements.bat batch file to install all dependencies automatically.

3. Download ChromeDriver (unless u download the releases or downloaded the whole code ignore this)
You'll need ChromeDriver for the script to work with Google Chrome. ChromeDriver is required for Selenium to control Chrome.

Download ChromeDriver from the official page.

Ensure that the version of ChromeDriver matches your installed version of Google Chrome. To check your version of Chrome, go to chrome://settings/help.

4. Edit the Configuration (config.json)
You'll need to configure the path for ChromeDriver and optionally set your Discord webhook URL.

Example config.json:

{
  "chromedriver_path": "chromedriver.exe", (leave like this if u downloaded from release or code)
  "webhook_url": "https://discord.com/api/webhooks/1234567890/abcdefg"
}
chromedriver_path: Provide the absolute path to chromedriver.exe. 

webhook_url: If you want to receive notifications via a Discord webhook, fill this in. If not, you can leave it blank.

Step-by-Step Setup
1. Save Cookies (Initial Login)
Before using the automation script, you need to log into Steam and AllKeyShop manually once and save the cookies.

To do this, run the save_session.py script by double-clicking run_save.bat or running the following in your terminal:

python save_session.py
This will:

Open the Steam login page, where you can log in manually.

Save the Steam cookies to cookies.pkl.

Open the AllKeyShop reward https://www.allkeyshop.com/blog/reward-program/ page, where you can log in manually and save the AllKeyShop cookies to allkeyshop_cookies.pkl. (might be a but buggy refresh and try again until you are logged into your account)

2. Run the Automation Script
After saving the cookies, you can run the main automation script.

To run wheel.py, you can either:

Run it directly:

python wheel.py

Or use the run_main.bat batch file to make it easier:

Double-click on run_main.bat to automatically start the script.

The script will:

Load the saved cookies for Steam and AllKeyShop.

Click the AllKeyShop wheel twice to spin it.

Handle the popup and send the result to your Discord webhook (if configured).

Optional: Schedule Script to Run Automatically Every Day
After confirming that the script works as expected, you can use Task Scheduler to run it automatically every day.

1. Open Task Scheduler
Press the Start button and search for Task Scheduler.

2. Create a New Task
In Task Scheduler, click on Create Basic Task in the right-hand pane.

Name the Task:

Enter a name (e.g., AllKeyShop Wheel Automation).

Optionally, add a description like "Runs the wheel automation script every day."

3. Set the Trigger
Choose Daily to run the task every day.

Set the start date and time for the task to run. Choose a time when your computer is typically on.

4. Set the Action
Select Start a Program and click Next.

In the Program/script field, browse to and select the run_wheel.bat file that you created earlier.

Leave Arguments and Start in empty, or set the directory for the batch file.

5. Finish Setup
Click Next, then Finish to schedule the task.

License
This project is licensed under the MIT License
