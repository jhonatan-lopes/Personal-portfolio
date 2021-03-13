from django.test import TestCase
from .models import Publication, Author


# Dummy post data:
post1 = {"title": "The axisymmetric shrink fit problem subjected to torsion",
    "year": 2020,
    "type": "AR",
    "link": "10.1016/j.ijengsci.2020.103259",
    "journal": "International Journal of Engineering Science",
}

post2 = {"title": "A sample book chapter",
    "year": 1991,
    "type": "BC",
}

auth1 = {'name': 'J. Doe'}

auth2 = {'name': 'T. User'}

# Create your tests here.
class PublicationTestCase(TestCase):
    def setUp(self):
        Author.objects.create(**auth1)
        Author.objects.create(**auth2)
        Publication.objects.create(**post1)
        Publication.objects.create(**post2)
    
    def test_correct_publication_creation(self):
        # Get publication objects
        pub1 = Publication.objects.get(title=post1["title"])
        pub2 = Publication.objects.get(title=post2["title"])
        # Get author objects
        author1 = Author.objects.get(name=auth1["name"])
        author2 = Author.objects.get(name=auth2["name"])
        # Add authors to publications
        pub1.authors.add(author1,author2)
        pub2.authors.add(author2)
        # Publication 1 assertions
        self.assertEqual(pub1.authors.all()[0],author1)
        self.assertEqual(pub1.authors.all()[1],author2)
        self.assertEqual(pub1.year,post1["year"])
        self.assertEqual(pub1.link,post1["link"])
        self.assertEqual(pub1.type,post1["type"])
        self.assertEqual(pub1.journal,post1["journal"])
        # Publication 2 assertions
        self.assertEqual(pub2.authors.all()[0],author2)
        self.assertEqual(pub2.year,post2["year"])
        self.assertEqual(pub2.type,post2["type"])

