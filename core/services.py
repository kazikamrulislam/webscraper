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
    

