from django.test import TestCase, Client
from offer.factories import CategoryFactory, OfferFactory
from faker import Factory


from django.urls import reverse

faker = Factory.create()


# Create your tests here.
class IndexViewTests(TestCase):

    def setUp(self):
        self.offer = OfferFactory()
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('offer:index'))
        self.assertEqual(response.status_code, 200)

    def test_if_an_offer_is_displayed_correctly(self):
        response = self.client.get(reverse('offer:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.offer.title)
        self.assertNotContains(response, 'No image to display')
