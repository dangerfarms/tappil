import ast
from rest_framework import serializers
from tappil.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        depth = 1

    def get_meta_data(self, obj):
        return ast.literal_eval(obj.meta_data)