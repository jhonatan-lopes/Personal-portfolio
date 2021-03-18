from django.test import TestCase
from .models import Publication


# Dummy post data:
post1 = {"title": "The axisymmetric shrink fit problem subjected to torsion",
    "year": 2020,
    "type": "AR",
    "authors": "J.P. Lopes, D.A. Hills",
    "link": "10.1016/j.ijengsci.2020.103259",
    "publisher": "International Journal of Engineering Science",
}

post2 = {"title": "A sample book chapter",
    "year": 1991,
    "type": "BC",
}

# Test model creation
class PublicationTestCase(TestCase):
    def setUp(self):
        Publication.objects.create(**post1)
        Publication.objects.create(**post2)
    
    def test_correct_publication_creation(self):
        # Get publication objects
        pub1 = Publication.objects.get(title=post1["title"])
        pub2 = Publication.objects.get(title=post2["title"])
        # Publication 1 assertions
        self.assertEqual(pub1.authors,post1["authors"])
        self.assertEqual(pub1.year,post1["year"])
        self.assertEqual(pub1.link,post1["link"])
        self.assertEqual(pub1.type,post1["type"])
        self.assertEqual(pub1.publisher,post1["publisher"])
        # Publication 2 assertions
        self.assertEqual(pub2.authors,"")
        self.assertEqual(pub2.year,post2["year"])
        self.assertEqual(pub2.type,post2["type"])
        self.assertEqual(pub2.publisher,"")
        self.assertEqual(pub2.link,"")
    
    def test_publications_page_status_code(self):
        response = self.client.get('/publications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['publications']), 2)
