from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from tappil.links.models import Link
from tappil.profiles.models import Profile
import user_agents


PIN_SEEKERZ_URL = ''
APP_STORE_URL = ''
PLAY_STORE_URL = ''


class Activation(TemplateView):
    template_name = 'index.html'

    STORE_URLS = {
        'Android': 'https://play.google.com/store/apps/details?id=com.pinseekerz.www',
        'iOS': 'https://itunes.apple.com/gb/app/pin-seekerz-golf-world-ranking/id933904752',
        'default': 'http://www.pinseekerz.com',
    }

    def get_user_agent(self):
        ua_string = self.request.META['HTTP_USER_AGENT']
        user_agent = user_agents.parse(ua_string)
        return ua_string, user_agent

    def set_profile(self, profile):
        ua_string, user_agent = self.get_user_agent()
        profile.user_agent = ua_string
        profile.device_family = user_agent.device.family
        profile.device_os = user_agent.os.family
        profile.device_version = user_agent.os.version_string

        profile.meta_data = {k: v for k, v in self.request.GET.items()}

        profile.save()

    def generate_response(self, profile, link):
        redirect_url = self.STORE_URLS.get(profile.device_os, self.STORE_URLS['default'])
        return HttpResponseRedirect(redirect_url)

    def get_link(self):
        link_code = self.kwargs['code']
        return get_object_or_404(Link, code=link_code)

    def get(self, request, *args, **kwargs):
        """
        Fetch the referrers link


        """
        user_string, agent = self.get_user_agent()
        import ipdb; ipdb.set_trace()

        link = self.get_link()

        ip = request.META['REMOTE_ADDR']
        profile, created = Profile.objects.get_or_create(ip=ip, link=link)
        self.set_profile(profile)

        return self.generate_response(profile, link)