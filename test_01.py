from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options();
options.add_argument("--headless");
driver = webdriver.Chrome(options=options);
driver.get("https://www.guvi.in");
print(driver.title);
