from django.test import TestCase
from .models import Publication
from main.models import MyInfo

# Dummy post data:
post1 = {"title": "The axisymmetric shrink fit problem subjected to torsion",
    "year": "2020",
    "kind": Publication.ARTICLE,
    "authors": "JP Lopes, DA Hills",
    "link": "10.1016/j.ijengsci.2020.103259",
    "publisher": "International Journal of Engineering Science",
}

post2 = {"title": "A sample book chapter",
    "year": "1999",
    "kind": Publication.BOOK,
}

class PublicationTestCase(TestCase):
    def setUp(self):
        Publication.objects.create(**post1)
        Publication.objects.create(**post2)
        MyInfo.objects.create(my_initials="JP Lopes")
    
    def test_correct_publication_creation(self):
        # Get publication objects
        pub1 = Publication.objects.get(title=post1["title"])
        pub2 = Publication.objects.get(title=post2["title"])
        # Publication 1 assertions
        self.assertEqual(pub1.authors,post1["authors"])
        self.assertEqual(pub1.year,post1["year"])
        self.assertEqual(pub1.link,post1["link"])
        self.assertEqual(pub1.kind,post1["kind"])
        self.assertEqual(pub1.publisher,post1["publisher"])
        # Publication 2 assertions
        self.assertEqual(pub2.authors,"")
        self.assertEqual(pub2.year,post2["year"])
        self.assertEqual(pub2.kind,post2["kind"])
        self.assertEqual(pub2.publisher,"")
        self.assertEqual(pub2.link,"")

    def test_authors_list(self):
        """authors_list method should return my_initials under strong tags
        e.g. "JP Lopes, DA Hills" with "JP Lopes" for my initials should
        return "<strong>JP Lopes</strong>, DA Hills".
        """
        pub1 = Publication.objects.get(title=post1["title"])
        self.assertEqual(pub1.authors_list(),"<strong>JP Lopes</strong>, DA Hills")


class PublicationsPageTestCase(TestCase):
    def setUp(self):
        MyInfo.objects.create(my_initials="JP Lopes")
        Publication.objects.create(**post1)
        Publication.objects.create(**post2)

    def test_publications_page_status_code(self):
        response = self.client.get('/publications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['publications']), 2)
