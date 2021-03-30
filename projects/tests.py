from django.test import TestCase
from .models import Project

# Dummy Test Data:
proj1 = {"title": "Sample project",
    "year": 2020,
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum vulputate pellentesque. Etiam porta elementum ullamcorper. Aliquam imperdiet ullamcorper dui ac rhoncus. Curabitur laoreet ullamcorper sodales. Donec ac ultrices nulla, nec tincidunt arcu. Maecenas id sapien at tortor vehicula molestie eu sed leo. Integer in feugiat elit, vitae fermentum nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus faucibus convallis elementum. Quisque at eros a mi vehicula sodales sit amet a massa. Integer finibus massa nec sem venenatis aliquam. Sed sit amet orci id odio ornare euismod. Proin sed porta orci. Nunc rutrum hendrerit leo ac rutrum. Pellentesque ornare tellus eget purus sollicitudin rutrum.",
    "technologies":"Software 1, Software 2",
    "categories": "Software, Mechanical Engineering, Data Science",
    "thumbnail": "",
    "hyperlink": "https:/10.1016/j.ijengsci.2020.103259",
}

proj2 = {"title": "Sample project",
    "year": 2020,
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum vulputate pellentesque. Etiam porta elementum ullamcorper. Aliquam imperdiet ullamcorper dui ac rhoncus. Curabitur laoreet ullamcorper sodales. Donec ac ultrices nulla, nec tincidunt arcu. Maecenas id sapien at tortor vehicula molestie eu sed leo. Integer in feugiat elit, vitae fermentum nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus faucibus convallis elementum. Quisque at eros a mi vehicula sodales sit amet a massa. Integer finibus massa nec sem venenatis aliquam. Sed sit amet orci id odio ornare euismod. Proin sed porta orci. Nunc rutrum hendrerit leo ac rutrum. Pellentesque ornare tellus eget purus sollicitudin rutrum.",
    "technologies":"Software 1, Software 2",
    "type": "Software, Mechanical Engineering, Data Science",
    "thumbnail": "",
    "hyperlink": "https:/10.1016/j.ijengsci.2020.103259",
    "publisher": "International Journal of Engineering Science",
}

# Test model creation
class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(**proj1)
        Project.objects.create(**proj2)
    
    def test_correct_publication_creation(self):
        # Get publication objects
        pub1 = Project.objects.get(title=proj1["title"])
        pub2 = Project.objects.get(title=proj2["title"])
        # Publication 1 assertions
        self.assertEqual(pub1.authors,proj1["authors"])
        self.assertEqual(pub1.year,proj1["year"])
        self.assertEqual(pub1.link,proj1["link"])
        self.assertEqual(pub1.type,proj1["type"])
        self.assertEqual(pub1.publisher,proj1["publisher"])
        # Publication 2 assertions
        self.assertEqual(pub2.authors,"")
        self.assertEqual(pub2.year,proj2["year"])
        self.assertEqual(pub2.type,proj2["type"])
        self.assertEqual(pub2.publisher,"")
        self.assertEqual(pub2.link,"")
    
    def test_publications_page_status_code(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['publications']), 2)