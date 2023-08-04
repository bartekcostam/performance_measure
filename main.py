from gui import GUI
from prepare_env import setup_environment
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_test():
    # Implement your test logic here
    url = gui.url.get()  # Get the URL from the GUI entry field
    xpath = gui.xpath.get()  # Get the XPath from the GUI entry field
    headless_mode = gui.is_headless_mode()
    print(f"Starting test for URL: {url}")
    num_iterations = gui.get_num_iterations()
    results = []
    for i in range(num_iterations):
        print(f"Running iteration {i + 1}")
        loading_time, element_time = test_loading_speed(url, xpath,headless_mode)
        results.append((i + 1, loading_time, element_time))

    # Save the results to a CSV file
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Iteration', 'Loading Time (seconds)', 'Element Time (seconds)'])  # Write the header row
        writer.writerows(results)  # Write the results

    print("Test complete. Results saved to results.csv.")

def test_loading_speed(url, xpath,headless_mode):
    # Set up the environment and get the path to the WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "./chrome_browser/win/browser/Chrome.exe"
    chrome_options.add_argument("--incognito")
    
    if headless_mode:
        chrome_options.add_argument("--headless")
    # Use Selenium to test the loading speed
    driver = webdriver.Chrome("./chrome_browser/win/driver/chromedriver.exe", options=chrome_options)
    start_time = time.time()

    driver.get(str(url))

    end_time = time.time()
    loading_time = end_time - start_time

    # Wait for the element to be available
    element_start_time = time.time()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element_end_time = time.time()
    element_time = element_end_time - element_start_time

    print(f"The loading time for {url} is {loading_time} seconds")
    print(f"The time for the element at {xpath} to be available is {element_time} seconds")
    driver.quit()

    return loading_time, element_time


gui = GUI(start_test)
gui.run()