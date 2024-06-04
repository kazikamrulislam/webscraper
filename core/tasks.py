# from celery import task, shared_task
# from quotescraper import celery_app
# from .scrapers import scrape
# from decouple import config

from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.by import By
from core.mongo_models import QuotesModelMongo


@shared_task
def scrape_data(url):
    driver = webdriver.Chrome()
    driver.get("http://quotes.toscrape.com/js/")
    quotes = driver.find_elements(By.XPATH, '//div[@class="quote"]')
    for quote in quotes:
        text = quote.find_element(By.XPATH, './/span[@class="text"]').text
        author = quote.find_element(By.XPATH, './/span/small[@class="author"]').text
        tags = [tag.text for tag in quote.find_elements(By.XPATH, './/div[@class="tags"]/a[@class="tag"]')]
        
        # print(text, author, tags)
        QuotesModelMongo.objects.create(text=text, author=author, tags=tags)

    driver.quit()



# driver = webdriver.Chrome()
# driver.get("http://quotes.toscrape.com/js/")
# driver.get(config('CRAWLING_URL'))
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
    
#     # print(text, author, tags)
#     QuotesModelMongo.objects.create(text=text, author=author, tags=tags)

# driver.quit()


# from selenium import webdriver

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

# driver.get('http://quotes.toscrape.com/js/')
# print(driver.title)

# from quotescraper import celery_app
# from core.tasks import run_crawler


# @celery_app
# def crawler_run():
#     run_crawler()


# from celery import shared_task
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @shared_task
# def scrape_website(url):
#     service = Service(ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get(url)
#     title = driver.title

#     driver.quit()

#     return title

# from core import scrape_website
# from celery import shared_task
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from core.mongo_models import QuotesModelMongo

# @shared_task
# def scrape_task(url):
#     return scrape_website(url)

# @shared_task
# def scrape_website(url):
#     # Initialize Selenium WebDriver
#     driver = webdriver.Chrome()
#     driver.get(url)

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     quotes = soup.find_all('div', class_='quote')

#     for quote in quotes:
#         text = quote.find('text').text
#         author = quote.find('author').text
#         tags = [tag.text for tag in quote.find_all('tags')]
        
#         QuotesModelMongo.objects.create(text=text, author=author, tags=tags)
    
#     driver.quit() # To Close WebDriver
