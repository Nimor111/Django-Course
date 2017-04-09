import tempfile
from django.test import TestCase, Client
from PIL import Image
from offer.factories import CategoryFactory, OfferFactory, UserFactory
from faker import Factory

from offer.models import Offer, Category, User

from moneyed import Money, EUR

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


class OfferCreateViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = CategoryFactory()
        self.user = UserFactory()

    def test_cannot_create_offer_if_user_not_logged(self):
        data = {
            'title': faker.word(),
            'description': faker.text(),
            'category': self.category,
        }

        response = self.client.post(reverse('offer:offer-create'), data=data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(0, Offer.objects.count())

    def test_can_create_offer_if_user_logged(self):
        image = Image.new('RGB', (100, 100), color='green')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(tmp_file.name)

        # I don't like this
        # price = Money(100, EUR)

        data = {
            'title': faker.word(),
            'description': faker.text(),
            'image': tmp_file,
            'category': self.category.id,
        }

        url = reverse('offer:offer-create')

        logged = self.client.force_login(self.user)
        response = self.client.post(url, data=data)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Offer.objects.count())

    def tearDown(self):
        self.client.logout()


class OffersByCategoryViewTests(TestCase):

    def setUp(self):
        self.category = CategoryFactory()
        self.client = Client()
        self.user = UserFactory()
        self.url = reverse('offer:category', kwargs={'pk': self.category.pk})

    def test_for_zero_offers_in_a_category(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'No offers for now!')

    def test_for_offers_in_category(self):
        offer = OfferFactory(category=self.category)
        offer2 = OfferFactory(category=self.category)
        self.assertEqual(2, Offer.objects.count())

        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, offer.title)
        self.assertContains(response, offer2.title)


class StatisticViewTests(TestCase):

    def setUp(self):
        self.category = CategoryFactory()
        self.client = Client()
        self.url = reverse('offer:statistics')

    def test_number_of_offers_for_category_is_correct_when_not_zero(self):
        offer = OfferFactory(category=self.category)
        offer2 = OfferFactory(category=self.category)

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, '{}'.format(self.category.name))
        self.assertContains(response, '2')

    def test_number_of_offers_for_cat_is_0_when_no_offers(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, '{}'.format(self.category.name))
