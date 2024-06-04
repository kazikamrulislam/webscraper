# from django.views import View
# from core.services import maincrawle

# class TestView(View):
#     maincrawle.start()


# from django.shortcuts import render
# from django.http import JsonResponse
# from .tasks import scrape_website

# def start_scraping(request):
#     url = request.GET.get('url', 'http://quotes.toscrape.com/js/')
#     task = scrape_website.delay(url)
#     return JsonResponse({'task_id': task.id})


# from django.shortcuts import render
from .tasks import scrape_data
from django.http import HttpResponse

def scraping_run(request):
    url = "http://quotes.toscrape.com/js/"
    scrape_data.delay(url)
    return HttpResponse("Scraping task triggered.")