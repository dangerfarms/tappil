from django.views.generic import View, TemplateView
import user_agents


class Activation(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        ua_string = request.META['HTTP_USER_AGENT']
        user_agent = user_agents.parse(ua_string)
        ip = request.META['REMOTE_ADDR']
        metadata = request.GET
        referrer = request.META.get('HTTP_REFERER', '')

        return self.render_to_response({
            'request': str(request),
            'user_agent': user_agent,
            'ip': ip,
            'metadata': metadata,
            'referrer': referrer,
        })


