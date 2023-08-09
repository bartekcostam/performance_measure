import platform
import zipfile
import os
import urllib.request
import io
import progressbar
from messagebox import messageBox

def is_valid_zip(zip_path):
    """Check if the file is a valid zip file."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            return True
    except zipfile.BadZipFile:
        return False
    
def openMessageBox():
    messagebox = messageBox()
    messagebox.run()

def download_file(url, path):
    try:
        openMessageBox()
        def show_progress(block_num, block_size, total_size):
            global pbar
            pbar = None
            if pbar is None:
                pbar = progressbar.ProgressBar(maxval=total_size)
                pbar.start()

            downloaded = block_num * block_size
            if downloaded < total_size:
                pbar.update(downloaded)
            else:
                pbar.finish()
                pbar = None

        urllib.request.urlretrieve(url, path, show_progress)

        return True
    except Exception as e:
        print(f"Error downloading from {url}. Error: {e}")
        return False

def print_directory_structure(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def setup_environment():
    print("Entering setup_environment function")
    # Detect the operating system
    os_name = platform.system()

    # Create the env directory if it doesn't exist
    env_path = os.path.join(os.getcwd(), "env", os_name.lower())
    if not os.path.exists(env_path):
        os.makedirs(env_path)

    # Download the appropriate portable Chrome and WebDriver
    if os_name == "Windows":
        chrome_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/win64/chrome-win64.zip"
        driver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/win64/chromedriver-win64.zip"
        chrome_extract_folder = "chrome-win64"
        driver_extract_folder = "chromedriver-win64"
        chrome_executable = "chrome.exe"
        driver_executable = "chromedriver.exe"
    elif os_name == "Linux":
        chrome_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chrome-linux64.zip"
        driver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chromedriver-linux64.zip"
        chrome_extract_folder = "chrome-linux64"
        driver_extract_folder = "chromedriver-linux64"
        chrome_executable = "chrome"
        driver_executable = "chromedriver"
    else:
        raise Exception("Unsupported operating system")

    chrome_zip_path = os.path.join(env_path, "chrome.zip")
    driver_zip_path = os.path.join(env_path, "chromedriver.zip")

    # Check if the zip files already exist
    if not os.path.exists(chrome_zip_path):
        if not download_file(chrome_url, chrome_zip_path):
            print("Failed to download Chrome. Exiting...")
            return None, None

    if not os.path.exists(driver_zip_path):
        if not download_file(driver_url, driver_zip_path):
            print("Failed to download ChromeDriver. Exiting...")
            return None, None

    # Paths to the extracted Chrome and WebDriver
    chrome_extract_path = os.path.join(env_path, "chrome")
    driver_extract_path = os.path.join(env_path, "driver")

    # Extract the portable Chrome and WebDriver
    with zipfile.ZipFile(chrome_zip_path, 'r') as zip_ref:
        zip_ref.extractall(chrome_extract_path)
    with zipfile.ZipFile(driver_zip_path, 'r') as zip_ref:
        zip_ref.extractall(driver_extract_path)

    # Print the directory structure
    print("Chrome directory structure:")
    print_directory_structure(chrome_extract_path)
    print("Driver directory structure:")
    print_directory_structure(driver_extract_path)

    # Paths to the extracted Chrome and WebDriver
    chrome_path = os.path.join(chrome_extract_path, chrome_extract_folder, chrome_executable)
    driver_path = os.path.join(driver_extract_path, driver_extract_folder, driver_executable)
   
    # Make the WebDriver executable
    os.chmod(driver_path, 0o755)
    os.chmod(chrome_path, 0o755)


    return chrome_path, driver_path

# Test the function
chrome, driver = setup_environment()
print("Chrome Path:", chrome)
print("Driver Path:", driver)
