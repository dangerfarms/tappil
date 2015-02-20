from rest_framework import serializers
from tappil.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        depth = 1