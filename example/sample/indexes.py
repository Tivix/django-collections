import datetime
from haystack.indexes import *
from sample.models import CollectionItem

class CollectionItemIndex(SearchIndex):
    title = CharField(document=True, use_template=True)
    description = CharField(model_attr='user')
    image = ImageField(model_attr='image')
    publish_time = DateTimeField(model_attr='publish_time')
    url = UrlField(model_attr='url')

    def index_queryset(self):
        "Used when the entire index for model is updated."
        return CollectionItem.objects.all()
