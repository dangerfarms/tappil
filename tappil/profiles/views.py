from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from tappil.profiles.models import Profile
from tappil.profiles.serializers import ProfileSerializer


class ProfileMatch(APIView):

    def match_profile(self, ip, data):
        """
        Algorithm to match a profile.

        Currently very basic, improve by first checking against a UUID, then IP
        """
        profiles_with_ip = list(Profile.objects.filter(ip=ip))
        best_match = None
        best_score = 0
        if profiles_with_ip:
            best_match = profiles_with_ip[0]
            profile_field_checks = ['device_family', 'device_os', 'device_version']
            for p in profiles_with_ip:
                score = sum(
                    map(lambda x: 1,
                        filter(lambda x: data.get(x) == getattr(p, x), profile_field_checks
                        )
                    )
                )
                if score > best_score:
                    best_match = p
                    best_score = score
        return best_match

    def post(self, request, *args, **kwargs):
        """
        Attempt to match a profile from a mobile SDK call.
        """
        ip = request.META['REMOTE_ADDR']
        data = request.data
        profile = self.match_profile(ip, data)
        profile.uuid = request.data.get('uuid', None)
        if not profile.installed_on:
            profile.installed_on = timezone.now()
        profile.save()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
