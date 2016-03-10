import factory


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'links.Link'
