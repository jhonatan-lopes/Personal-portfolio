from django.test import TestCase
from .models import Experience, Education, Expertise, MyInfo

class PageTests(TestCase):

    def test_home_page_status_code(self):
        """Home page is responding. """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page_status_code(self):
        """About page is responding. """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

# Dummy Test Data:
dummy_edu_1 = {"title": "Education 1",
    "start_date": 2020,
    "institution": "Sample institution", 
}

dummy_edu_2 = {"title": "Education 2",
    "start_date": 2020,
    "end_date": 2021,
    "institution": "Sample institution", 
}

dummy_exp_1 = {"title": "Expertise 1"}
dummy_exp_2 = {"title": "Expertise 2"}

dummy_job_1 = {"title": "Job 1", "start_date": 2020}
dummy_job_2 = {"title": "Job 2", "start_date": 1985, "end_date": 1991}


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

class AboutPageTestCase(TestCase):
    def setUp(self):
        Education.objects.create(**dummy_edu_1)
        Education.objects.create(**dummy_edu_2)
        Expertise.objects.create(**dummy_exp_1)
        Expertise.objects.create(**dummy_exp_2)
        Experience.objects.create(**dummy_job_1)
        Experience.objects.create(**dummy_job_2)
        MyInfo.objects.create(my_initials="JP Lopes")
        MyInfo.load()

    def test_about_page_status_code(self):
        """About page is responding. """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_education_context(self):
        """About view sends adequate number of eduction objects."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['educations']), 2)
    
    def test_about_page_experience_context(self):
        """About view sends adequate number of experience objects."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['experiences']), 2)
    
    def test_about_page_expertise_context(self):
        """About view sends adequate number of expertises objects."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['expertises']), 2)