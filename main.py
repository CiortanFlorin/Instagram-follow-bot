from InstaFollower import InstaFollower

chrome_driver_path = "E:\development\chromedriver.exe"
SIMILAR_ACCOUNT = "igndotcom"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
URL = "https://www.instagram.com/"

driver = InstaFollower(chrome_driver_path)

driver.login(USERNAME, PASSWORD, URL)
driver.findusers(SIMILAR_ACCOUNT)
driver.follow()