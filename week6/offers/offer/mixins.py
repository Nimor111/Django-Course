from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from offer.models import Offer

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseUserPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return True


class CanUpdateOfferMixin(BaseUserPassesTestMixin):

    raise_exception = False

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


class JWTAuthenticationMixin():
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
