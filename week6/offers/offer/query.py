from django.db import models

from django.contrib.auth.models import User


class OfferQuerySet(models.QuerySet):

    def get_pending_offers(self):
        return self.filter(status='p')

    def get_accepted_offers(self):
        return self.filter(status='a')

    def get_offers_for_user(self, pk):
        return self.filter(author=User.objects.get(pk=pk), status__in=['r', 'a'])
