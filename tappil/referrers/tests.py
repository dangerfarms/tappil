from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from tappil.links.factories import LinkFactory
from tappil.profiles.factories import ProfileFactory
from tappil.referrers.factories import ReferrerFactory
from tappil.referrers.views import ReferrerForIp


class ReferrerForIpTest(APITestCase):
    url = reverse(ReferrerForIp.URL_NAME)

    def tearDown(self):
        self.client.logout()

    def aware_datetime(self, *args):
        return timezone.make_aware(datetime(*args), timezone.get_current_timezone())

    def login(self):
        User.objects.create_superuser(username='user', email='admin@referrals.pinseekerz.com', password='password')
        self.client.login(username='user', password='password')

    def test_should_return_response(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response, Response)

    def test_should_return_unauthorized_if_user_is_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_return_bad_request_if_no_ip_query_param(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_return_bad_request_if_ip_is_blank(self):
        ip = ''
        self.login()
        response = self.client.get(self.url, {'ip': ip})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_return_referrer_if_ip_matches_profile_ip(self):
        """
        Test that sending an IP existing in the database returns the correct referrer
        """
        self.login()
        ip = '123.123.123.123'
        referrer_name = 'peterFinch'

        referrer = ReferrerFactory(name=referrer_name.upper())
        link = LinkFactory(referrer=referrer, code=referrer_name)
        profile = ProfileFactory(ip=ip, link=link)

        response = self.client.get(self.url, {'ip': ip})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['referrer'], referrer_name)

    def test_should_return_not_found_if_ip_does_not_match_any_profile(self):
        """Test that if no IPs match the given IP, then return a 404"""
        self.login()
        ip = '123.123.123.123'

        response = self.client.get(self.url, {'ip': ip})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_return_referrer_of_profile_who_installed_app_closest_to_given_time(self):
        """
        Test that given three IP 'registers' (which could have come from 3 people on the same network at different
         times), the referrer of the Profile that is nearest to the provided time is returned.

         In this instance, the middle record is closest to the provided time.
        """
        self.login()
        ip = '123.123.123.123'
        referrer_name = 'peterFinch'
        other_referrer_name = 'richShiels'

        referrer = ReferrerFactory(name=referrer_name.upper())
        other_referrer = ReferrerFactory(name=other_referrer_name.upper())

        link = LinkFactory(referrer=referrer, code=referrer_name)
        other_link = LinkFactory(referrer=other_referrer, code=other_referrer_name)

        ProfileFactory(ip=ip, link=other_link, installed_on=self.aware_datetime(2015, 12, 29, 0, 0))
        ProfileFactory(ip=ip, link=link, installed_on=self.aware_datetime(2015, 12, 30, 0, 0))
        ProfileFactory(ip=ip, link=other_link, installed_on=self.aware_datetime(2016, 1, 5, 0, 0))

        response = self.client.get(self.url, {
            'ip': ip,
            'user_joined_on': '2015-12-30T09:00:00Z'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['referrer'], referrer_name)

    def test_should_return_referrer_from_profiles_containing_installed_on_entries(self):
        self.login()
        ip = '123.123.123.123'
        referrer_name = 'peterFinch'
        other_referrer_name = 'richShiels'

        referrer = ReferrerFactory(name=referrer_name.upper())
        other_referrer = ReferrerFactory(name=other_referrer_name.upper())

        link = LinkFactory(referrer=referrer, code=referrer_name)
        other_link = LinkFactory(referrer=other_referrer, code=other_referrer_name)

        ProfileFactory(ip=ip, link=other_link)
        ProfileFactory(ip=ip, link=link, installed_on=self.aware_datetime(2015, 12, 30, 0, 0))
        ProfileFactory(ip=ip, link=other_link)
        ProfileFactory(ip=ip, link=other_link)

        response = self.client.get(self.url, {
            'ip': ip,
            'user_joined_on': '2015-12-30T09:00:00Z'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['referrer'], referrer_name)
