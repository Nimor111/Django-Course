import factory
from .models import Tag, BlogPost
from faker import Factory


faker = Factory.create()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: faker.word())


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyAttribute(lambda _: faker.word())
    content = factory.LazyAttribute(lambda _: faker.text())
    created_at = faker.date_time()
    updated_at = faker.date_time()

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.tags.add(group)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.authors.add(group)
