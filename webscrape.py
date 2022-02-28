from flask import Blueprint, render_template, request
from base64 import encode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import datetime

webscrape_blueprint = Blueprint("webscrape", __name__)

#Opens the duunitori web page
url = "https://duunitori.fi/"
driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)

#Waits until the element is located on the page and then clicks it if it's present, quit if the element can't be located. 
#This eliminates possible "element not interactable exceptions"
try:
    cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gdpr-close")))
    cookies.click()
except:
    driver.quit()

#Finds the search bar, inputs and submits the job you want to search for
try:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-autocomplete"]/ul/li/input')))
    search.send_keys("Software Engineer")
    search.send_keys(Keys.RETURN)
except:
    driver.quit()


#Gets the first job posting on the page, saves the company name and clicks to open up the job posting
post = driver.find_elements(By.CLASS_NAME, "job-box__hover").get_attribute("data-position")

print(post)

companyName = post.get_attribute("data-company")
print(companyName)
    
post.click()

#Finds the paragraph where the date info is located, it'll be in the form of "Julkaistu 17.2." for example
#Adds the current year into the end of the string and then trims the "Julkaistu" from the beginning of the string
postDate = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/div[3]/p[2]/span[1]").text + datetime.datetime.today().strftime("%Y")
postDate = postDate[10:]
print(postDate)

location = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/div[3]/p[1]/a[2]/span").text
print(location)

role = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/div[3]/h1").text
print(role)

driver.quit()

