from django.db import models


class OfferQuerySet(models.QuerySet):

    def get_pending_offers(self):
        return self.filter(status='p')

    def get_accepted_offers(self):
        return self.filter(status='a')
