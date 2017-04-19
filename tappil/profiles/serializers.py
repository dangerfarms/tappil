from rest_framework import serializers

from tappil.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'

    def get_meta_data(self, obj):
        return obj.meta_data


class ProfileIPSerializer(serializers.ModelSerializer):
    referrer = serializers.ReadOnlyField(source='link.code')
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'

    def get_meta_data(self, obj):
        return obj.meta_data
