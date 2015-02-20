from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from tappil.links.models import Link
from tappil.links.response import DeepLinkRedirect
from tappil.profiles.models import Profile
import user_agents


class Activation(TemplateView):
    template_name = 'index.html'

    def set_profile(self, profile):
        ua_string = self.request.META['HTTP_USER_AGENT']
        user_agent = user_agents.parse(ua_string)

        profile.device_family = user_agent.device.family
        profile.device_os = user_agent.os.family
        profile.device_version = user_agent.os.version_string

        profile.meta_data = dict(self.request.GET)
        profile.save()

    def generate_response(self, profile, link):
        if profile.device_family == 'iPhone':
            return DeepLinkRedirect(link.deep_link)
        return self.render_to_response({'profile': profile})

    def get_link(self):
        link_code = self.kwargs['code']
        return get_object_or_404(Link, code=link_code)

    def get(self, request, *args, **kwargs):
        """
        Fetch the referrers link


        """
        link = self.get_link()

        ip = request.META['REMOTE_ADDR']
        profile, created = Profile.objects.get_or_create(ip=ip, link=link)
        self.set_profile(profile)

        return self.generate_response(profile, link)