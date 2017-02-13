from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from tappil.devices.models import Device
from tappil.profiles.models import Profile
from tappil.profiles.serializers import ProfileSerializer


class ProfileMatch(APIView):

    def match_profile(self, ip):
        """Return the most recently logged user with a given IP or None"""
        return Profile.objects.filter(ip=ip).order_by('-date_created').first()

    def post(self, request, *args, **kwargs):
        """
        Attempt to match a profile from a mobile SDK call.
        """
        ip = request.META['HTTP_X_FORWARDED_FOR']
        data = request.data

        device_lookup = {
            'uuid': data.get('device_uuid'),
            'family': data.get('device_family'),
            'os': data.get('device_platform'),
            'version': data.get('device_version'),
        }
        device, created = Device.objects.get_or_create(**device_lookup)

        profile = self.match_profile(ip)
        if profile:
            device_uuid = request.data.get('device_uuid', None)
            if device_uuid == 'uuid removed manually':
                profile.uuid = 'No UUID given: Profile {0}'.format(profile.id)
            else:
                profile.uuid = device_uuid
            new_install = profile.installed_on is None
            if new_install:
                profile.installed_on = timezone.now()
            profile.save()
            serializer = ProfileSerializer(profile)
            # TODO: this is not nice at all, sorry (balint)
            data = serializer.data
            data['new_install'] = new_install
            # return Response(data)
            # TODO: Get back in when it's all nice and working.
        return Response({'new_install': True})
