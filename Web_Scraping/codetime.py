from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from lxml import html

driver = webdriver.Chrome()
driver.get("https://app.software.com/login")

username_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.NAME, "commit")

username_input.send_keys("jacquesgomes66@gmail.com")
password_input.send_keys("canjica66")
submit_button.click()

protected = "https://app.software.com/dashboard/code_time"

session_requests = requests.session()

result = session_requests.get(
    protected,
    headers = dict(referer = protected)
)

tree = html.fromstring(result.content)
bucket_name = tree.xpath("//div[@class='my-2']/text()")

print(bucket_name)

print(result.ok)