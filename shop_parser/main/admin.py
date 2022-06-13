from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_joined', 'email')
    search_fields = ('username', 'email', 'send_messages')
    fields = (('username', 'email'),
                ('send_messages', 'is_active'),
                ('is_staff', 'is_superuser'),
                ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')




admin.site.register(User, UserAdmin)
admin.site.unregister(Group)