# from celery import task, shared_task
# from quotescraper import celery_app
# from .scrapers import scrape

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://quotes.toscrape.com/js/")
# element = driver.find_element(By.CLASS_NAME, 'author')
# element = driver.find_elements(By.XPATH, '//div/')

'''
To fiend all single elements 
'''
# elements=driver.find_elements(By.XPATH, "//small[@class='author']")
# elements=driver.find_elements(By.XPATH, "//div/div/a[@class='tag']")
# elements=driver.find_elements(By.XPATH, "//div/span[@class='text']")

# for element in elements:
#     print(element.text)

'''
For fiend all elements specific div class
'''
# quotes = driver.find_elements(By.XPATH, '//div[@class="quote"]')

# for quote in quotes:
#     text = quote.find_element(By.XPATH, './/span[@class="text"]').text
#     author = quote.find_element(By.XPATH, './/span/small[@class="author"]').text
#     tags = [tag.text for tag in quote.find_elements(By.XPATH, './/div[@class="tags"]/a[@class="tag"]')]
    
#     print(text, author, tags)


# from selenium import webdriver

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

# driver.get('http://quotes.toscrape.com/js/')
# print(driver.title)

from quotescraper import celery_app

@celery_app.task(name="Run Crawler") #??name
def crawler_run():
    