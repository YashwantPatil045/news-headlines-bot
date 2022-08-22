from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
from datetime import datetime
import sys

# app_path = os.path.dirname(sys.executable)

now = datetime.now()
today = now.strftime('%d%b%Y')


website = "https://www.thesun.co.uk/sport/"
chrome_driver_path = "chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = Options()
options.headless = True
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class= "teaser__copy-container"]')

titles = []
sub_titles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    sub_title = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute('href')

    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)

my_dict = {"title": titles, "Subtitle": sub_titles, "Links": links}
headlines = pd.DataFrame(my_dict)

file_name = f'headlines--{today}.csv'
# final_path = os.path.join(app_path, file_name)
headlines.to_csv(file_name)

driver.quit()
