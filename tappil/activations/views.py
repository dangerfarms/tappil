from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, TemplateView
from tappil.links.models import Link
from tappil.profiles.models import Profile
from tappil.referrers.models import Referrer
import user_agents


referrer = Referrer.objects.get_or_create(name='MeAndMyGolf')[0]
Link.objects.get_or_create(
    code='test',
    referrer=referrer,
    deep_link="pinseekerz:///path/to/something?params=are&great=no#/fragment/maybe/a/better/url/route"
)


class Activation(TemplateView):
    template_name = 'index.html'

    def match_profile(self):
        pass

    def set_profile(self, profile):
        ua_string = self.request.META['HTTP_USER_AGENT']
        user_agent = user_agents.parse(ua_string)

        profile.device_family = user_agent.device.family
        profile.device_os = user_agent.os.family
        profile.device_version = user_agent.os.version_string

        profile.meta_data = dict(self.request.GET)

    def generate_response(self, profile, link):
        if profile.device_family == 'iPhone':
            return redirect(link.deep_link)
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
        profile, created = Profile.objects.get_or_create(ip=ip)
        self.set_profile(profile)

        return self.generate_response(profile, link)


class Match(TemplateView):

    pass