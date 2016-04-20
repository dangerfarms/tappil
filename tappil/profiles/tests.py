from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from tappil.links.models import Link
from tappil.profiles.models import Profile
from tappil.referrers.models import Referrer


class ProfileMatchTest(APITestCase):
    deep_link = 'pinseekerz://activate?param=true#/path/to/go/to'

    def create_profile(self):
        r = Referrer.objects.create(name='test-referrer')
        l = Link.objects.create(code='code', referrer=r, deep_link=self.deep_link)
        Profile.objects.create(ip='1.1.1.1', link=l)

    def test_should_update_profile_to_match_on_success(self):
        self.create_profile()
        phone_data = {
            'device_os': 'iOS',
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})

        self.assertEqual(response.data['link']['deep_link'], self.deep_link)

    def test_should_find_best_possible_match(self):
        """
        Simulate 2 people that have come through the same IP, but on different phones. Make sure that
        the correct device is matched.

        In future check for UUID first to guarantee matching. Also remove matched profiles.
        :return:
        """
        deep_link = 'pinseekerz://'
        r = Referrer.objects.create(name='test-referrer')
        l = Link.objects.create(code='code', referrer=r, deep_link=deep_link)
        p = Profile.objects.create(ip='1.1.1.1', link=l, device_family='iPhone')

        unused_deep_link = 'pinseekerz://unused'
        r = Referrer.objects.create(name='unseen-referrer')
        l = Link.objects.create(code='unseen-code', referrer=r, deep_link=unused_deep_link)
        bad_profile = Profile.objects.create(ip='1.1.1.1', link=l, device_family='android')

        phone_data = {
            'device_family': 'iPhone',
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})

        self.assertEqual(response.data['link']['deep_link'], deep_link)
        self.assertEqual(response.data['id'], p.id)

    def test_should_return_new_install_field_for_new_installs(self):
        self.create_profile()
        phone_data = {
            'device_os': 'iOS',
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})
        self.assertEqual(response.data['new_install'], True)

    def test_should_return_non_matching_new_install_field_for_new_installs(self):
        phone_data = {
            'device_os': 'iOS',
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})
        self.assertEqual(response.data['new_install'], True)

    def test_should_return_false_new_install_field_for_not_new_installs(self):
        self.create_profile()
        phone_data = {
            'device_os': 'iOS'
        }

        # initial create
        self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})

        # second call
        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})
        self.assertEqual(response.data['new_install'], False)

    def test_should_return_400_on_bad_input_not_500(self):
        self.create_profile()
        phone_data = {
            "device_family": "undefined",
            "device_uuid": "uuid removed manually",
            "device_platform": "browser",
            "device_version": "browser"
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'HTTP_X_FORWARDED_FOR': '1.1.1.1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)