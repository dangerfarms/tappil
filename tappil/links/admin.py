from django.contrib import admin
from tappil.links.models import Link


class LinkAdmin(admin.ModelAdmin):

    list_display = ('code', 'referrer', 'deep_link')

admin.site.register(Link, LinkAdmin)