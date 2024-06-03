# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from django.utils import timezone
# # from .models import quotItem, ScrapRecord

# def scrap(urls):
#     options = webdriver.ChromOptions()
#     options.add_rguments("-incognito")
#     options.add_rguments("-headless")
#     options.add_rguments("-isable-dev-shmusage")
#     options.add_rguments("--no-sandbox")

#     brawser = webdriver.Chrom(
#         executable_path='user/locaal/bin/chromedriver', chrome_option=options)
    
#     browser.get(urls)

#     timeout = 10

#     try:
#         WebDriverWait(brawser, timeout).until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//div[@class='author']")
#             )
#         )
#     except TimeoutException:
#         print("Time out aiting for page to load")
#         browser.quit()
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from core.tasks import run_crawler




def maincrawle():
    driver = webdriver.Chrome()
    driver.get(config('CRAWLING_URL'))
    quotes = driver.find_elements(By.XPATH, '//div[@class="quote"]')

    for quote in quotes:
        text = quote.find_element(By.XPATH, './/span[@class="text"]').text
        author = quote.find_element(By.XPATH, './/span/small[@class="author"]').text
        tags = [tag.text for tag in quote.find_elements(By.XPATH, './/div[@class="tags"]/a[@class="tag"]')]
        
        print(text, author, tags)
    if quotes:
        run_crawler.delay(quotes)