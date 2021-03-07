from django.test import TestCase
from .models import Publication

# Dummy post data:
post1 = {"authors": "J.P. Lopes, D.A. Hills",
    "title": "The axisymmetric shrink fit problem subjected to torsion",
    "abstract": "Lorem ipsum",
    "doi": "10.1016/j.ijengsci.2020.103259",
    "date_published": "2020",
}

post2 = {"authors": "J Doe",
    "title": "A sample article",
    "abstract": "Lorem ipsum",
    "doi": "12345",
    "date_published": "2021",
}

# Create your tests here.
class PublicationTestCase(TestCase):
    def setUp(self):
        Publication.objects.create(**post1)
        Publication.objects.create(**post2)
    
    def test_correct_publication_creation(self):
        pub1 = Publication.objects.get(title=post1["title"])
        pub2 = Publication.objects.get(title=post2["title"])
        self.assertEqual(pub1.authors,post1["authors"])
        self.assertEqual(pub1.abstract,post1["abstract"])
        self.assertEqual(pub1.doi,post1["doi"])
        self.assertEqual(pub1.date_published,post1["date_published"])
        self.assertEqual(pub2.authors,post2["authors"])
        self.assertEqual(pub2.abstract,post2["abstract"])
        self.assertEqual(pub2.doi,post2["doi"])
        self.assertEqual(pub2.date_published,post2["date_published"])

