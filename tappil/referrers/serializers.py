from rest_framework import serializers


class ReferralForIpSerializer(serializers.Serializer):

    ip = serializers.IPAddressField()
    user_joined_on = serializers.DateTimeField(required=False)
