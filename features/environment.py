import os
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

BEFORE_SCENARIO = "before_scenario"
AFTER_SCENARIO = "after_scenario"


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    context.base_url = "https://www.saucedemo.com"
    os.makedirs("reports", exist_ok=True)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_dir = "reports"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(
            screenshot_dir, f"failure_{scenario.name}_{timestamp}.png"
        )
        context.driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved to: {screenshot_path}")

    context.driver.quit()