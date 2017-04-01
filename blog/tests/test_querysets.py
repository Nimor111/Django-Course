from django.test import TestCase, Client
from django.contrib.auth.models import User
from .factories import TagFactory, BlogPostFactory

from django.urls import reverse
from .models import BlogPost
from faker import Factory


faker = Factory.create()


class CustomQuerySetTests(TestCase):

    def setUp(self):
        self.blog_post = BlogPostFactory()
        self.blog_post2 = BlogPostFactory(is_private=True)

    def test_get_private_posts_works_correctly(self):
        self.blog_post3 = BlogPostFactory(is_private=True)
        private_posts = BlogPost.objects.get_private_posts()

        self.assertEqual(len(private_posts), 2)

    def test_get_public_posts_works_correctly(self):
        self.blog_post3 = BlogPostFactory()
        public_posts = BlogPost.objects.get_public_posts()

        self.assertEqual(len(public_posts), 2)
