import platform
import zipfile
import os
import urllib.request

print(platform.system())

def is_valid_zip(zip_path):
    """Check if the file is a valid zip file."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            return True
    except zipfile.BadZipFile:
        return False


def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except Exception as e:
        print(f"Error downloading from {url}. Error: {e}")
        return False


def setup_environment():
    print("Entering setup_environment function")
    # Detect the operating system
    os_name = platform.system()
    # Create the env/linux directory if it doesn't exist

    env_linux_path = os.path.join(os.getcwd(), "env", "linux")
    if not os.path.exists(env_linux_path):
        os.makedirs(env_linux_path)

    
     # Paths to the extracted Chrome and WebDriver
    chrome_path = os.path.join(env_linux_path, "chrome-linux64/chrome")
    driver_path = os.path.join(env_linux_path, "chromedriver-linux64/chromedriver")
    
    # Download the appropriate portable Chrome and WebDriver
    if os_name == "Windows":
        chrome_url = "https://download_link_for_portable_chrome_for_windows"
        driver_url = "https://chromedriver.storage.googleapis.com/version/chromedriver_win32.zip"
    elif os_name == "Linux":
        chrome_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chrome-linux64.zip"
        driver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chromedriver-linux64.zip"
    else:
        raise Exception("Unsupported operating system")
    
    chrome_zip_path = os.path.join(env_linux_path, "chrome.zip")
    driver_zip_path = os.path.join(env_linux_path, "chromedriver.zip")
    
    # Check if the zip files already exist
    if not os.path.exists(chrome_zip_path):
        if not download_file(chrome_url, chrome_zip_path):
            print("Failed to download Chrome. Exiting...")
            return None, None

    if not os.path.exists(driver_zip_path):
        if not download_file(driver_url, driver_zip_path):
            print("Failed to download ChromeDriver. Exiting...")
            return None, None
    print("123")
    # Extract the portable Chrome and WebDriver
    with zipfile.ZipFile(chrome_zip_path, 'r') as zip_ref:
        zip_ref.extractall(env_linux_path)
    with zipfile.ZipFile(driver_zip_path, 'r') as zip_ref:
        zip_ref.extractall(env_linux_path)

    # Paths to the extracted Chrome and WebDriver
    chrome_path = os.path.join(env_linux_path, "chrome-linux64/chrome")
    driver_path = os.path.join(env_linux_path, "chromedriver-linux64/chromedriver")

    # Make the WebDriver executable
    os.chmod(driver_path, 0o755)

    return chrome_path, driver_path

# Test the function
chrome, driver = setup_environment()
print("Chrome Path:", chrome)
print("Driver Path:", driver)