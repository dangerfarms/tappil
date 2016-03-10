import factory


class ReferrerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'referrers.Referrer'
