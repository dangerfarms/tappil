from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from tappil.links.models import Link
from tappil.profiles.models import Profile
from tappil.referrers.models import Referrer


class ProfileMatchTest(APITestCase):

    def test_should_update_profile_to_match_on_success(self):
        deep_link = 'pinseekerz://activate?param=true#/path/to/go/to'
        r = Referrer.objects.create(name='test-referrer')
        l = Link.objects.create(code='code', referrer=r, deep_link=deep_link)
        p = Profile.objects.create(ip='1.1.1.1', link=l)
        phone_data = {
            'device_os': 'iOS',
        }

        response = self.client.post(reverse('profile-match'), phone_data, **{'REMOTE_ADDR':'1.1.1.1'})

        self.assertEqual(response.data['link']['deep_link'], deep_link)

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

        response = self.client.post(reverse('profile-match'), phone_data, **{'REMOTE_ADDR':'1.1.1.1'})

        self.assertEqual(response.data['link']['deep_link'], deep_link)
        self.assertEqual(response.data['id'], p.id)