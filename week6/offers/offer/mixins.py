from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from offer.models import Offer


class BaseUserPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return True


class CanUpdateOfferMixin(BaseUserPassesTestMixin):

    raise_exception = True

    def test_func(self):
        # import ipdb; ipdb.set_trace()
        offer = get_object_or_404(Offer, pk=self.kwargs.get('pk'))

        if not offer.author == self.request.user:
            return False

        return True and super().test_func()


class IsSuperUserMixin(BaseUserPassesTestMixin):

    raise_exception = True

    def test_func(self):
        if not self.request.user.is_superuser:
            return False

        return True and super().test_func()
