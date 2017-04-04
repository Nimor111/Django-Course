import factory
from moneyed import Money, EUR
from djmoney.models.fields import MoneyField
from .models import Category, Offer

from faker import Factory

from django.contrib.auth.models import User

faker = Factory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: faker.word())


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    title = factory.LazyAttribute(lambda _: faker.word())
    description = factory.LazyAttribute(lambda _: faker.word())
    price = Money(100, EUR)
    created_at = faker.date_time()
    category = factory.SubFactory(CategoryFactory)
    image = factory.django.ImageField(color='blue')
