from django.test import TestCase
from .models import Post
from publications.models import MyInfo

# Dummy Test Data:
dummy1 = {"title": "Sample post",
    "slug": "sample-post",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed interdum vulputate pellentesque. Etiam porta elementum ullamcorper. Aliquam imperdiet ullamcorper dui ac rhoncus. Curabitur laoreet ullamcorper sodales. Donec ac ultrices nulla, nec tincidunt arcu. Maecenas id sapien at tortor vehicula molestie eu sed leo. Integer in feugiat elit, vitae fermentum nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus faucibus convallis elementum. Quisque at eros a mi vehicula sodales sit amet a massa. Integer finibus massa nec sem venenatis aliquam. Sed sit amet orci id odio ornare euismod. Proin sed porta orci. Nunc rutrum hendrerit leo ac rutrum. Pellentesque ornare tellus eget purus sollicitudin rutrum.",
    "tags":"Tag1, Tag2, Tag3",
}

dummy2 = {"title": "Sample post 2",
    "slug": "sample-post-2",
    "content": "",
    "tags":"Tag1, Tag2, Tag3, Tag4, Tag5, Tag6",
}

class PostTestCase(TestCase):
    def setUp(self):
        MyInfo.objects.create(my_initials="JP Lopes")
        Post.objects.create(**dummy1)
        Post.objects.create(**dummy2)
    
    def test_correct_post_creation(self):
        "Post objects are created properly."
        # Get post objects
        post1 = Post.objects.get(title=dummy1["title"])
        post2 = Post.objects.get(title=dummy2["title"])
        # Post 1 assertions
        self.assertEqual(post1.slug,dummy1["slug"])
        self.assertEqual(post1.tags,dummy1["tags"])
        self.assertEqual(post1.content,dummy1["content"])
        # Post 2 assertions
        self.assertEqual(post2.slug,dummy2["slug"])
        self.assertEqual(post2.tags,dummy2["tags"])
        self.assertEqual(post2.content,dummy2["content"])
    
    def test_get_tags_string(self):
        """Test get_tags_string method. Returns a string of tags
        for less than 5 tags. Returns the five first tags + and n others
        if there are more than five. """
        post1 = Post.objects.get(title=dummy1["title"])
        post2 = Post.objects.get(title=dummy2["title"])
        self.assertEqual(post1.tags_list(),"Tag1, Tag2, Tag3")
        self.assertEqual(post2.tags_list(),
            "Tag1, Tag2, Tag3, Tag4, Tag5 and 1 others")

    def test_blog_page_status_code(self):
        """Blog list view renders properly. Renders two dummy projects"""
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 2)
    
    def test_post_detail_page_status_code(self):
        """Blog post detail views render properly for each dummy post."""
        post1 = Post.objects.get(title=dummy1["title"])
        post2 = Post.objects.get(title=dummy2["title"])
        response1 = self.client.get(post1.get_absolute_url())
        response2 = self.client.get(post2.get_absolute_url())
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

