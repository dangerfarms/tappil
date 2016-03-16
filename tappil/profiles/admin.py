from django.contrib import admin
from tappil.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('uuid', 'ip', 'device_family', 'device_os', 'device_version', 'user_agent')
    search_fields = ('uuid', 'ip',)


admin.site.register(Profile, ProfileAdmin)