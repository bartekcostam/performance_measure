from prepare_env import setup_environment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def test_loading_speed(url):
    # Set up the environment and get the paths to the portable Chrome and WebDriver
    chrome_path, driver_path = setup_environment()

    # Create a Chrome Options object
    chrome_options = Options()
    chrome_options.binary_location = chrome_path

    # Create a WebDriver object using the ChromeDriver and Chrome Options
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # Use Selenium to test the loading speed
    start_time = time.time()
    driver.get(url)
    end_time = time.time()
    loading_time = end_time - start_time

    print(f"The loading time for {url} is {loading_time} seconds")

    driver.quit()
