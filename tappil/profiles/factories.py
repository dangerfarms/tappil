import factory


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'profiles.Profile'
