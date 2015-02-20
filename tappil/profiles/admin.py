from django.contrib import admin
from tappil.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('uuid', 'ip', 'device_family', 'device_ios', 'device_version')


admin.site.register(Profile)