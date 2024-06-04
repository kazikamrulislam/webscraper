import datetime
## if needed for converting time fot locsl time
# import pytz 

from django.conf import settings
from mongoengine import *




# class BaseModelMongo(Document):
#     """
#     Base model for other models
#     """
#     is_active = BooleanField(default=True)
#     created_at = DateTimeField(default=datetime.datetime.now)
#     updated_at = DateTimeField(default=datetime.datetime.now)
#     meta = {
#         'abstract': True,
#         # 'allow_inheritance': True,
#         # 'indexes': ['is_active'],
#     }


class QuotesModelMongo(Document):
    """
    Model for storing list of quotes
    """
    text = StringField(max_length=250)
    author = StringField(max_length=80)
    tags = ListField(StringField(max_length=255))

    # @classmethod
    # def create(cls, quote: str, author: str, tags: list):
        
    #     obj = cls(quote=quote, author=author, tags=tags).save()
    #     return obj