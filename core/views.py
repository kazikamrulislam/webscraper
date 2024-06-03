from django.views import View
from core.services import maincrawle

class TestView(View):
    maincrawle.start()