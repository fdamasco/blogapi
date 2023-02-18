from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user1 = User.objects.create_user(
            username="test_user1", password="abc123")
        test_user1.save()

        # Create a post
        test_post = Post.objects.create(
            author=test_user1, title="Blog title", body="Body content")
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, "test_user1")
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, "Body content")
