from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from offer.factories import OfferFactory, CategoryFactory, UserFactory
from offer.models import Offer, Category

from django.urls import reverse_lazy
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

import json


class OfferAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.offer = OfferFactory()
        self.other_offer = OfferFactory()
        self.category = CategoryFactory()
        self.user = UserFactory()

    def test_can_access_all_offers_from_offer_list(self):
        self.client.force_login(self.user)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse_lazy('offer:offer-list-api'))
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.offer.title)
        self.assertContains(response, self.other_offer.title)

    def test_can_view_single_offer(self):
        self.client.force_login(self.user)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse_lazy('offer:offer-detail-api', kwargs={'pk': self.offer.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.offer.title)
        self.assertNotContains(response, self.other_offer.title)

    def test_can_edit_an_offer(self):
        title = "New title"
        self.client.force_login(self.user)
        self.client.force_authenticate(user=self.user)

        response = self.client.put(reverse_lazy('offer:offer-detail-api', kwargs={'pk': self.offer.pk}), data={'title': title})
        self.offer.refresh_from_db()
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.offer.title, title)

    def test_can_create_an_offer(self):
        self.assertEqual(Offer.objects.count(), 2)
        self.client.force_login(self.user)
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'New',
            'description': 'Offer',
            'category': self.category.id
        }

        response = self.client.post(reverse_lazy('offer:offer-list-api'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Offer.objects.count(), 3)

    def test_can_delete_an_offer(self):
        self.assertEqual(Offer.objects.count(), 2)
        self.client.force_login(self.user)
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse_lazy('offer:offer-detail-api', kwargs={'pk': self.offer.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Offer.objects.count(), 1)

    def test_can_not_access_if_not_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('offer:offer-list-api'))
        response2 = self.client.get(reverse_lazy('offer:offer-detail-api', kwargs={'pk': self.offer.pk}))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response2.status_code, 401)

    def test_can_authenticate(self):
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)

        response = self.client.get(reverse_lazy('offer:offer-list-api'), {}, HTTP_AUTHORIZATION='JWT {}'.format(token))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.offer.title)
        self.assertContains(response, self.other_offer.title)

    def tearDown(self):
        self.client.logout()


class CategoryAPITests(APITestCase):
    pass
