from django.test import TestCase
from .models import Publication, MyInfo


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

class MyInfoTestCase(TestCase):

    def test_myinfo_load_create(self):
        """MyInfo.load method. It should return a MyInfo object with pk=1."""
        MyInfo.objects.create(my_initials="T User")
        myinfo = MyInfo.load()
        self.assertEqual(myinfo.pk,1)
    
    def test_myinfo_load_existing(self):
        """MyInfo.load method. It should return a MyInfo object with pk=1.
        If object doesn't exist, create it."""
        MyInfo.objects.create(my_initials="JP Lopes")
        myinfo = MyInfo(my_initials="T User")
        myinfo.save()
        self.assertEqual(myinfo.pk,1)
        self.assertEqual(myinfo.my_initials,"T User")
    
    def test_myinfo_save(self):
        """MyInfo.save method. There should still be only one instance
        after saving."""
        MyInfo.objects.create(my_initials="JP Lopes")
        myinfo = MyInfo(my_initials="T User")
        myinfo.save()
        self.assertEqual(myinfo.pk,1)
        self.assertEqual(myinfo.my_initials,"T User")
    
    def test_myinfo_delete(self):
        """Delete shouldn't alter anything """
        myinfo = MyInfo.objects.create(my_initials="JP Lopes")
        myinfo.delete()
        self.assertEqual(len(MyInfo.objects.all()),1)
        self.assertEqual(MyInfo.objects.get(pk=1),myinfo)

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
