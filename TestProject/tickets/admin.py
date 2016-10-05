from django.contrib import admin
from tickets.models import *

admin.site.register(AdminComment)
admin.site.register(UserComment)
admin.site.register(Ticket)
admin.site.register(Profile)

