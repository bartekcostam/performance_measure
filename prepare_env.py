import platform
import zipfile
import os
import urllib.request

print(platform.system())

def setup_environment():
    # Detect the operating system
    os_name = platform.system()

    # Download the appropriate portable Chrome and WebDriver
    if os_name == "Windows":
        chrome_url = "https://download_link_for_portable_chrome_for_windows"
        driver_url = "https://chromedriver.storage.googleapis.com/version/chromedriver_win32.zip"
    elif os_name == "Linux":
        chrome_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chrome-linux64.zip"
        driver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chromedriver-linux64.zip"
    else:
        raise Exception("Unsupported operating system")

    chrome_zip_path = os.path.join(os.getcwd(), "chrome.zip")
    driver_zip_path = os.path.join(os.getcwd(), "chromedriver.zip")
    chrome_path = os.path.join(os.getcwd(), "chrome")
    driver_path = os.path.join(os.getcwd(), "chromedriver")
    
    urllib.request.urlretrieve(chrome_url, chrome_zip_path)
    urllib.request.urlretrieve(driver_url, driver_zip_path)

    # Extract the portable Chrome and WebDriver
    with zipfile.ZipFile(chrome_zip_path, 'r') as zip_ref:
        zip_ref.extractall(chrome_path)
    with zipfile.ZipFile(driver_zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())

    # Make the WebDriver executable
    os.chmod(driver_path, 0o755)

    return chrome_path, driver_path
