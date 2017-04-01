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


class CreateBlogViewTests(TestCase):

    def setUp(self):
        self.tag = TagFactory()
        self.tag2 = TagFactory()
        self.blog_post = BlogPostFactory()
        self.user = User.objects.create_user(username=faker.name(), password='pesho')

    def test_post_request_when_not_logged_in_is_invalid(self):
        self.assertEqual(BlogPost.objects.count(), 1)
        url = reverse('blog:create')
        response = self.client.post(url, data={'title': faker.name(), 'content': faker.text()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_post_request_when_logged_in_is_valid(self):
        self.client.login(username=self.user.username, password='pesho')
        self.assertEqual(BlogPost.objects.count(), 1)
        url = reverse('blog:create')
        response = self.client.post(url, data={'title': faker.name(), 'content': faker.text()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 2)

    def tearDown(self):
        self.client.logout()
