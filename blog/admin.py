from django.contrib import admin
from .models import Post, Comment, Choice, Poll, Vote
from django_summernote.admin import SummernoteModelAdmin


# Choice, Poll, and Vote were added in line 2

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# Choice, Poll, and Vote were added below


@admin.register(Choice)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'body', 'post', 'created_on', 'approved') was removed from below
    list_display = ('name',)
    # list_filter = ('approved', 'created_on') orginal line changed to line below
    # list_filter = ('created_on',) was removed from below
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Poll)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'body', 'post', 'created_on', 'approved') was removed from below
    list_display = ('name',)
    # list_filter = ('approved', 'created_on') orginal line changed to line below
    # list_filter = ('created_on',) was removed from below
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Vote)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'body', 'post', 'created_on', 'approved') was removed from below
    # list_filter = ('approved', 'created_on') orginal line changed to line below
    # list_filter = ('created_on',) was removed from below
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
