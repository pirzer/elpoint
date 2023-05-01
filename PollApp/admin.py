from django.contrib import admin

from PollApp.models import Choice, Poll, Vote

# Register your models here, line 3 updated with User
# line 8 added admin.site.register(User)

admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
