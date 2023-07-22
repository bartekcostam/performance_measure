from gui import GUI
from prepare_env import setup_environment
from selenium import webdriver
import time

def test_loading_speed(url):
    # Set up the environment and get the path to the WebDriver
    driver_path = setup_environment()

    # Use Selenium to test the loading speed
    driver = webdriver.Chrome(driver_path)
    start_time = time.time()
    driver.get(url)
    end_time = time.time()
    loading_time = end_time - start_time
    print(f"The loading time for {url} is {loading_time} seconds")
    driver.quit()
    # Display the result in the GUI
    # ...

gui = GUI()
gui.run()
