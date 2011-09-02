import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from models import Collection

class CollectionViewsTest(TestCase):
    "Test the collections pages"

    def test_collection_exists(self):
        "Check that the collections pages work"
        
        response = self.client.get('/collections/slug/')
        self.assertEqual(response.status_code, 404)

        collection = Collection(create_timestamp=datetime.datetime.now(),
                                title='Title', subtitle='Article',
                                description='asdf', slug='slug')
        collection.save()
        
        response = self.client.get(reverse('collection_page', args=[collection.slug]))
        self.assertEqual(response.status_code, 200)
