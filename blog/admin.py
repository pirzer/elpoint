from django.contrib import admin
from .models import Post, Comment, Choice, Poll, Vote

# Choice, Poll, and Vote are part of Poll option

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
