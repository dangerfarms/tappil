from django.contrib import admin
from tappil.devices.models import Device


class DeviceAdmin(admin.ModelAdmin):

    list_display = ('uuid', 'family', 'os', 'version',)

admin.site.register(Device)