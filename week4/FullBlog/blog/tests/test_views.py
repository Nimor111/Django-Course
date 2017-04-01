from django.test import TestCase, Client
from django.contrib.auth.models import User
from .factories import TagFactory, BlogPostFactory

from django.urls import reverse
from .models import BlogPost
from faker import Factory


faker = Factory.create()


class IndexViewTests(TestCase):

    def setUp(self):
        self.tag = TagFactory()
        self.tag2 = TagFactory()
        self.blog_post = BlogPostFactory()
        self.client = Client()
        self.user = User.objects.create_user(username=faker.name(), password='pesho')

    def test_index_does_not_show_private_posts_with_user_logged_out(self):
        self.blog_post2 = BlogPostFactory(is_private=True)

        response = self.client.get(reverse('blog:index'))
        self.assertEqual(200, response.status_code)

        self.assertContains(response, self.blog_post.title)
        self.assertNotContains(response, self.blog_post2.title)

    def test_index_shows_private_posts_with_user_logged_in(self):
        self.blog_post2 = BlogPostFactory(is_private=True)
        self.client.login(username=self.user.username, password='pesho')

        response = self.client.get(reverse('blog:index'))
        self.assertEqual(200, response.status_code)

        self.assertContains(response, self.blog_post.title)
        self.assertContains(response, self.blog_post2.title)

    def test_index_shows_all_public_posts(self):
        self.blog_post2 = BlogPostFactory()

        response = self.client.get(reverse('blog:index'))
        self.assertEqual(200, response.status_code)

        self.assertContains(response, self.blog_post.title)
        self.assertContains(response, self.blog_post2.title)

    def test_index_shows_tags_for_blog_posts(self):
        self.blog_post.tags.add(self.tag)
        response = self.client.get(reverse('blog:index'))

        self.assertContains(response, self.tag.name)


class BlogPostCreateTests(TestCase):

    def setUp(self):
        self.tag = TagFactory()
        self.tag2 = TagFactory()
        self.blog_post = BlogPostFactory()
        self.user = User.objects.create_user(username=faker.name(), password='pesho')

    def test_create_blog_post_works_correctly(self):
        pass
