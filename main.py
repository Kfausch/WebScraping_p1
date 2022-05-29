import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#webdriver-manager pkg
from webdriver_manager.chrome import ChromeDriverManager

#Options keeps Chrome open instead of instantly closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s = Service('C:/Users/kfaus/.wdm/drivers/chromedriver/win32/102.0.5005.61/chromedriver.exe')
driver = webdriver.Chrome(service= s, options=chrome_options)
page_url = "https://witcher.fandom.com/wiki/Category:Characters_in_the_stories"
driver.get(page_url)

#clicks accept if there is a prompt for accepting cookeis
#time.sleep(3)
#driver.find_element(By.XPATH, '//div[text()="ACCEPT"').click()

book_category = driver.find_elements_by_class_name('category-page__member-link')

books = []
for category in book_category:
    book_url = category.get_attribute('href')
    book_name = category.text
    books.append({'book_name': book_name, 'url': book_url})

character_list = []

for book in books:
    driver.get(book['url'])
    character_elements = driver.find_elements_by_class_name('category-page__member-link')

    for char in character_elements:
        character_list.append({'book': book['book_name'],'character': char.text})

character_df = pd.DataFrame(character_list)
character_df['book'].value_counts().plot(kind="bar")
plt.show()