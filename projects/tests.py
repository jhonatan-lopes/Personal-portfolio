from django.test import TestCase
from .models import Project

# Dummy Test Data:
dummy1 = {"title": "Sample project",
    "year": "2020",
    "slug": "sample-project",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum vulputate pellentesque. Etiam porta elementum ullamcorper. Aliquam imperdiet ullamcorper dui ac rhoncus. Curabitur laoreet ullamcorper sodales. Donec ac ultrices nulla, nec tincidunt arcu. Maecenas id sapien at tortor vehicula molestie eu sed leo. Integer in feugiat elit, vitae fermentum nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus faucibus convallis elementum. Quisque at eros a mi vehicula sodales sit amet a massa. Integer finibus massa nec sem venenatis aliquam. Sed sit amet orci id odio ornare euismod. Proin sed porta orci. Nunc rutrum hendrerit leo ac rutrum. Pellentesque ornare tellus eget purus sollicitudin rutrum.",
    "technologies":"Tag1, Tag2, Tag3",
    "categories": "Software, Mechanical Engineering, Data Science",
    "hyperlink": "https:/10.1016/j.ijengsci.2020.103259",
}

dummy2 = {"title": "Sample project 2",
    "year": "Ongoing",
    "slug": "sample-project-2",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum vulputate pellentesque. Etiam porta elementum ullamcorper. Aliquam imperdiet ullamcorper dui ac rhoncus. Curabitur laoreet ullamcorper sodales. Donec ac ultrices nulla, nec tincidunt arcu. Maecenas id sapien at tortor vehicula molestie eu sed leo. Integer in feugiat elit, vitae fermentum nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus faucibus convallis elementum. Quisque at eros a mi vehicula sodales sit amet a massa. Integer finibus massa nec sem venenatis aliquam. Sed sit amet orci id odio ornare euismod. Proin sed porta orci. Nunc rutrum hendrerit leo ac rutrum. Pellentesque ornare tellus eget purus sollicitudin rutrum.",
    "technologies":"Tag1, Tag2, Tag3, Tag4, Tag5, Tag6",
    "categories": "Software, Firmware, Data Science",
}

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(**dummy1)
        Project.objects.create(**dummy2)
    
    def test_correct_project_creation(self):
        # Get project objects
        proj1 = Project.objects.get(title=dummy1["title"])
        proj2 = Project.objects.get(title=dummy2["title"])
        # Project 1 assertions
        self.assertEqual(proj1.slug,dummy1["slug"])
        self.assertEqual(proj1.year,dummy1["year"])
        self.assertEqual(proj1.hyperlink,dummy1["hyperlink"])
        self.assertEqual(proj1.technologies,dummy1["technologies"])
        self.assertEqual(proj1.categories,dummy1["categories"])
        self.assertEqual(proj1.content,dummy1["content"])
        # Project 2 assertions
        self.assertEqual(proj2.slug,dummy2["slug"])
        self.assertEqual(proj2.year,dummy2["year"])
        self.assertEqual(proj2.hyperlink,"")
        self.assertEqual(proj2.technologies,dummy2["technologies"])
        self.assertEqual(proj2.categories,dummy2["categories"])
        self.assertEqual(proj2.content,dummy2["content"])
    
    def test_get_tags_string(self):
        """Test get_tags_string method. Returns a string of tags
        for less than 5 tags. Returns the five first tags + and n others
        if there are more than five. """
        proj1 = Project.objects.get(title=dummy1["title"])
        proj2 = Project.objects.get(title=dummy2["title"])
        self.assertEqual(proj1.technologies_list(),"Tag1, Tag2, Tag3")
        self.assertEqual(proj2.technologies_list(),
            "Tag1, Tag2, Tag3, Tag4, Tag5 and 1 others")

    def test_projects_page_status_code(self):
        """List view renders properly. Renders two dummy projects"""
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 2)
    
    def test_project_detail_page_status_code(self):
        """Detail views render properly for each dummy project."""
        proj1 = Project.objects.get(title=dummy1["title"])
        proj2 = Project.objects.get(title=dummy2["title"])
        response1 = self.client.get(proj1.get_absolute_url())
        response2 = self.client.get(proj2.get_absolute_url())
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

