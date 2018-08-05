
from selenium import webdriver
import time
import requests
from PIL import Image
from io import BytesIO


# url i want to browse
url = "https://unsplash.com/"

# Using Selenium's webdriver to open the page
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get(url)

# scroll page and wait 5 seconds
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(5)
image_elements = driver.find_elements_by_css_selector("#gridMulti img")
i = 0

# Select image elements and print their URLs
for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1

driver.quit()