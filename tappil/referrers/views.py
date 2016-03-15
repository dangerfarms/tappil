from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from tappil.profiles.models import Profile
from tappil.referrers.serializers import ReferralForIpSerializer


class ReferrerForIp(APIView):

    URL_NAME = 'referrer-for-ip'

    def get_closest_profile_installation(self, queryset, given_time):
        """
        Return the minimum difference in time between entries and the
        given time, transformed by a key function.
        """
        def time_difference(profile):
            return abs((given_time - profile.installed_on).total_seconds())
        return min(queryset, key=time_difference)

    def get(self, request, *args, **kwargs):
        """
        Return the referrer name who best matches the given IP. If no timestamp given, return the earliest entry.
        """
        serializer = ReferralForIpSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        ip = serializer.validated_data['ip']
        profiles = Profile.objects.filter(ip=ip)
        if not profiles.exists():
            raise NotFound()
        try:
            user_joined_date = serializer.validated_data['user_joined_on']
            profile = self.get_closest_profile_installation(profiles, user_joined_date)
        except (KeyError, TypeError):
            profile = profiles.order_by('installed_on').first()
        return Response({'referrer': profile.link.referrer.name})
